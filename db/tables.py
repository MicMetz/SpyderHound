from typing import Any, Sequence
from psycopg import Column
from sqlalchemy import String, Integer, ForeignKey

from db.database import Base



class chan_session(Base):
    __tablename__ = 'chan_session'
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    start_time = Column(String)
    finish_time = Column(String)
    total_hosts = Column(String)
    posts = Column(String)
    posters = Column(String)

    def __init__(self, filename, start_time, finish_time, total_hosts='0', posts='0', posters='0'):
        self.filename = filename
        self.start_time = start_time
        self.finish_time = finish_time
        self.total_hosts = total_hosts
        self.posts = posts
        self.posters = posters



class red_session(Base):
    __tablename__ = 'red_session'
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    start_time = Column(String)
    finish_time = Column(String)
    total_hosts = Column(String)
    posts = Column(String)
    posters = Column(String)

    def __init__(self, filename, start_time, finish_time, total_hosts='0', posts='0', posters='0'):
        self.filename = filename
        self.start_time = start_time
        self.finish_time = finish_time
        self.total_hosts = total_hosts
        self.posts = posts
        self.posters = posters



class note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('chan_host.id'))
    text = Column(String)

    def __init__(self, host_id, text):
        self.text = str(text)
        self.host_id = host_id
