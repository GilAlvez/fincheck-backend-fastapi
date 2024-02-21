from sqlalchemy import create_engine
from sqlalchemy.orm import Session


DATABASE_URL = "postgresql://root:password@database/fincheck-db"

engine = create_engine(DATABASE_URL, echo=True)
db = Session(bind=engine)
