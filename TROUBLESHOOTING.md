# 🔧 TROUBLESHOOTING - Porta 8000 não responde

## ✅ Soluções Rápidas

### 1️⃣ Iniciar a API

**Opção A - Script Python (Recomendado)**
```bash
python run_server.py
```

**Opção B - Script Batch (Windows)**
```bash
run_server.bat
```

**Opção C - Direto com uvicorn**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🔍 Diagnosticar Problemas

Execute o script de diagnóstico:
```bash
python diagnose.py
```

Isso verificará:
- ✅ Arquivo `.env` existe
- ✅ `DATABASE_URL` está configurada
- ✅ `SECRET_KEY` está configurada
- ✅ Todas as dependências instaladas
- ✅ Conexão com banco de dados
- ✅ Estrutura de arquivos

---

## ❌ Erros Comuns

### Erro: "DATABASE_URL não está configurada"
**Solução:**
1. Abra o arquivo `.env`
2. Adicione/corrija:
```env
DATABASE_URL=postgresql://usuario:senha@host:5432/database
SECRET_KEY=sua_chave_super_secreta
```

### Erro: "Connection refused"
**Possíveis causas:**
1. Banco de dados offline
   - Teste a URL do banco em um navegador
   - Verifique se o servidor PostgreSQL está rodando

2. Dependências não instaladas
```bash
pip install -r requirements.txt
```

3. Porta 8000 em uso
```bash
# Verificar qual processo está usando a porta
netstat -ano | findstr ":8000"

# Liberar a porta (Windows)
taskkill /PID [PID] /F

# Ou usar outra porta
uvicorn app.main:app --port 8001
```

### Erro: "ModuleNotFoundError"
**Solução:**
```bash
pip install -r requirements.txt
```

### Erro: "psycopg2 - ImportError"
**Solução:**
```bash
pip install psycopg2-binary
```

---

## 📝 Verificação Manual

### 1. Verificar se Python está instalado
```bash
python --version
```

### 2. Verificar se uvicorn está instalado
```bash
uvicorn --version
```

### 3. Testar a conexão com o banco
```python
python
>>> from sqlalchemy import create_engine, text
>>> engine = create_engine("postgresql://usuario:senha@host/db")
>>> with engine.connect() as conn:
...     print(conn.execute(text("SELECT 1")))
```

### 4. Verificar se a API sobe
```bash
python -c "from app.main import app; print('✅ API carregada com sucesso')"
```

---

## 🌐 Acessar a API

Quando tudo estiver funcionando:

- **API:** http://localhost:8000
- **Documentação (Swagger):** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **Healthcheck:** http://localhost:8000/receita/health

---

## 📂 Estrutura Esperada

```
BACK 2 DO SITE DE RECEITAS/
├── .env                          # ✅ DEVE existir
├── requirements.txt              # ✅ dependências
├── diagnose.py                   # Script de diagnóstico
├── run_server.py                 # Script para rodar
├── run_server.bat                # Script Windows
├── app/
│   ├── main.py                   # ✅ DEVE existir
│   ├── router.py                 # ✅ DEVE existir
│   ├── core/config.py            # ✅ DEVE existir
│   ├── database/session.py        # ✅ DEVE existir
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── crud_services/
│   └── autenticacao10/
└── alembic/                      # Migrações (opcional)
```

---

## 🚨 Se nada funcionar

1. **Verificar logs completos:**
```bash
python run_server.py 2>&1 | tee logs.txt
```

2. **Coletar informações:**
   - Output completo do erro
   - Versão do Python: `python --version`
   - Versão do pip: `pip --version`
   - Sistema operacional
   - Resultado de `python diagnose.py`

3. **Verificar se o .env tem valores corretos:**
   - `DATABASE_URL` acessível?
   - `SECRET_KEY` tem conteúdo?

---

## ✨ Dicas Importantes

⚠️ **Para PRODUÇÃO:**
- Remova `--reload` do comando
- Remova localhost do CORS em `app/main.py`
- Defina `ENVIRONMENT=production` no `.env`
- Use um reverse proxy (Nginx)

📌 **Para DESENVOLVIMENTO:**
- Use `run_server.py` que inclui hot-reload
- Verifique logs em tempo real
- Use `http://localhost:3000` ou `8000` conforme necessário
