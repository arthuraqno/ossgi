from sqlalchemy.orm import Session
from models.usuario import Usuario
from database import engine
from auth import gerar_hash_senha

class UsuarioService:
    def cadastrar_usuario(self, email, senha, role, professor_id=None):
        with Session(engine) as session:
            senha_hash = gerar_hash_senha(senha)
            usuario = Usuario(
                email=email,
                senha=senha_hash,
                role=role,
                professor_id=professor_id)
            session.add(usuario)
            session.commit()
            print(f"Usuário {email} cadastrado com sucesso!")

    def buscar_usuario(self, email):
        with Session(engine) as session:
            usuario = session.query(Usuario).filter(Usuario.email == email).first()
            return usuario