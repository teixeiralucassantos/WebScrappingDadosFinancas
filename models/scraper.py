# models/scraper.py

import requests
import pandas as pd
from lxml import html

class Scraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        # Faz uma requisição GET para o site
        response = requests.get(self.url)
        response.raise_for_status()  # Lança um erro se a requisição falhar
        return html.fromstring(response.content)

    def extract_tables(self):
        tree = self.fetch_data()
        
        # Dicionário para armazenar os DataFrames
        data = {
            "indiceamerica": self.extract_table(tree, '/html/body/div[2]/main/section/section/section/article/section[1]/div/div/div/section[1]/div/div/table'),
            "europaindice": self.extract_table(tree, '/html/body/div[2]/main/section/section/section/article/section[1]/div/div/div/section[2]/div'),
            "asiaindice": self.extract_table(tree, '/html/body/div[2]/main/section/section/section/article/section[1]/div/div/div/section[3]/div'),
            "commodities": self.extract_table(tree, '/html/body/div[2]/main/section/section/section/article/section[2]/div/div/div/section[1]/div'),
            "tesouro": self.extract_table(tree, '/html/body/div[2]/main/section/section/section/article/section[2]/div/div/div/section[3]/div'),
            "setor": self.extract_table(tree, '/html/body/div[2]/main/section/section/section/article/section[3]/section/div/div/div[1]/div/div[2]'),
            "topnegociacao": self.extract_table(tree, '/html/body/div[2]/main/section/section/section/article/section[4]/div[2]/div')
        }
        print(data)
        # Convertendo os elementos extraídos em DataFrames com nomes apropriados
        for key, value in data.items():
            data[key] = self.convert_to_dataframe(value)
            data[key].name = key  # Nomeando o DataFrame com a chave correspondente

        return data

    def extract_table(self, tree, xpath):
        # Extrai a tabela com base no XPath fornecido
        table_element = tree.xpath(xpath)
        return table_element[0] if table_element else None

    def convert_to_dataframe(self, table_element):
        # Converte o elemento da tabela em um DataFrame
        if table_element is not None:
            rows = table_element.xpath('.//tr')  # Obtém todas as linhas da tabela
            data = []

            for row in rows:
                cols = row.xpath('.//td/text()')  # Obtém todos os dados das colunas
                data.append([col.strip() for col in cols])  # Adiciona os dados ao DataFrame

            return pd.DataFrame(data)  # Retorna um DataFrame
        return pd.DataFrame()  # Retorna um DataFrame vazio se não houver tabela

# Exemplo de uso
if __name__ == "__main__":
    url = "https://finance.yahoo.com/markets/"
    scraper = Scraper(url)
    tables_data = scraper.extract_tables()
    
    for table_name, df in tables_data.items():
        print(f"\n{table_name}:")
        print(df.head())  # Exibe as primeiras linhas de cada DataFrame
