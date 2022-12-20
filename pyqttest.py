from PyQt6.QtWidgets import QWidget, QApplication
import sys

#Eine Instanz von der Klasse QApplication erzeugen
app = QApplication(sys.argv)

#Fensterelement erzeugen und konfigurieren
window = QWidget()
window.setWindowTitle("Meine erste PyQt App!")
window.setGeometry(200, 200, 600, 300)


window.show()
sys.exit(app.exec())