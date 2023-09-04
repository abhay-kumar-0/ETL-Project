from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine(
    "postgresql+psycopg2://postgres:Abhayk@localhost:5432/campdata_prod"
)
session = Session(engine)
