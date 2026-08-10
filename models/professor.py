from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from base import Base
from datetime import date 

class Professor(Base):
    __tablename__ = "professores"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    faixa = Column(String(50), nullable=False)
    graus = Column(Integer, nullable=False)
    data_contratacao = Column(Date, nullable=False, default=date.today)
    ativo = Column(Boolean)
    
