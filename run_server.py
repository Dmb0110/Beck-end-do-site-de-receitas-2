#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os

print("=" * 60)
print("🚀 INICIANDO RECEITAS MASTERCHEF API")
print("=" * 60)
print()

# 1. Rodar diagnóstico
print("Executando diagnóstico...")
result = subprocess.run([sys.executable, "diagnose.py"], capture_output=False)

if result.returncode != 0:
    print()
    print("❌ Diagnóstico falhou. Corrija os erros acima.")
    sys.exit(1)

# 2. Iniciar o servidor
print()
print("🎯 Iniciando servidor uvicorn...")
print()
print("A API estará disponível em: http://localhost:8000")
print("Documentação em: http://localhost:8000/docs")
print()
print("Pressione CTRL+C para parar o servidor")
print()

try:
    subprocess.run([
        sys.executable, "-m", "uvicorn",
        "app.main:app",
        "--reload",
        "--host", "0.0.0.0",
        "--port", "8000"
    ])
except KeyboardInterrupt:
    print()
    print("⏹️  Servidor parado.")
    sys.exit(0)
