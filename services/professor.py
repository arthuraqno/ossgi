from sqlalchemy.orm import Session
from models.professor import Professor
from database import engine
from datetime import date

class ProfessorService:
    def cadastrar_professores(self, nome, telefone, email, data_nascimento, faixa, graus):
        with Session(engine) as session:
            professor = Professor(
            nome = nome,
            telefone = telefone,
            email = email,
            data_nascimento = data_nascimento,
            faixa = faixa,
            graus = graus,
            data_contratacao = date.today(),
            ativo = True)
            session.add(professor)
            session.commit()
            print(f"{nome} cadastrado com sucesso!")
            
    def listar_professores(self):
        with Session(engine) as session:
            professores = session.query(Professor).all()
            return professores
                
    def buscar_professor(self, nome):
        with Session(engine) as session:
            professor = session.query(Professor).filter(Professor.nome.ilike(nome)).first()
            return professor
        
    def atualizar_professor(self, id, faixa=None, graus=None, ativo=None, telefone=None):
        with Session(engine) as session:
            professor = session.get(Professor, id)
            
            if professor is None:
                print("Não há professores cadastrados")
                return
            
            if faixa is not None:
                professor.faixa = faixa
            if graus is not None:
                professor.graus = graus
            if ativo is not None:
                professor.ativo = ativo
            if telefone is not None:
                professor.telefone = telefone
            
            session.commit()
            print(f"{professor.nome} atualizado com sucesso!")
            
    def desativar_professor(self, nome):
        with Session(engine) as session:
            professor = session.query(Professor).filter(Professor.nome.ilike(nome)).first()
            if professor is None:
                print("Professor não encontrado!")
                return
            professor.ativo = False    
            session.commit()
            print(f"{professor.nome} foi desativado.")