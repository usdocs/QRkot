from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    project_id = await charity_project_crud.get_by_attribute(
        attr_name='name',
        attr_value=project_name,
        session=session
    )
    if project_id is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Проект с таким именем уже существует!',
        )


async def check_charity_project_exists(
        charity_project_id: int,
        session: AsyncSession,
) -> CharityProject:
    charity_project = await charity_project_crud.get(
        charity_project_id, session
    )
    if charity_project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Проект не найдена!'
        )
    return charity_project


async def check_project_before_delete(
        charity_project_id: int,
        session: AsyncSession,
) -> CharityProject:
    charity_project = await check_charity_project_exists(
        charity_project_id, session
    )
    if charity_project.invested_amount > 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='В проект были внесены средства, не подлежит удалению!'
        )
    return charity_project


async def check_project_before_edit(
        charity_project_id: int,
        session: AsyncSession,
) -> CharityProject:
    charity_project = await check_charity_project_exists(
        charity_project_id, session
    )
    if charity_project.fully_invested:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Закрытый проект нельзя редактировать!'
        )
    return charity_project


async def check_invested_amount(
        full_amount: int,
        charity_project: CharityProject,
        session: AsyncSession,
) -> None:
    if full_amount < charity_project.invested_amount:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Нельзя установить требуемую сумму меньше уже вложенной!',
        )
