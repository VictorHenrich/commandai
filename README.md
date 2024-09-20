# commandai
Sistema de gerenciamento de Sistema Operacional por comandos de voz, utilizando Inteligência Artificial para controle eficiente e automatizado.


# Instalação do Python

## Windows

1. **Baixar o Instalador:**
   - Acesse a [página de downloads do Python](https://www.python.org/downloads/).
   - Clique no botão para baixar a versão mais recente do Python.

2. **Executar o Instalador:**
   - Localize o arquivo baixado e clique duas vezes para executá-lo.
   - **Importante:** Marque a opção "Add Python to PATH" antes de clicar em "Install Now".

3. **Verificar a Instalação:**
   - Abra o Prompt de Comando (`cmd`).
   - Digite o seguinte comando:
     ```bash
     python --version
     ```
   - Você deve ver a versão do Python instalada.

## Linux

1. **Atualizar o Sistema:**
   - Abra um terminal e execute:
     ```bash
     sudo apt update
     sudo apt upgrade
     ```

2. **Instalar o Python:**
   - Para instalar a versão mais recente do Python, use:
     ```bash
     sudo apt install python3
     ```

3. **Verificar a Instalação:**
   - No terminal, execute:
     ```bash
     python3 --version
     ```
   - A versão do Python instalada deve ser exibida.

## Configuração do Ambiente Virtual

Após a instalação do Python, é recomendável criar um ambiente virtual para isolar suas dependências:

1. **Criar um Ambiente Virtual:**
   - No terminal, navegue até o diretório do seu projeto e execute:
     ```bash
     python3 -m venv nome_do_ambiente
     ```

2. **Ativar o Ambiente Virtual:**
   - No Linux:
     ```bash
     source nome_do_ambiente/bin/activate
     ```
   - No Windows:
     ```bash
     nome_do_ambiente\Scripts\activate
     ```

3. **Instalar Dependências:**
   - Com o ambiente virtual ativado, você pode instalar pacotes com:
     ```bash
     pip install nome_do_pacote
     ```

# Executando o projeto

## Forma manual
Para executar o programa, é necessário que todos os passos anteriores, como a instalação do Python e a preparação dos pacotes, tenham sido concluídos. Se preferir, nos próximos tópicos, será demonstrada uma maneira mais simples e direta de realizar a execução utilizando os scripts inicializadores chamados *start_project*.

### Windows

1. **Execução do programa:**
   - Abra o Prompt de Comando (`cmd`).
   - Digite o seguinte comando:
     ```bash
     python main.py
     ```
   - O programa deve se inicializar ao rodar.


### Linux

1. **Execução do programa:**
   - Abra um terminal e execute:
     ```bash
     python3 main.py
     ```
   - O programa deve se inicializar ao rodar.

## Utilizando arquivo start_project
Este arquivo é responsável por verificar / criar um ambiente virtual do python e realizar as devidas instalações dos pacotes necessários para execução do projeto. Isso irá facilitar o processo de criação e inicialização do projeto como um todo.


### Windows

- Abra o Prompt de Comando (`cmd`), navegue até o diretório do seu projeto e execute.
     ```bash
        start_project.cmd
     ```

### Linux

1. **Inicializando projeto:**
   - No terminal, navegue até o diretório do seu projeto e execute:
     ```bash
     source start_project.sh
     ```

# Executando testes do projeto

Este tutorial irá mostrar como realizar os testes unitários da aplicação. Para este projeto, foi utilizado a biblioteca unittest nativa do python. Para os testes funcionarem, você precisará estar com seu ambiente preparado e pronto para execução.

## Para executar todos os testes na pasta tests, utilize o seguinte comando:
```python -m unittest discover -s tests```

## Para executar um teste específico, você pode usar:
```python -m unittest tests.test_exemplo```

## Se você precisar de mais detalhes sobre falhas, pode executar os testes com a opção -v (verbose):
```python -m unittest discover -s tests -v```