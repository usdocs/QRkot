from sqlalchemy import Column, Integer, ForeignKey, Text

from app.core.db import AbstractBase


class Donation(AbstractBase):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
