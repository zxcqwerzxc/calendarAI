from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.params_schemas import CreateParams, GetParams
from src.db.postgres.repositories.params_repository import ParamsRepository



class ParamsService:
    async def create_params(self, data: CreateParams, db_session: AsyncSession):
        params_repository = ParamsRepository(db_session)
        params = await params_repository.create_params(data)
        return params

    async def get_params(self, user_id, db_session: AsyncSession):
        params_repository = ParamsRepository(db_session)
        params_data = await params_repository.get_params(user_id)

        return GetParams(
            id=params_data.id,
            description=params_data.description
        )

    async def upsert_params(self, data: CreateParams, db_session: AsyncSession):
        params_repository = ParamsRepository(db_session)
        params = await params_repository.upsert_params(data)
        return params