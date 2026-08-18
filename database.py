from sqlalchemy import create_engine
from base import Base
from dotenv import load_dotenv
import os
from models.aluno import Aluno
from models.professor import Professor
from models.turma import Turma
from models.turma_horario import TurmaHorario
from models.usuario import Usuario

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
print("Tabelas criadas com sucesso!")
