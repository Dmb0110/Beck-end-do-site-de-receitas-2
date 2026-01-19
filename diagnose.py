#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

print("=" * 60)
print("🔍 DIAGNÓSTICO DA API RECEITAS MASTERCHEF")
print("=" * 60)
print()

# 1. Verificar arquivo .env
print("📋 1. Verificando arquivo .env...")
env_path = Path(".env")
if not env_path.exists():
    print("   ❌ Arquivo .env não encontrado!")
    print("   ✏️  Crie um arquivo .env na raiz do projeto com:")
    print()
    print("   DATABASE_URL=sua_url_postgresql_aqui")
    print("   SECRET_KEY=sua_chave_secreta_aqui")
    print()
    sys.exit(1)
else:
    print("   ✅ Arquivo .env encontrado")

# 2. Verificar variáveis de ambiente
print()
print("🔐 2. Verificando variáveis de ambiente...")
from dotenv import load_dotenv
load_dotenv()

database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')

if not database_url:
    print("   ❌ DATABASE_URL não configurada no .env")
    sys.exit(1)
else:
    # Mascarar a URL por segurança
    masked_url = database_url[:30] + "...***" if len(database_url) > 30 else database_url
    print(f"   ✅ DATABASE_URL: {masked_url}")

if not secret_key or secret_key == "sua_chave_secreta_deve_estar_em_env":
    print("   ❌ SECRET_KEY não configurada ou é o valor padrão")
    sys.exit(1)
else:
    print(f"   ✅ SECRET_KEY configurada")

# 3. Verificar dependências
print()
print("📦 3. Verificando dependências...")
required_packages = ['fastapi', 'uvicorn', 'sqlalchemy', 'psycopg2', 'python-dotenv', 'passlib', 'python-jose']
missing = []

for package in required_packages:
    try:
        __import__(package.replace('-', '_'))
        print(f"   ✅ {package}")
    except ImportError:
        print(f"   ❌ {package} NÃO INSTALADO")
        missing.append(package)

if missing:
    print()
    print(f"   Instale os pacotes faltantes com:")
    print(f"   pip install {' '.join(missing)}")
    sys.exit(1)

# 4. Verificar conexão com banco de dados
print()
print("🗄️  4. Testando conexão com banco de dados...")
try:
    from sqlalchemy import create_engine, text
    from sqlalchemy.pool import StaticPool
    
    engine = create_engine(database_url, poolclass=StaticPool)
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("   ✅ Conexão com banco de dados OK")
except Exception as e:
    print(f"   ❌ Erro ao conectar ao banco:")
    print(f"   {str(e)}")
    print()
    print("   Verifique:")
    print("   - Se a URL do banco está correta no .env")
    print("   - Se o banco de dados está online")
    print("   - Se as credenciais estão corretas")
    sys.exit(1)

# 5. Verificar estrutura de arquivos
print()
print("📁 5. Verificando estrutura de arquivos...")
required_files = [
    'app/main.py',
    'app/router.py',
    'app/core/config.py',
    'app/database/session.py',
    'app/models/models_usuario.py',
    'app/models/models_receita.py',
]

all_ok = True
for file in required_files:
    if Path(file).exists():
        print(f"   ✅ {file}")
    else:
        print(f"   ❌ {file} NÃO ENCONTRADO")
        all_ok = False

if not all_ok:
    print()
    print("   Erro: Alguns arquivos essenciais estão faltando!")
    sys.exit(1)

# 6. Resumo
print()
print("=" * 60)
print("✅ TUDO OK! A API está pronta para rodar!")
print("=" * 60)
print()
print("Para iniciar o servidor, execute:")
print()
print("   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")
print()
print("Ou use o script:")
print()
print("   python run_server.py")
print()
