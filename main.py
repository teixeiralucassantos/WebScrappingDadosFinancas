# main.py

from controllers import MainController
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MainController()  # Inicializa o controlador
    controller.run()                # Executa a interface
    sys.exit(app.exec_())
