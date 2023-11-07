from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, PositiveInt


class DonationsBase(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationsCreate(DonationsBase):
    pass


class DonationsDB(DonationsBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationsGet(DonationsDB):
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]
