from sqlalchemy import Column, String, Integer, DECIMAL, DateTime
from gerenciador.database import Base


class Gerenciador(Base):

    __tablename__ = "gerenciador"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(100))
    data_compra = Column(String(20))
    valor = Column(DECIMAL)
    vencimento = Column(String(20))
    data_criacao = Column(DateTime)