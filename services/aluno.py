from sqlalchemy.orm import Session
from models.aluno import Aluno
from database import engine
from datetime import date

class AlunoService:
    def cadastrar_alunos(self, nome, telefone, email, data_nascimento, faixa, graus, turma_id):
        with Session(engine) as session:
            aluno = Aluno(
                nome = nome, 
                telefone = telefone,
                email = email,
                data_nascimento=data_nascimento,
                faixa=faixa,
                graus=graus,
                data_matricula=date.today(),
                ativo=True,
                turma_id=turma_id)
            session.add(aluno)
            session.commit()
            print(f"{nome} cadastrado com sucesso!")
            
    def listar_alunos(self):
        with Session(engine) as session:
            alunos = session.query(Aluno).all()
            return alunos
                
    def buscar_aluno(self, nome):
        with Session(engine) as session:
            aluno = session.query(Aluno).filter(Aluno.nome.ilike(nome)).first()
            return aluno
    
    def atualizar_aluno(self, id, faixa=None, graus=None, ativo=None, turma_id=None, telefone=None):
        with Session(engine) as session:
            aluno = session.get(Aluno, id)
            if aluno is None:
                print("Aluno não encontrado!")
                return
            
            if faixa is not None:
                aluno.faixa = faixa
            if graus is not None:
                aluno.graus = graus
            if ativo is not None:
                aluno.ativo = ativo
            if turma_id is not None:
                aluno.turma_id = turma_id
            if telefone is not None:
                aluno.telefone = telefone
            
            session.commit() 
            print(f"{aluno.nome} atualizado com sucesso!")
        
    def desativar_aluno(self, nome):
        with Session(engine) as session:
            aluno = session.query(Aluno).filter(Aluno.nome.ilike(nome)).first()
            if aluno is None:
                print("Aluno não encontrado!")
                return
            aluno.ativo = False
            session.commit()
            print(f"{aluno.nome} foi desativado.")