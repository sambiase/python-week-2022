from sqlmodel import create_engine # create_engine is the object used to connect to the DB
from beerlog.config import settings
from beerlog import models_with_sql # this import will get Beer class and use it to create a Table in SQL

engine = create_engine(settings.database.url)

models_with_sql.SQLModel.metadata.create_all(engine) #table creation




