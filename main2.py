import sys
from ui import UI
from PyQt6.QtWidgets import QApplication

            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    interface = UI()
    interface.setup_ui()
    interface.show()
    sys.exit(app.exec())