# 🥋 OssGi

API REST para gestão de academias de jiu-jitsu, desenvolvida em Python com FastAPI, PostgreSQL e autenticação JWT.

## 📋 Funcionalidades

- Cadastro e gestão de alunos, professores e turmas
- Controle de graduação (faixa e graus) de alunos e professores
- Gestão de horários de turmas (múltiplos dias por turma)
- Autenticação de usuários com JWT e senhas criptografadas (bcrypt)
- Documentação interativa automática (Swagger)

## 📁 Estrutura do Projeto

ossgi/
├── main.py
├── base.py
├── database.py
├── auth.py
├── models/
│ ├── aluno.py
│ ├── professor.py
│ ├── turma.py
│ ├── turma_horario.py
│ └── usuario.py
├── services/
│ ├── aluno.py
│ ├── professor.py
│ ├── turma.py
│ ├── turma_horario.py
│ └── usuario.py
└── routes/
├── aluno.py
├── professor.py
├── turma.py
├── turma_horario.py
└── usuario.py


## ▶️ Como rodar

1. Crie um banco de dados PostgreSQL chamado `ossgi_db`
2. Crie um arquivo `.env` na raiz do projeto com sua senha do banco:

DB_PASSWORD=sua_senha_aqui

3. Instale as dependências:

pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv passlib[bcrypt] python-jose[cryptography]

4. Crie as tabelas:

python database.py

5. Inicie a API:

uvicorn main:app --reload

6. Acesse a documentação interativa em `http://127.0.0.1:8000/docs`

## 🛠️ Tecnologias

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- JWT (autenticação)
- Passlib/Bcrypt (hash de senha)

## 📚 Conceitos aplicados

- API RESTful com rotas GET, POST e PUT
- Modelagem relacional com Foreign Keys e relacionamentos (Aluno → Turma → Professor)
- Validação de dados com Pydantic (schemas de entrada separados dos models do banco)
- Autenticação com JWT e hash de senha com bcrypt
- Variáveis de ambiente para proteger credenciais sensíveis
- Documentação automática via Swagger

## 🚧 Em desenvolvimento

- Proteção de rotas sensíveis com autenticação JWT
- Dockerização e deploy