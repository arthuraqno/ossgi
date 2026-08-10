from fastapi import APIRouter
from pydantic import BaseModel
from services.turna_horario import TurmaHorarioService
from datetime import time

class TurmaHorarioCreate(BaseModel):
    turma_id: int
    dia_semana: str
    horario_inicio: time
    horario_fim: time

router = APIRouter()
turma_horario_service = TurmaHorarioService()

@router.get("/turmas/{turma_id}/horarios")
def listar_horarios_turma(turma_id: int):
    return turma_horario_service.listar_horarios_turma(turma_id)

@router.post("/turmas/horarios")
def cadastrar_horarios(dados: TurmaHorarioCreate):
    turma_horario_service.cadastrar_horarios(
        turma_id=dados.turma_id,
        dia_semana=dados.dia_semana,
        horario_inicio=dados.horario_inicio,
        horario_fim=dados.horario_fim)
    return {"mensagem": "Horário cadastrado com sucesso!"}