from fastapi import FastAPI
from app.database.session import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from app.router import api_router

app = FastAPI(
    title='Receitas Masterchef API',
    description='API para gerenciamento de usuários e receitas',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redoc',
    openapi_url='/openapi.json'
)

origins = [
    "https://front-do-site-de-receitas-2.vercel.app",
    "https://front-do-site-de-receitas-2.vercel.app/"
]

# Middleware para permitir requisições do frontend hospedado na Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Substitua pela URL real do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Rotas principais da API
app.include_router(api_router)

