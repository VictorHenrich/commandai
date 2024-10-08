# COMMANDAI
**CommandAI** é um sistema de gerenciamento de operações por meio de comandos de voz, que utiliza Inteligência Artificial para oferecer um controle eficiente e automatizado. Esta ferramenta visa simplificar a interação com sistemas operacionais, permitindo uma experiência mais intuitiva e dinâmica.


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
Para executar o programa, é necessário que todos os passos anteriores, como a instalação do Python e a preparação dos pacotes, tenham sido concluídos. Se preferir, nos próximos tópicos, será demonstrada uma maneira mais simples e direta de realizar a execução utilizando os scripts inicializadores chamados **start_project**.

### Windows

   **Execução do programa:**
   - Abra o Prompt de Comando (`cmd`).
   - Digite o seguinte comando:
     ```bash
     python main.py
     ```
   - O programa deve se inicializar ao rodar.


### Linux

   **Execução do programa:**
   - Abra um terminal e execute:
     ```bash
     python3 main.py
     ```
   - O programa deve se inicializar ao rodar.

## Utilizando arquivo *start_project*
Este arquivo é responsável por verificar e criar um ambiente virtual do Python, além de instalar os pacotes necessários para a execução do projeto. Isso simplifica o processo de configuração e inicialização do projeto como um todo.


### Windows

   **Inicializando projeto:**
   - Abra o Prompt de Comando (`cmd`), navegue até o diretório do seu projeto e execute.
     ```bash
        start_project.cmd
     ```

### Linux

   **Inicializando projeto:**
   - No terminal, navegue até o diretório do seu projeto e execute:
     ```bash
     source start_project.sh
     ```

# Executando testes do projeto
Este tutorial apresenta o procedimento para realizar os testes unitários da aplicação, utilizando a biblioteca *unittest*, nativa do Python. Para que os testes funcionem corretamente, é necessário que seu ambiente esteja devidamente configurado e pronto para a execução.

## Forma Manual
Para executar os testes do programa, é essencial que todos os passos anteriores, como a instalação do Python e a configuração dos pacotes, tenham sido concluídos. Nos próximos tópicos, você encontrará uma maneira mais simples e direta de rodar os testes, utilizando os scripts inicializadores chamados **start_tests**.

   **Executar todos os testes na pasta tests:**
   - No terminal, navegue até o diretório do seu projeto e execute:
     ```bash
     python -m unittest discover -s tests
     ```

   **Executar um teste específico:**
   - No terminal, navegue até o diretório do seu projeto e execute:
     ```bash
     python -m unittest discover -s tests
     ```

   **Executar testes com mais detalhes sobre falhas:**
   - No terminal, navegue até o diretório do seu projeto e execute:
     ```bash
     python -m unittest discover -s tests -v`
     ```
   - A opção -v (verbose) irá mostrar mais detalhes sobre os testes aplicados

  
## Utilizando o arquivo *start_tests*
Este arquivo verifica e cria o ambiente virtual do Python, além de instalar os pacotes necessários para a execução dos testes do projeto. Ele simplifica o processo de configuração e execução dos testes, tornando-o mais eficiente.

### Windows

   **Testando projeto:**
   - Abra o Prompt de Comando (`cmd`), navegue até o diretório do seu projeto e execute.
     ```bash
      start_tests.cmd
     ```

### Linux

   **Testando projeto:**
   - No terminal, navegue até o diretório do seu projeto e execute:
     ```bash
     source start_tests.sh
     ```