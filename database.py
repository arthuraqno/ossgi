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
senha = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql://postgres:{senha}@localhost:5432/ossgi_db"
)

Base.metadata.create_all(engine)
print("Tabelas criadas com sucesso!")