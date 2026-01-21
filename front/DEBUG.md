# 🧪 Troubleshooting Frontend - index.html não carrega receitas

## 🔍 Como Debugar

### Passo 1: Abrir o Teste de Conexão
1. Abra o arquivo: **`front7/teste.html`** no navegador
2. Clique em **"Testar Conexão"**
3. Veja se a API responde

---

## ✅ Se a API responde:

### Passo 2: Verificar se há receitas no banco
1. No arquivo `teste.html`, clique em **"Listar Receitas"**
2. Você deve ver receitas cadastradas
3. Se não houver, crie algumas receitas primeiro (login + criar receita)

---

## ❌ Se a API NÃO responde:

### 1. Verifique se o servidor está rodando
```bash
uvicorn app.main:app --reload --port 8000
```

Deve aparecer:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### 2. Verifique a porta
```bash
netstat -ano | findstr ":8000"
```

Se houver resultado, a porta está em uso.

### 3. Teste a API diretamente
Abra no navegador: **http://localhost:8000/docs**

Você deve ver a documentação do Swagger.

---

## 🔗 URLs do Frontend

- **Home:** `http://localhost:8000/` → Abra `front7/index.html`
- **Teste:** `http://localhost:8000/` → Abra `front7/teste.html`
- **Receita:** `http://localhost:8000/` → Abra `front7/receita.html`

---

## 📊 Verificação de API Endpoints

Teste cada endpoint no arquivo `teste.html`:

| Endpoint | Esperado |
|----------|----------|
| GET `/receita/health` | `{"Status": "Ola desenvolvedor, tudo ok por aqui"}` |
| GET `/receita/receber` | `[{...receita1}, {...receita2}]` |
| GET `/receita/especifico/{id}` | `{id, nome_da_receita, ingredientes, modo_de_preparo, foto}` |

---

## 🐛 Erros Comuns

### "Failed to fetch"
- [ ] Servidor não está rodando
- [ ] Banco de dados offline
- [ ] Firewall bloqueando porta 8000
- [ ] CORS desabilitado

**Solução:**
```bash
uvicorn app.main:app --reload --port 8000
```

### "Network error"
- [ ] Sem conexão com internet
- [ ] DNS não consegue resolver localhost

**Solução:**
```bash
ping localhost
```

Deve responder com um IP.

### "CORS error" no console
Significa que o frontend conseguiu alcançar a API, mas a API rejeitou a requisição.

Verifique em `app/main.py` se `localhost:3000` e `localhost:8000` estão em `origins`.

---

## 🔧 Verificações no Console (F12)

Abra o arquivo `index.html` e pressione **F12** para abrir o DevTools.

Você deve ver logs como:
```
🚀 Página carregada
🔄 Carregando receitas de: http://localhost:8000/receita/receber
📊 Response status: 200
✅ Receitas carregadas: Array(5)
```

Se houver erros, copie e compartilhe a mensagem de erro exata.

---

## 📋 Checklist de Debug

- [ ] `uvicorn app.main:app --reload` está rodando sem erros
- [ ] http://localhost:8000/docs abre e mostra documentação
- [ ] `front7/teste.html` consegue "Testar Conexão"
- [ ] `front7/teste.html` consegue "Listar Receitas"
- [ ] Há receitas no banco de dados
- [ ] `index.html` consegue carregar a página (mesmo sem receitas)
- [ ] Console (F12) não mostra erros CORS

---

## 🚀 Próximos Passos

1. Use o `teste.html` para identificar qual endpoint está falhando
2. Se todos os testes passarem, o `index.html` funcionará
3. Se algum teste falhar, compartilhe a mensagem de erro

**Comece aqui:** `front7/teste.html` 🎯
