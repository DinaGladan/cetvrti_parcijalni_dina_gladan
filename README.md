# **Parcijalni Ispit - Python u području Internet stvari **

## **Upute za Rješavanje Zadatka**


1. **Priprema okruženja:**
   - Kreirajte "fork" repozitorija.
   - Dodijelite repozitoriju naziv u formatu `cetvrti_parcijalni_ime_prezime` (primjer: `cetvrti_parcijalni_pero_peric`). 
   - **VAŽNO:** Nemojte kreirati "clone" repozitorija jer nemate pravo mijenjanja.

---

### 2. **Postavljanje projekta**
#### Struktura projekta:
```
weather_app/                 # Glavni direktorij projekta (PySide6 aplikacija)
│
├── main.py                  # Glavna aplikacijska skripta (PySide6, logika, DB, niti)
├── vrijeme_app.ui           # Qt Designer UI datoteka (izvoz: QMainWindow + tabovi)
├── ui_vrijeme.py            # Generirani Python kod iz .ui (pyside6-uic)
│
├── resources/               # (opcionalno) ikone/slike/fontovi
│   └── .gitkeep
│
├── weather_app.db           # SQLite baza (generira se pri prvom pokretanju)
│
├── requirements.txt         # Ovisnosti projekta
│
└── README.md                # Kratke upute za pokretanje (opcionalno)

```
#### Koraci:
   - Nakon što ste kreirali fork, klonirajte repozitorij s vašeg GitHub profila na lokalno računalo koristeći GitHub Desktop ili drugu omiljenu metodu.
   - **Nakon kloniranja**, kreirajte novu lokalnu granu nazvanu `ispit`
   - Sve promjene unosite isključivo unutar grane ispit
   - Instalirajte sve potrebne module pomoću `requirements.txt` kako biste osigurali da aplikacija ima sve potrebne biblioteke.
     
1. Klonirajte repozitorij:
   ```bash
   git clone https://github.com/vaše-korisničko-ime/cetvrti_parcijalni.git
   cd cetvrti_parcijalni
   ```

2. Kreirajte virtualno okruženje:
   ```bash
   python -m venv venv
   ```

3. Aktivirajte virtualno okruženje:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Instalirajte potrebne module:
   ```bash
   pip install -r requirements.txt
   # ili direktno:
   pip install PySide6 requests
   ```
   
 5. Izrada UI-a (odaberite jednu opciju)

   ### Opcija A — Izradite u Qt Designeru
   1. Otvorite **Qt Designer** i kreirajte `QMainWindow`.
   2. Kao **centralni widget** postavite `QTabWidget` (naziv: `main_tabs`).
   3. Dodajte kartice i widgete **točno** ovim imenima:
      - **Prva kartica** `tab_trenutno` (QWidget)
        - `QLabel` — naslov “Trenutno vrijeme”
        - `QLineEdit` — `city_input`
        - `QPushButton` — `fetch_button` (“Dohvati vrijeme”)
        - `QLabel` — `city_label`
        - `QLabel` — `icon_label`
        - `QLabel` — `temp_label`
        - `QLabel` — `desc_label`
        - `QLabel` — `humidity_label`
        - `QLabel` — `wind_label`
      - **Druga kartica** `tab_prognoza` (QWidget)
        - `QTableWidget` — `forecast_table` (3 stupca: “Vrijeme”, “Temperatura”, “Opis”)
        - `QLabel` — `graph_label`
      - **Treća kartica** `tab_postavke` (QWidget)
        - `QLabel` — “OpenWeather API ključ:”
        - `QLineEdit` — `api_key_input`
        - `QLabel` — “Jedinice:”
        - `QComboBox` — `units_combo` (stavke: “Celzijus”, “Fahrenheit”)
        - `QPushButton` — `save_settings_button` (“Spremi postavke”)
   4. U **QMainWindow** dodajte **QStatusBar**.
   5. Spremite datoteku kao **`vrijeme_app.ui`** u korijen projekta.
   6. Generirajte Python kod iz `.ui`:
      ```bash
      pyside6-uic vrijeme_app.ui -o ui_vrijeme.py
      ```

   ### Opcija B — Preuzmite gotov UI s Gita
   1. Preuzmite datoteku **`vrijeme_app.ui`** iz repozitorija (putanja: `./vrijeme_app.ui`).
   2. Kopirajte je u korijen projekta (pokraj `main.py`).
   3. Generirajte Python kod iz `.ui`:
      ```bash
      pyside6-uic vrijeme_app.ui -o ui_vrijeme.py
      ```

   7. Pokrenite aplikaciju:
     ```
      python main.py
           ```


