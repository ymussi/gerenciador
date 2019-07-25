from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, DECIMAL
from gerenciador.utils.conector.mysql import mysql_engine

engine = mysql_engine('pessoal')
meta = MetaData()

gerenciador = Table(
    'gerenciador', meta,
    Column('id', Integer, primary_key=True),
    Column('descricao', String(100)),
    Column('data_compra', String(20)),
    Column('valor', DECIMAL),
    Column('vencimento', String(20)),
    Column('data_criacao', String(20))
)
meta.create_all(engine)
# meta.drop_all(engine)