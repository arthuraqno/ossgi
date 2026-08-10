from fastapi import APIRouter
from pydantic import BaseModel
from services.usuario import UsuarioService
from auth import verificar_senha, criar_token

class UsuarioCreate(BaseModel):
    email : str
    senha : str
    role : str
    professor_id : int | None = None

class LoginRequest(BaseModel):
    email: str
    senha: str

router = APIRouter()
usuario_service = UsuarioService()

@router.post("/usuarios")
def cadastrar_usuario(dados: UsuarioCreate):
    usuario_service.cadastrar_usuario(
        email=dados.email,
        senha=dados.senha,
        role=dados.role,
        professor_id=dados.professor_id)
    return {"mensagem": f"Usuário {dados.email} cadastrado com sucesso!"}

@router.post("/usuarios/login")
def login_usuario(dados: LoginRequest):
    usuario = usuario_service.buscar_usuario(dados.email)
    if usuario is None:
        return {"erro": "Email não cadastrado"}

    if not verificar_senha(dados.senha, usuario.senha):
        return {"erro": "Senha incorreta"}

    token = criar_token({"email": usuario.email, "role": usuario.role})
    return {"access_token": token, "token_type": "bearer"}

    