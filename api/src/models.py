from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from .database import Base

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)