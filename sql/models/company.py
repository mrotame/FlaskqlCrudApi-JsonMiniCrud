from sqlalchemy import *
from sql.sqlbase import base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict

class Company(base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    razao = Column(String)
    cnpj = Column(String)
    