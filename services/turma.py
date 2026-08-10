from sqlalchemy.orm import Session
from models.turma import Turma
from database import engine
from datetime import date

class TurmaService:
    def cadastrar_turma(self, nome, nivel, categoria, professor_id):
        with Session(engine) as session:
            turma = Turma(
                nome = nome,
                nivel = nivel,
                categoria = categoria,
                professor_id = professor_id)
            session.add(turma)
            session.commit()
            print(f"Turma {nome} cadastrada com sucesso!")
    
    def listar_turmas(self):
        with Session(engine) as session:
            turmas = session.query(Turma).all()
            return turmas
    
    def buscar_turma(self, nome):
        with Session(engine) as session:
            turma = session.query(Turma).filter(Turma.nome.ilike(nome)).first()            
            return turma
    
    def atualizar_turma(self, id, novo_nome=None, nivel=None, categoria=None, professor_id=None):
        with Session(engine) as session:
            turma = session.get(Turma, id)
            if turma is None:
                print("Não há turmas cadastradas")
                return
            
            if nivel is not None:
                turma.nivel = nivel
            if categoria is not None:
                turma.categoria = categoria
            if professor_id is not None:
                turma.professor_id = professor_id
            if novo_nome is not None:
                turma.nome = novo_nome

            session.commit()
            print(f"Turma {turma.nome} atualizada com sucesso!")