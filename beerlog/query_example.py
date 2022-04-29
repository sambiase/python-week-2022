from sqlmodel import select, Session
from beerlog.models_with_sql import Beer
from beerlog.database import engine

# PRINT ALL BEER NAMES AND STYLES
with Session(engine) as session:  # this is the scope and it runs only once
    sql = select(Beer)
    res = session.exec(sql)
    for beer in res:
        print(f'Beer Name: {beer.name}')
        print(f'Beer Style: {beer.style}')

# ADD NEW BEER
with Session(engine) as session:
    new_beer = Beer(name='Antarctica', style='IPA', flavor=8, image=4, cost=10)  # dont need to pass rate and date.
    # They are both calculated by Python within models_with_sql Validators
    session.add(new_beer)
    session.commit()
