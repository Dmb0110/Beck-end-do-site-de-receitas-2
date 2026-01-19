@echo off
echo ============================================
echo 🔍 VERIFICANDO STATUS DA API
echo ============================================
echo.

REM Verificar se a API consegue carregar
echo Testando se a aplicação FastAPI carrega...
python -c "from app.main import app; print('✅ FastAPI carregou com sucesso')" 2>&1

if %errorlevel% neq 0 (
    echo ❌ Erro ao carregar FastAPI
    echo.
    pause
    exit /b 1
)

echo.
echo Agora iniciando servidor...
echo.
echo ============================================
echo 🚀 SERVIDOR INICIANDO NA PORTA 8000
echo ============================================
echo.
echo Acesse: http://localhost:8000
echo Documentação: http://localhost:8000/docs
echo.
echo Pressione CTRL+C para parar
echo ============================================
echo.

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause
