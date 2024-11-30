from sqlalchemy import Column, Integer, Sequence, String

from base_model import BaseModel
from main import db

class User(BaseModel):
    """
    Models to describe a user in system.
    """
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(128), nullable=False)
