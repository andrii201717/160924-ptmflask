from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine("sqlite:///database.db", echo=True)

Base = declarative_base()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()