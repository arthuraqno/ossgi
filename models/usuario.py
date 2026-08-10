from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)
    professor_id = Column(Integer, ForeignKey("professores.id"))