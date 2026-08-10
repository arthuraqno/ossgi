from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from datetime import date  

class Aluno(Base):
    __tablename__ = "alunos"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    data_nascimento = Column(Date, nullable=False)
    faixa = Column(String(50), nullable=False)
    graus = Column(Integer, nullable=False)
    data_matricula = Column(Date, nullable=False, default=date.today)
    ativo = Column(Boolean)
    turma_id = Column(Integer, ForeignKey("turmas.id"))
    
    turma = relationship("Turma")
    
    
    
    
    
 