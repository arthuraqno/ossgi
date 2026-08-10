from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from datetime import date 

class Turma(Base):
    __tablename__ = "turmas"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    nivel = Column(String(50), nullable=False)
    categoria = Column(String(50), nullable=False)
    professor_id = Column(Integer, ForeignKey("professores.id"))
    
    professor = relationship("Professor")
    horarios = relationship("TurmaHorario")