import sys
import sqlite3
import requests
import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap
from ui_vrijeme import Ui_MainWindow


# ---------------------------------------
# Baza podataka - inicijalizacija
# ---------------------------------------
def init_db():
    """Kreira SQLite bazu i tablice ako ne postoje."""
    conn = sqlite3.connect("weather_app.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            date TEXT NOT NULL,
            temp REAL NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


# ---------------------------------------
# Worker thread za dohvat podataka
# ---------------------------------------
class WeatherFetcher(QThread):
    finished = Signal(dict)  # emitira dict s current i forecast
    error = Signal(str)  # emitira poruku greške

    def __init__(self, city: str, api_key: str, units: str):
        super().__init__()
        self.city = city
        self.api_key = api_key
        self.units = units

    def run(self):
        """Dohvat podataka s OpenWeather API-ja."""
        # TODO: implementirati GET pozive na /weather i /forecast
        #       te emitirati self.finished({...}) ili self.error("...").
        try:
            url = "http://api.openweathermap.org/data/2.5"  # ovo mie chat reka da prominim da nemam geo.koor.

            weather_url = f"{url}/weather"
            weather_respond = requests.get(
                weather_url,
                params={
                    "q": self.city,
                    "appid": self.api_key,
                    "units": self.units,
                },
            )
            weather_respond.raise_for_status()
            current = weather_respond.json()
            print(current)

            forecast_url = f"{url}/forecast"
            forecast_respond = requests.get(
                forecast_url,
                params={
                    "q": self.city,
                    "appid": self.api_key,
                    "units": self.units,
                },
            )
            forecast_respond.raise_for_status()
            forecast = forecast_respond.json()
            self.finished.emit({"current": current, "forecast": forecast})

        except requests.RequestException as e:
            self.error.emit(f"{e}")


# ---------------------------------------
# Glavna aplikacija
# ---------------------------------------
class WeatherApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        init_db()
        self.api_key = "e0b96fc62eb1b237a4d1db128638097f"
        self.units = "metric"
        self.weather_thread = None

        # TODO: povezati gumbe i combo box s metodama
        # npr. self.fetch_button.clicked.connect(self.start_fetch_weather)
        self.fetch_button.clicked.connect(self.start_fetch_weather)
        self.save_settings_button.clicked.connect(self.save_settings)

        self.load_settings()
        self.units_combo.setCurrentText(self.units)

    def load_settings(self):
        """Učitava spremljene postavke iz baze."""
        # TODO: dohvatiti api_key i units iz tablice settings
        conn = sqlite3.connect("weather_app.db")
        cursor = conn.cursor()
        cursor.execute("SELECT key, value FROM settings")
        rows = cursor.fetchall()
        conn.close()
        settings = {}
        for k, v in rows:
            settings[k] = v

        self.api_key = settings.get("api_key", self.api_key)
        self.units = settings.get("units", self.units)

    def save_settings(self):
        """Sprema postavke u bazu podataka."""
        # TODO: zapisati api_key i units u tablicu settings
        conn = sqlite3.connect("weather_app.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO settings (key, value) VALUES (?,?)", ("api_key", self.api_key)
        )
        cursor.execute(
            "INSERT INTO settings (key, value) VALUES(?, ?)", ("units", self.units)
        )
        conn.commit()
        conn.close()

    def start_fetch_weather(self):
        """Pokreće nit za dohvat vremena."""
        # TODO: provjera unosa, kreiranje i start WeatherFetcher niti
        city = self.city_input.text().strip()
        self.fetch_button.setEnabled(False)

        self.weather_thread = WeatherFetcher(city, self.api_key, self.units)
        self.weather_thread.finished.connect(self.handle_weather_data)
        self.weather_thread.error.connect(self.show_error)
        self.weather_thread.finished.connect(
            lambda _: self.fetch_button.setEnabled(True)
        )
        self.weather_thread.start()

    def handle_weather_data(self, data: dict):
        """Ažurira UI s dohvaćenim podacima."""
        # TODO: popuniti city_label, temp_label, desc_label, itd.
        #       pozvati update_icon, update_forecast_table, draw_temp_graph
        current = data["current"]
        forecast = data["forecast"]

        self.city_label.setText(current.get("name", ""))
        temp = current["main"]["temp"]
        self.temp_label.setText(f"{temp} °C")
        self.desc_label.setText(current["weather"][0]["description"].capitalize())
        self.save_to_history(current.get("name", ""), temp)

        icon_code = current["weather"][0]["icon"]
        self.update_icon(icon_code)
        self.update_forecast_table(forecast)
        # self.draw_temp_graph(forecast)

    def update_icon(self, icon_code: str):
        """Prikazuje ikonu vremena u city_label."""
        # TODO: dohvatiti ikonu s openweathermap i postaviti QPixmap
        try:
            url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(url).content)
            self.icon_label.setPixmap(pixmap)
        except Exception:
            pass

    def update_forecast_table(self, forecast: dict):
        """Popunjava QTableWidget podacima prognoze."""
        # TODO: dodati 24 unosa (vrijeme, temperatura, opis)
        self.forecast_table.setRowCount(24)
        for i, entry in enumerate(forecast["list"][:24]):
            time_item = QTableWidgetItem(entry["dt_txt"])
            temp_item = QTableWidgetItem(
                f"{entry['main']['temp']} °{'C' if self.units=='metric' else 'F'}"
            )
            desc_item = QTableWidgetItem(
                entry["weather"][0]["description"].capitalize()
            )
            self.forecast_table.setItem(i, 0, time_item)
            self.forecast_table.setItem(i, 1, temp_item)
            self.forecast_table.setItem(i, 2, desc_item)

    def draw_temp_graph(self, forecast: dict):
        """Crtanje grafikona temperature."""
        # TODO: nacrtati jednostavan grafikon unutar graph_label
        pass

    def save_to_history(self, city: str, temp: float):
        """Sprema unos u tablicu history."""
        # TODO: insert u bazu (city, date, temp)
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        conn = sqlite3.connect("weather_app.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO history (city, date, temp) VALUES (?, ?, ?)",
            (city, date_str, temp),
        )
        conn.commit()
        conn.close()

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
