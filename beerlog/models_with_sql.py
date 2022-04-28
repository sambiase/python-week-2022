from typing import Optional  # this import is to tell Python that the ID field will not be passed by the user
from sqlmodel import SQLModel, select, Field
from pydantic import validator  # used to validate errors, EX: cost cannot be greater than 10


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)  # primary key is mandatory
    name: str
    style: str
    flavor: int
    image: int
    cost: int

    @validator('flavor', 'image', 'cost')
    def validate_rating(cls, v, field):  # v = value
        if v < 1 or v > 10:
            raise RuntimeError(f'{field.name} must be between 1 and 10')
        return v


brahma = Beer(name='Brahma', style='NEIPA', flavor=7, image=1, cost=10)
