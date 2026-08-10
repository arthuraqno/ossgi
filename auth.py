from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = "uma-chave-secreta-bem-dificil-de-advinhar-by-arthuraqno"
ALGORITHM = "HS256"
TEMPO_EXPIRACAO_MINUTOS = 60


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha_digitada: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha_digitada, senha_hash)

def criar_token(dados: dict):
    dados_copia = dados.copy()
    expira_em = datetime.utcnow() + timedelta(minutes=TEMPO_EXPIRACAO_MINUTOS)
    dados_copia.update({"exp": expira_em})
    token = jwt.encode(dados_copia, SECRET_KEY, algorithm=ALGORITHM)
    return token   

def validar_token(token: str):
    try: 
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
