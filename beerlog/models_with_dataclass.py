from dataclasses import dataclass


@dataclass
class Beer:
    name: str
    style: str
    flavor: int
    image: int
    cost: int


brahma = Beer(name='Brahma', style='NEIPA', flavor=6, image=8, cost=10)