> Napomena: Nazivi widgeta moraju biti **identični** gore navedenima (npr. `city_input`, `forecast_table`, `units_combo`…), jer ih aplikacijska logika očekuje.

---

## 3. **Dodajte funkcionalnosti kako slijedi:**

### Baza (SQLite)
- Tablica **settings(key, value)** za spremanje API ključa i jedinica.  
- Tablica **history(id, city, date, temp)** za evidenciju pretraživanja.  

### Dohvat podataka (OpenWeather API)
- Trenutno vrijeme:  
  `GET /weather?q=<city>&appid=<API_KEY>&units=<units>`  
- Prognoza:  
  `GET /forecast?q=<city>&appid=<API_KEY>&units=<units>`  

### Višenitnost (QThread)
- Napravite **WeatherFetcher(QThread)** koji dohvaća *trenutno* i *prognozu* te emitira signale **finished** ili **error**.  

### UI povezivanje
- **fetch_button** → pokreće dohvat  
- **save_settings_button** → sprema `api_key` i `units` u SQLite  
- **units_combo** → ažurira interni state (`metric` / `imperial`)  

### Prikaz podataka
- **Tab “Trenutno”**: ispis naziva grada, države, temperatura, opis, vlažnost, vjetar, ikona.  
- **Tab “Prognoza”**: QTableWidget (24 unosa), grafikon promjene temperature.  
- **StatusBar**: informativne poruke i greške.  

### Greške i rubni slučajevi
- **404** – grad ne postoji  
- **401** – neispravan API ključ  
- Problemi s mrežom  
- Prazan unos grada, nedostajući API ključ  

---

## 5. Upotreba i testiranje

### API ključ
- U aplikaciji otvorite **Postavke**, upišite **OpenWeather API ključ** i odaberite **Celzijus** ili **Fahrenheit**, zatim kliknite **Spremi postavke**.  
- Očekujte poruku u statusnoj traci: *“Postavke uspješno spremljene.”*  

### Trenutno vrijeme
- Upišite grad (npr. *Zagreb*), kliknite **Dohvati vrijeme**.  
- Provjerite da se osvježavaju naziv grada/države, temperatura, opis, vlažnost, vjetar i ikona.  

### Prognoza
- Otvorite karticu **Prognoza** – provjerite tablicu (24 zapisa) i graf promjene temperature.  

### Greške
- Grad ne postoji (npr. *asdfgh*) → poruka *“Grad ‘…’ nije pronađen.”*  
- Krivi API ključ → *“Nevažeći API ključ. Provjerite postavke.”*  
- Prekid veze → *“Greška s mrežnom vezom. Provjerite internet.”*  

### Baza podataka
- Datoteka **weather_app.db** sadrži tablice **settings** i **history**.  
- Možete je otvoriti u npr. **DB Browser for SQLite** i provjeriti zapise.  

---

## 6. Dodatne Upute

- Ne mijenjajte zadanu strukturu projekta osim gdje je izričito navedeno.  
- Koristite razumne nazive widgeta točno kako je specificirano (npr. `city_input`, `forecast_table`…), jer se na njih oslanja kod.  
- Vodite računa o **obradi grešaka** i **statusnim porukama** za bolji UX.  
- *(Preporuka)* Koristite **TypeHints** u funkcijama i metodama.  

---

## Podnošenje Rješenja

### Nakon završetka:
```bash
git add .
git commit -m "Implementirana PySide6 aplikacija za vrijeme"
git push -u origin ispit
```

### Otvorite **Pull Request** iz grane `ispit` prema `main`
- **Autor:** Vaše ime  
- **Reviewer:** Predavač (dodajte ga kao suradnika)  

### Podjela repozitorija s predavačem
- `Settings` → `Collaborators` → dodajte predavača kao **Contributor** i pošaljite pozivnicu.  

⚠️ Provjerite da su sve promjene **commitane i pushane** prije dodavanja predavača i otvaranja PR-a.  

> **Napomena:** Ako se upute ne budu striktno slijedile, rješenje se neće pregledati.  

> **Rok predaje:** prema dogovoru s predmetom/predavačem.  

---

**Sretno!**
