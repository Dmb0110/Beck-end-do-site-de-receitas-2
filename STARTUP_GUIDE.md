# 🎯 RESUMO - Por que localhost:8000 não responde

## 🔴 Problema Principal
A API **não está rodando** porque:
1. O servidor uvicorn não foi iniciado
2. Falta o arquivo `.env` com configurações
3. Banco de dados não está acessível

---

## ✅ Solução Rápida (3 passos)

### Passo 1: Diagnosticar
```bash
python diagnose.py
```

### Passo 2: Corrigir erros (se houver)
- Verifique o arquivo `.env`
- Confirme que `DATABASE_URL` está correto
- Confirme que `SECRET_KEY` está preenchido

### Passo 3: Iniciar servidor
```bash
python run_server.py
```

✅ Pronto! Acesse: http://localhost:8000

---

## 📋 Verificação de Pré-requisitos

- [ ] Arquivo `.env` existe e tem `DATABASE_URL`
- [ ] Arquivo `.env` tem `SECRET_KEY`
- [ ] Python está instalado (`python --version`)
- [ ] Dependências estão instaladas (`pip install -r requirements.txt`)
- [ ] Banco de dados está online e acessível
- [ ] Nenhum outro processo usa porta 8000

---

## 🚀 Comandos Úteis

| Comando | Descrição |
|---------|-----------|
| `python diagnose.py` | Diagnosticar problemas |
| `python run_server.py` | Iniciar servidor (recomendado) |
| `run_server.bat` | Iniciar servidor (Windows) |
| `uvicorn app.main:app --reload --port 8000` | Iniciar manualmente |
| `pip install -r requirements.txt` | Instalar dependências |

---

## 📡 URLs Importantes

Quando o servidor estiver rodando:

| URL | Descrição |
|-----|-----------|
| http://localhost:8000 | API raiz |
| http://localhost:8000/docs | Documentação interativa (Swagger) |
| http://localhost:8000/redoc | Documentação (ReDoc) |
| http://localhost:8000/receita/health | Health check |
| http://localhost:8000/receita/receber | Lista de receitas |

---

## 🔗 Arquivo .env (Exemplo)

```env
DATABASE_URL=postgresql://neondb_owner:npg_HDj9psUF4Scv@ep-red-meadow-acf8hr0w-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require

SECRET_KEY=minha_chave_super_secreta_que_so_eu_sei_qual_e

ENVIRONMENT=development
```

---

## 📁 Arquivos Criados para Ajudar

✅ `diagnose.py` - Verifica tudo automaticamente  
✅ `run_server.py` - Iniciar servidor com diagnóstico  
✅ `run_server.bat` - Script Windows  
✅ `TROUBLESHOOTING.md` - Guia completo de erros  

---

## ❓ Dúvidas Comuns

**P: A porta 8000 está em uso por outro processo?**  
R: Execute `netstat -ano | findstr ":8000"` para verificar

**P: Como usar outra porta?**  
R: `uvicorn app.main:app --port 8001`

**P: O banco de dados está offline?**  
R: Verifique a URL em `DATABASE_URL` no `.env`

---

Comece executando: **`python diagnose.py`** ✨
