# playwright_com_python_do_zero_automacao_profissional
Treinamento do curso da Udemy sobre uso de Playwright com Python e Pytest

## Criação do ambiente virtual

Quando um projeto é criado, as bibliotecas que funcionavam com ele podem não funcionar com novas versões. Por exemplo, se uma versão X do FastAPI funcionava apenas com Python 3.12 e agora há um Python 3.13, aquela biblioteca apresentará problemas no momento da execução. Para evitar estes problemas é necessário criar um ambiente virtual.

### Passo à passo da criação: 
1. Abrir o Terminal (CMD no windows) na pasta do diretório
* Estar dentro do diretório usando Explorador de arquivos;
* Clicar com botão direito do mouse;
* Selecionar "abrir no terminal".

2. Digitar o comando
**python -m venv [nome da venv]**
Obs.: normalmente é usado python -m venv venv

## Ativação do ambiente virtual
O comando do final da etapa anterior criará uma pasta com o nome da venv (ambiente vritual). Dentro dets apasta há uma série de outros arquivos e pastas, uma delas é a pasta de **Scripts**, onde há uma série de coemandos uteis para trabalhar com o ambiente virtual.

Aqui o interesse inicial é de ativar o ambiente virtual usando o arquivo **activate.bat**. O que deve ser feito:
1. Entrar na pasta de Script do venv;
2. Copiar o caminho até o activate.bat;
3. Colar todo o caminho até o arquivo no terminal para ativar o ambiente virtual. 

A partir de agora todos os comandos exceutados serão dentro da venv do Python:
- pip install pytest pytest-playwright (instala 2 libs: pytest e pytest-playwright);
- playwright install (instala todos os navegadores do playwright: Chrome, Firefox e Webkit);

## Testagem em terminal
No terminal, dentro do ambiente virtual, rodar o seguinte comando:<br>

**pytest --headed --browser=firefox test/ambience_google.py**<br>

Onde o browser pode ser qualquer um instalado, o diretório pode não ser "tests", e o nome do arquivo deve ser explicitado.

## Facilitando escrita de terminal -> arquivo pytest.ini

O pytest.ini nos permite colocar algumas instruções que diminuem a quantidade de flags e direções no terminal, usando de exemplo o
```
[pytest]
addopts = --headed
testpaths = tests
```
Isto remove a necessidade de escrever 'headed' toda vez, bem como a necessidade de dizer que os testes estão no diretório "tests". 

## Praticidade do requirements.txt

Este arquivo pode ser criado com 
```
pip freeze > requirements.txt
```

Ele automaticamente puxa as bibliotecas que o projeto está utilizando para rodar.
Outra pessoa em outra máquina pode baixar este requerimentos com 
```
pip install -r requirements.txt
```