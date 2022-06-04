import sqlalchemy.orm
from sqlalchemy import *
from sql.sqlbase import base
from sql.models.nfse import Nfse
from sql.models.company import Company

from os import environ

db_name = 'postgres'
db_username = 'admin'
db_password = 'admin'
db_url = '127.0.0.1'
db_port = 5432
db_dialect = 'postgresql'
uri_string = '%s://%s:%s@%s:%d/%s' %(db_dialect,db_username,db_password,db_url,db_port,db_name)
engine = sqlalchemy.create_engine(uri_string, echo=True)

session = sqlalchemy.orm.scoped_session(sqlalchemy.orm.sessionmaker(bind=engine))

base.metadata.create_all(engine)
