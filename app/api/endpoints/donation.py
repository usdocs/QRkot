from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.models import User
from app.services.investing import investing
from app.schemas.donation import (
    DonationsCreate, DonationsDB, DonationsGet
)

router = APIRouter()


@router.get(
    '/',
    response_model=list[DonationsGet],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    """Только для суперюзеров.\n
    Возвращает список всех пожертвований."""
    return await donation_crud.get_multi(session)


@router.post(
    '/',
    response_model=DonationsDB,
    response_model_exclude_none=True,
)
async def create_donation(
        reservation: DonationsCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    """Сделать пожертвование."""
    new_donation = await donation_crud.create(
        reservation, session, user
    )
    return await investing(new_donation, charity_project_crud, session)


@router.get(
    '/my',
    response_model=list[DonationsDB],
)
async def get_my_reservations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Вернуть список пожертвований пользователя, выполняющего запрос."""
    return await donation_crud.get_by_user(user=user, session=session)
