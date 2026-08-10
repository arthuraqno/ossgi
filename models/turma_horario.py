from sqlalchemy import Column, Integer, String, ForeignKey, Time
from base import Base

class TurmaHorario(Base):
    __tablename__ = "turma_horarios"
    
    id = Column(Integer, primary_key=True)
    turma_id = Column(Integer, ForeignKey("turmas.id"))
    dia_semana = Column(String(50), nullable=False)
    horario_inicio = Column(Time, nullable=False)
    horario_fim = Column(Time, nullable=False)
    
    