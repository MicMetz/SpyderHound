import os

from sqlalchemy import create_engine, String, Integer, Column, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import date as dt



class Database:
    connection = None
    cursor = None
    db_name = "spyderhound_db"
    db = None
    engine = None
    SessionMaker = None
    session = None
    Base = None


    def __init__(self):
        self.db = os.getenv(
            "DB", "postgresql+psycopg2://postgres:postgres@localhost:5432/spyderhound_db"
        )
        self.engine = create_engine(self.db)
        self.SessionMaker = sessionmaker(bind=self.engine)
        self.session = self.SessionMaker()
        self.Base = declarative_base()


class DatabaseController:
    def __init__(self):
        self.database = Database()


    def get_database(self):
        return self.database


    def get_session(self):
        return self.database.session


    def get_base(self):
        return self.database.Base


    def get_engine(self):
        return self.database.engine


    def get_session_maker(self):
        return self.database.SessionMaker


    def get_db(self):
        return self.database.db


    def get_db_name(self):
        return self.database.db_name


    def get_connection(self):
        return self.database.connection


    def get_cursor(self):
        return self.database.cursor


    def get_db(self):
        return self.database.db



class TargetModel:
    __tablename__ = "targets"

    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False)
    email = Column(String(255), nullable=True)
    image = Column(String(255), nullable=True)
    link = Column(String(255), nullable=True)
    header = Column(String(255), nullable=True)
    text = Column(Column(String(255), nullable=True))
    date = Column(Date, nullable=False)


    def __init__(self, url, email, image, link, header, text, date):
        self.url = url
        self.email = email
        self.image = image
        self.link = link
        self.header = header
        self.text = text
        self.date = dt.today()


    def __repr__(self):
        return f"{self.url} {self.email} {self.image} {self.link} {self.header} {self.text} {self.date}"


    def __str__(self):
        return f"{self.url} {self.email} {self.image} {self.link} {self.header} {self.text} {self.date}"



if __name__ == "__main__":
    print("Building Database Tables")
    db = DatabaseController()
    db.get_base().metadata.create_all(db.get_engine())
    print("Done")
