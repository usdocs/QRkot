from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_projects_by_completion_rate(
            self,
            session: AsyncSession,
    ) -> list[dict]:
        projects = await session.execute(
            select(
                (
                    func.julianday(CharityProject.close_date) -
                    func.julianday(CharityProject.create_date)
                ).label('collection_time'),
                CharityProject.name,
                CharityProject.description,
            ).where(
                CharityProject.close_date
            ).order_by('collection_time')
        )
        return projects.all()


charity_project_crud = CRUDCharityProject(CharityProject)
