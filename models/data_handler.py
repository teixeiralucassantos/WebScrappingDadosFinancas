# models/data_handler.py

import pandas as pd
from .scraper import Scraper  # Importa a classe Scraper do mesmo pacote
 # Importa a classe Scraper

class DataHandler:
    def __init__(self, data):
        self.data = data  # Recebe o dicionário de DataFrames do Scraper

    def consolidate_data(self):
        # Junta os DataFrames 'indiceamerica', 'europaindice', 'asiaindice' verticalmente
        indiceamerica = self.data["indiceamerica"]
        europaindice = self.data["europaindice"]
        asiaindice = self.data["asiaindice"]
        
        # Concatenando os DataFrames
        indice = pd.concat([indiceamerica, europaindice, asiaindice], ignore_index=True)

        # Cria um arquivo Excel com as planilhas desejadas
        with pd.ExcelWriter('consolidado.xlsx') as writer:
            indice.to_excel(writer, sheet_name='indice', index=False)
            indiceamerica.to_excel(writer, sheet_name='indiceamerica', index=False)
            europaindice.to_excel(writer, sheet_name='europaindice', index=False)
            asiaindice.to_excel(writer, sheet_name='asiaindice', index=False)
            self.data['commodities'].to_excel(writer, sheet_name='commodities', index=False)
            self.data['tesouro'].to_excel(writer, sheet_name='tesouro', index=False)
            self.data['setor'].to_excel(writer, sheet_name='setor', index=False)
            self.data['topnegociacao'].to_excel(writer, sheet_name='topnegociacao', index=False)

# Exemplo de uso
if __name__ == "__main__":
    url = "https://finance.yahoo.com/markets/"
    scraper = Scraper(url)
    tables_data = scraper.extract_tables()  # Obtém os DataFrames

    data_handler = DataHandler(tables_data)  # Passa o dicionário de DataFrames para o DataHandler
    data_handler.consolidate_data()  # Consolida os dados e cria o arquivo Excel
