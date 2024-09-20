@echo off

set ENV_DIR=env

where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Python nao esta instalado. Instale o Python 3 antes de continuar.
    exit /b 1
)

if exist %ENV_DIR% (
    echo Ambiente virtual encontrado, ativando...
    call %ENV_DIR%\Scripts\activate
) else (
    echo Ambiente virtual nao encontrado, criando um novo...
    python -m venv %ENV_DIR%
    call %ENV_DIR%\Scripts\activate
)

if exist requirements.txt (
    echo Instalando pacotes do requirements.txt...
    pip install -r requirements.txt
) else (
    echo Arquivo requirements.txt nao encontrado.
)

echo Ambiente pronto!
echo ...Inicializando projeto...
python main.py