from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.params_schemas import CreateParams
from src.db.postgres.models.params import Params


class ParamsRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def create_params(self, data):
        new_params=Params(
            description=data.description,
            user_id=data.user_id
        )
        self._session.add(new_params)
        await self._session.commit()
        await self._session.refresh(new_params)

    async def get_params(self, user_id):
        query = (
            select(Params)
            .where(Params.user_id == user_id)
        )
        result = await self._session.execute(query)
        params = result.scalar_one_or_none()

        return params

    async def upsert_params(self, data: CreateParams) -> Params:
        query = (select(Params)
                 .where(Params.user_id == data.user_id))
        result = await self._session.execute(query)
        existing = result.scalar_one_or_none()

        if existing:
            existing.description = data.description
            params = existing
        else:
            params = Params(
                description=data.description,
                user_id=data.user_id
            )
            self._session.add(params)

        await self._session.commit()
        await self._session.refresh(params)

        return params

