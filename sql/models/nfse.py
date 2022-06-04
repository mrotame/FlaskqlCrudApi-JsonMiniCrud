from sqlalchemy import *
from sql.sqlbase import base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict

class Nfse(base):
    __tablename__ = 'nfse'
    id = Column(Integer, primary_key=True)
    id_company = Column(Integer)
    dt_emissao = Column(DateTime)
    num_nfse = Column(String(20))
    cod_verif = Column(String(40))
    cnpj_prest = Column(String(14))
    xml_nota = Column(Text)
    json_nota = Column(MutableDict.as_mutable(JSONB))