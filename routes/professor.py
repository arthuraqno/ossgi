from fastapi import APIRouter
from services.professor import ProfessorService
from datetime import date
from pydantic import BaseModel

class ProfessorCreate(BaseModel):
    nome : str
    telefone : str
    email : str
    data_nascimento : date
    faixa : str
    graus : int

class ProfessorUpdate(BaseModel):
    faixa : str | None = None
    graus : int | None = None
    ativo : bool | None = None
    telefone : str | None = None
    

router = APIRouter()
professor_service = ProfessorService()

@router.get("/professores")
def listar_professores():
    return professor_service.listar_professores()

@router.post("/professores")
def cadastrar_professores(dados: ProfessorCreate):
    professor_service.cadastrar_professores(
        nome = dados.nome,
        telefone = dados.telefone,
        email = dados.email,
        data_nascimento = dados.data_nascimento,
        faixa = dados.faixa,
        graus = dados.graus)
    return {"mensagem": f"{dados.nome} cadastrado com sucesso!"}

@router.put("/professores/{id}")
def atualizar_professor(id : int, dados : ProfessorUpdate):
    professor_service.atualizar_professor(
        id=id, 
        faixa=dados.faixa,
        graus=dados.graus,
        ativo=dados.ativo,
        telefone=dados.telefone)
    return {"mensagem": "Professor atualizado com sucesso!"}