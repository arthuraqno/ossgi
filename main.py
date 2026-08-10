from fastapi import FastAPI
from routes.aluno import router as aluno_router
from routes.professor import router as professor_router
from routes.turma import router as turma_router
from routes.turma_horario import router as turma_horario_router
from routes.usuario import router as usuario_router


app = FastAPI()
app.include_router(aluno_router)
app.include_router(professor_router)
app.include_router(turma_router)
app.include_router(turma_horario_router)
app.include_router(usuario_router)



@app.get("/")
def home():
    return {"mensagem": "API OssGi funcionando!"}
