# Web Scraper

## Descrição

Este projeto é um web scraper desenvolvido em Python, que extrai dados de mercados financeiros do site Yahoo Finance. Os dados extraídos são organizados e salvos em um arquivo Excel. O projeto utiliza uma interface gráfica simples, construída com PyQt5, permitindo que os usuários interajam com o scraper de forma intuitiva.

## Funcionalidades

- **Extração de Dados**: O scraper é capaz de coletar dados de diferentes tabelas no site Yahoo Finance, incluindo índices de mercado, commodities, e setores.
- **Consolidação de Dados**: Os dados extraídos são organizados em um único arquivo Excel, com diferentes planilhas para cada tipo de dado.
- **Interface Gráfica**: A aplicação apresenta uma interface gráfica simples, que permite ao usuário iniciar o scraping com um clique de botão.
- **Mensagens de Status**: O aplicativo exibe mensagens informativas para o usuário, indicando o status da execução do scraper.

## Estrutura do Projeto

web_scraper/
│
├── models/
│   ├── __init__.py
│   ├── scraper.py          # Lógica de scraping e manipulação de dados
│   └── data_handler.py     # Lógica para manipular dados e salvar em Excel
│
├── views/
│   ├── __init__.py
│   ├── console_view.py     # Interface de linha de comando (ou pode ser uma interface gráfica)
│   └── report_view.py      # Visualização de relatórios ou dados (opcional)
│
├── controllers/
│   ├── __init__.py
│   └── main_controller.py   # Controlador principal que orquestra o fluxo do aplicativo
│
├── requirements.txt         # Dependências do projeto
├── main.py


### Modelos

- **scraper.py**: Contém a lógica para fazer requisições HTTP ao Yahoo Finance, extrair tabelas usando XPath e converter os dados em DataFrames do Pandas.
- **data_handler.py**: Gerencia a consolidação dos DataFrames extraídos e a criação de um arquivo Excel com as informações coletadas.

### Visualizações

- **console_view.py**: Implementa a interface gráfica com PyQt5, permitindo ao usuário interagir com o scraper. Inclui botões, mensagens e design responsivo.

### Controladores

- **main_controller.py**: Coordena o fluxo de dados entre o scraper e o manipulador de dados, além de iniciar a interface gráfica.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do scraper.
- **Requests**: Biblioteca para fazer requisições HTTP.
- **lxml**: Biblioteca para análise e extração de dados HTML.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **PyQt5**: Framework para construção de interfaces gráficas.

## Conceitos Utilizados

- **Web Scraping**: Técnica utilizada para extrair dados de sites da web.
- **DataFrame**: Estrutura de dados do Pandas utilizada para armazenar dados tabulares.
- **XPath**: Linguagem usada para navegar e extrair informações de documentos XML e HTML.
- **Interface Gráfica**: Desenvolvimento de uma interface amigável para interação com o usuário.


