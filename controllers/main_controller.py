# controllers/main_controller.py

from models.scraper import Scraper
from models.data_handler import DataHandler
from views import CustomWindow

class MainController:
    def __init__(self):
        self.url = "https://finance.yahoo.com/markets/"
        self.scraper = Scraper(self.url)
        self.data_handler = None

    def start_scraping(self):
        try:
            tables_data = self.scraper.extract_tables()
            self.data_handler = DataHandler(tables_data)
            self.data_handler.consolidate_data()
            print("Dados extraídos e salvos com sucesso.")
        except Exception as e:
            print(f"Erro ao executar o scraping: {e}")

    def run(self):
        app = CustomWindow()
        app.show()

if __name__ == "__main__":
    controller = MainController()
    controller.start_scraping()  # Inicia o scraping antes de abrir a interface
    controller.run()
