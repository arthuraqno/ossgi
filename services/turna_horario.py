from models.turma_horario import TurmaHorario
from database import engine
from sqlalchemy.orm import Session

class TurmaHorarioService:
    def cadastrar_horarios(self, turma_id, dia_semana, horario_inicio, horario_fim):
        with Session(engine) as session:
            turma_horario = TurmaHorario(
                turma_id = turma_id,
                dia_semana = dia_semana,
                horario_inicio = horario_inicio,
                horario_fim = horario_fim)
            session.add(turma_horario)
            session.commit()
            print(f"Horario cadastrado com sucesso!")
            
    def listar_horarios_turma(self, turma_id):
        with Session(engine) as session:
            horarios = session.query(TurmaHorario).filter(TurmaHorario.turma_id == turma_id).all()
            return horarios