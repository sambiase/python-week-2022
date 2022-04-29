from typing import Optional  # this import is to tell Python that the ID field will not be passed by the user
from sqlmodel import SQLModel, select, Field
from pydantic import validator  # used to validate errors, EX: cost cannot be greater than 10
from statistics import mean  # library used to calculate average
from datetime import datetime


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)  # primary key is mandatory
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    @validator('flavor', 'image', 'cost')
    def validate_rating(cls, v, field):  # v = value
        if v < 1 or v > 10:
            raise RuntimeError(f'{field.name} must be between 1 and 10')
        return v

    @validator('rate',always=True)      # always=True means that this function will always be executed
    def average_calc(cls, v, values):
        rate = mean([values['flavor'], values['image'], values['cost']])
        return int(rate)


brahma = Beer(name='Brahma', style='NEIPA', flavor=7, image=1, cost=10)

