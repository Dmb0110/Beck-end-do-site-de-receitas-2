@echo off
echo ============================================
echo Iniciando Receitas Masterchef API
echo ============================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python não está instalado ou não está no PATH
    pause
    exit /b 1
)

REM Verificar se estamos na pasta correta
if not exist "app\main.py" (
    echo [ERRO] Arquivo app\main.py não encontrado
    echo Certifique-se de estar na pasta raiz do projeto
    pause
    exit /b 1
)

REM Instalar/atualizar dependências
echo [1] Verificando dependências...
pip install -q -r requirements.txt

REM Iniciar o servidor
echo [2] Iniciando servidor uvicorn...
echo.
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause
