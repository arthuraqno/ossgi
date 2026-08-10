from fastapi import APIRouter
from services.aluno import AlunoService
from pydantic import BaseModel
from datetime import date

class AlunoCreate(BaseModel):
    nome: str
    telefone: str
    email: str
    data_nascimento: date
    faixa: str
    graus: int
    turma_id: int
    
class AlunoUpdate(BaseModel):
    faixa: str | None = None
    graus: int | None = None
    ativo: bool | None = None
    turma_id: int | None = None
    telefone: str | None = None 

router = APIRouter()
aluno_service = AlunoService()
    
@router.get("/alunos")
def listar_alunos():
    return aluno_service.listar_alunos()

@router.post("/alunos")
def cadastrar_alunos(dados: AlunoCreate):
    aluno_service.cadastrar_alunos(
        nome=dados.nome,
        telefone=dados.telefone,
        email=dados.email,
        data_nascimento=dados.data_nascimento,
        faixa=dados.faixa,
        graus=dados.graus,
        turma_id=dados.turma_id)
    return {"mensagem": f"{dados.nome} cadastrado com sucesso!"}

@router.put("/alunos/{id}")
def atualizar_aluno(id : int, dados: AlunoUpdate):
    aluno_service.atualizar_aluno(
        id = id,
        faixa=dados.faixa,
        graus=dados.graus,
        ativo=dados.ativo,
        turma_id=dados.turma_id,
        telefone=dados.telefone)
    return {"mensagem": "Aluno atualizado com sucesso!"}
    