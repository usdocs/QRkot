from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession


def close_model(model):
    model.invested_amount = model.full_amount
    model.fully_invested = True
    model.close_date = datetime.now()
    return model


def calculating(model_in, db_model):
    amount_db_model = db_model.full_amount - db_model.invested_amount
    amount_model_in = model_in.full_amount - model_in.invested_amount

    if amount_model_in < amount_db_model:
        db_model.invested_amount += amount_model_in
        model_in = close_model(model_in)
    if amount_model_in == amount_db_model:
        model_in = close_model(model_in)
        db_model = close_model(db_model)
    if amount_model_in > amount_db_model:
        model_in.invested_amount += amount_db_model
        db_model = close_model(db_model)

    return model_in, db_model


async def investing(
        model_in,
        crud_model,
        session: AsyncSession,
):
    while model_in.invested_amount < model_in.full_amount:
        db_model = await crud_model.get_by_attribute(
            attr_name='fully_invested',
            attr_value=False,
            session=session,
        )
        if not db_model:
            break
        model_in, db_model = calculating(model_in, db_model)
        session.add(db_model)

    session.add(model_in)
    await session.commit()
    await session.refresh(model_in)
    return model_in
