ENV_DIR="venv-lin"

if ! command -v python3 &> /dev/null; then
    echo "Python não está instalado. Instale o Python 3 antes de continuar."
    exit 1
fi

if [ -d "$ENV_DIR" ]; then
    echo "Ambiente virtual encontrado, ativando..."
    source "$ENV_DIR/bin/activate"
else
    echo "Ambiente virtual não encontrado, criando um novo..."
    python3 -m venv "$ENV_DIR"
    source "$ENV_DIR/bin/activate"
fi

if [ -f "requirements.txt" ]; then
    echo "Instalando pacotes do requirements.txt..."
    pip install -r requirements.txt
else
    echo "Arquivo requirements.txt não encontrado."
fi

echo "Ambiente pronto!"