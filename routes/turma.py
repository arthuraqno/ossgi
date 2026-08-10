from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.turma import TurmaService
from auth import obter_usuario_atual

class TurmaCreate(BaseModel):
    nome : str
    nivel : str
    categoria : str
    professor_id : int

class TurmaUpdate(BaseModel):
    nivel : str | None = None
    categoria : str | None = None
    professor_id : int | None = None
    novo_nome : str | None = None
    
router = APIRouter()
turma_service = TurmaService()

@router.get("/turmas")
def listar_turmas():
    return turma_service.listar_turmas()

@router.post("/turmas")
def cadastrar_turma(dados: TurmaCreate, usuario=Depends(obter_usuario_atual)):
    turma_service.cadastrar_turma(
        nome= dados.nome,
        nivel= dados.nivel,
        categoria= dados.categoria,
        professor_id= dados.professor_id)
    return {"mensagem": f"{dados.nome} cadastrado com sucesso!"}

@router.put("/turmas/{id}")
def atualizar_turma(id : int, dados: TurmaUpdate, usuario=Depends(obter_usuario_atual)):
    turma_service.atualizar_turma(
        id=id,
        nivel=dados.nivel,
        categoria=dados.categoria,
        professor_id=dados.professor_id,
        novo_nome=dados.novo_nome)
    return {"mensagem": "Turma atualizada com sucesso!"}