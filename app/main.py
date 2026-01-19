from fastapi import FastAPI
from app.database.session import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.router import api_router
import os

app = FastAPI(
    title='Receitas Masterchef API',
    description='API para gerenciamento de usuários e receitas',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redoc',
    openapi_url='/openapi.json'
)

# URLs permitidas para CORS
origins = [
    "https://front-do-site-de-receitas-2.vercel.app",
    "https://front-do-site-de-receitas-2.vercel.app/",
    "http://localhost:3000",  # Para desenvolvimento local
    "http://localhost:5500",  # Live Server do VS Code
    "http://localhost:8000",  # Para testes da API
    "http://localhost:8080",  # Porta alternativa de desenvolvimento
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8080",
]

# Middleware para permitir requisições do frontend hospedado na Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Apenas origens específicas permitidas
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

# Cria as tabelas no banco de dados (comentado para evitar erro se banco estiver offline)
# Base.metadata.create_all(bind=engine)
# Nota: Execute este comando manualmente quando o banco estiver disponível:
# python -c "from app.database.session import Base, engine; Base.metadata.create_all(bind=engine)"

# Rotas principais da API
app.include_router(api_router)

# Servir arquivos de uploads (fotos das receitas)
uploads_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "uploads")
if os.path.exists(uploads_path):
    app.mount("/uploads", StaticFiles(directory=uploads_path), name="uploads")

# Servir arquivos estáticos do frontend (deve ser o último mount)
front_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "front7")
if os.path.exists(front_path):
    app.mount("/", StaticFiles(directory=front_path, html=True), name="static")
