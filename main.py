import sys
import sqlite3
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QThread, Signal
from ui_vrijeme import Ui_MainWindow

# ---------------------------------------
# Baza podataka - inicijalizacija
# ---------------------------------------
def init_db():
    """Kreira SQLite bazu i tablice ako ne postoje."""
    conn = sqlite3.connect("weather_app.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            date TEXT NOT NULL,
            temp REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# ---------------------------------------
# Worker thread za dohvat podataka
# ---------------------------------------
class WeatherFetcher(QThread):
    finished = Signal(dict)   # emitira dict s current i forecast
    error = Signal(str)       # emitira poruku greške

    def __init__(self, city: str, api_key: str, units: str):
        super().__init__()
        self.city = city
        self.api_key = api_key
        self.units = units

    def run(self):
        """Dohvat podataka s OpenWeather API-ja."""
        # TODO: implementirati GET pozive na /weather i /forecast
        #       te emitirati self.finished({...}) ili self.error("...").
        pass


# ---------------------------------------
# Glavna aplikacija
# ---------------------------------------
class WeatherApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        init_db()
        self.api_key = "YOUR_API_KEY_HERE"
        self.units = "metric"
        self.weather_thread = None

        # TODO: povezati gumbe i combo box s metodama
        # npr. self.fetch_button.clicked.connect(self.start_fetch_weather)

    def load_settings(self):
        """Učitava spremljene postavke iz baze."""
        # TODO: dohvatiti api_key i units iz tablice settings
        pass

    def save_settings(self):
        """Sprema postavke u bazu podataka."""
        # TODO: zapisati api_key i units u tablicu settings
        pass

    def start_fetch_weather(self):
        """Pokreće nit za dohvat vremena."""
        # TODO: provjera unosa, kreiranje i start WeatherFetcher niti
        pass

    def handle_weather_data(self, data: dict):
        """Ažurira UI s dohvaćenim podacima."""
        # TODO: popuniti city_label, temp_label, desc_label, itd.
        #       pozvati update_icon, update_forecast_table, draw_temp_graph
        pass

    def update_icon(self, icon_code: str):
        """Prikazuje ikonu vremena u city_label."""
        # TODO: dohvatiti ikonu s openweathermap i postaviti QPixmap
        pass

    def update_forecast_table(self, forecast: dict):
        """Popunjava QTableWidget podacima prognoze."""
        # TODO: dodati 24 unosa (vrijeme, temperatura, opis)
        pass

    def draw_temp_graph(self, forecast: dict):
        """Crtanje grafikona temperature."""
        # TODO: nacrtati jednostavan grafikon unutar graph_label
        pass

    def save_to_history(self, city: str, temp: float):
        """Sprema unos u tablicu history."""
        # TODO: insert u bazu (city, date, temp)
        pass

    def show_error(self, message: str):
        """Prikazuje poruku o grešci."""
        QMessageBox.critical(self, "Greška", message)


# ---------------------------------------
# Entry point
# ---------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())

