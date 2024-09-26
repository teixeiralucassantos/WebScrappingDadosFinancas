# views/console_view.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox, QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon, QPixmap, QColor, QFont
from PyQt5.QtCore import Qt

from models import Scraper, DataHandler  # Importa as classes Scraper e DataHandler

class CustomWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Scrapping")
        self.setGeometry(100, 100, 800, 600)

        self.upper_section = QLabel(self)
        self.upper_section.setGeometry(0, 0, int(self.width() * 0.66), self.height())
        self.upper_section.setStyleSheet("background-color: white")

        self.lower_section = QLabel(self)
        self.lower_section.setGeometry(int(self.width() * 0.66), 0, int(self.width() * 0.34), self.height())
        self.lower_section.setStyleSheet("background-color: darkblue")
        self.add_shadow_effect(self.lower_section)

        self.csn_logo = QLabel(self)
        csn_pixmap = QPixmap("c.png")
        self.csn_logo.setPixmap(csn_pixmap)
        self.csn_logo.setGeometry(5, 8, csn_pixmap.width(), csn_pixmap.height())

        self.setor_image = QLabel(self)
        setor_pixmap = QPixmap("c.png")
        self.setor_image.setPixmap(setor_pixmap)
        self.setor_image.setGeometry(self.width() - setor_pixmap.width() - 8, 3, setor_pixmap.width(), setor_pixmap.height())

        self.play_button = QPushButton("PLAY!", self)
        self.play_button.setGeometry(int(self.width() * 0.35), int(self.height() * 0.4), int(self.width() * 0.3), int(self.height() * 0.15))
        self.add_shadow_effect(self.play_button)
        self.play_button.setStyleSheet("background-color: darkblue; color: white")
        play_icon = QIcon("play.png")
        self.play_button.setIcon(play_icon)
        icon_size = self.play_button.iconSize()
        icon_size.setWidth(icon_size.width() + 40)
        icon_size.setHeight(icon_size.height() + 40)
        self.play_button.setIconSize(icon_size)
        self.play_button.clicked.connect(self.start_program)

        self.gerencia_text = QLabel("® Lucas Santos Teixeira", self)
        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.gerencia_text.setFont(font)
        self.gerencia_text.setStyleSheet("color: white;")
        self.gerencia_text.setAlignment(Qt.AlignCenter)
        self.gerencia_text.setGeometry(
            int(self.width() * 0.66), 
            int(self.height() * 0.85),
            int(self.width() * 0.34), 
            int(self.height() * 0.1)
        )

        self.width_ratio = self.width() / self.height()
        self.height_ratio = self.height() / self.width()
        self.resizeEvent = self.handle_resize

    def handle_resize(self, event):
        new_width = event.size().width()
        new_height = event.size().height()

        self.upper_section.setGeometry(0, 0, new_width, int(new_height * 0.66))
        self.lower_section.setGeometry(0, int(new_height * 0.66), new_width, int(new_height * 0.34))
        self.csn_logo.setGeometry(5, 8, self.csn_logo.width(), self.csn_logo.height())
        self.setor_image.setGeometry(new_width - self.setor_image.width() - 8, 3, self.setor_image.width(), self.setor_image.height())
        self.play_button.setGeometry(int(new_width * 0.35), int(new_height * 0.4), int(new_width * 0.3), int(new_height * 0.15))
        self.gerencia_text.setGeometry(
            int(new_width * 0.66), 
            int(new_height * 0.85), 
            int(new_width * 0.34), 
            int(new_height * 0.1)
        )

    def add_shadow_effect(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0, 0, 0, 150))
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 10)
        widget.setGraphicsEffect(shadow)

    def start_program(self):
        popup = QMessageBox(self)
        popup.setIcon(QMessageBox.Information)
        popup.setWindowTitle("Aviso")
        popup.setText("O programa está sendo executado. Aguarde.")
        popup.show()
        QApplication.processEvents()

        try:
            # Escreva o código aqui 
            url = "https://finance.yahoo.com/markets/"
            scraper = Scraper(url)
            tables_data = scraper.extract_tables()  # Faz a chamada ao Scraper

            data_handler = DataHandler(tables_data)  # Passa os dados para o DataHandler
            data_handler.consolidate_data()  # Consolida os dados e cria o arquivo Excel
            
            popup.setIcon(QMessageBox.Information)
            popup.setText("O programa foi executado com sucesso.")
            popup.exec_()
        except Exception as e:
            popup.setIcon(QMessageBox.Critical)
            popup.setText(f"Erro ao executar o programa: {e}")
            popup.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomWindow()
    window.show()
    sys.exit(app.exec_())
