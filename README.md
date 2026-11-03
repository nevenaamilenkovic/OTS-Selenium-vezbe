# Vežbaonica lokatora (OTS 26/27)

Stranica za vežbanje pronalaženja elemenata u Selenium-u (Termin 7).
Sadrži formu i tabelu sa namernim zamkama za lokatore, i dugme koje menja
raspored stranice da bi se videlo koji lokatori su stabilni.

## Pokretanje stranice

- Online: GitHub Pages adresa koju daje predmetni nastavnik.
- Lokalno, bez interneta:

```
python -m http.server 8000 --directory docs
```

pa otvorite http://localhost:8000. Druga verzija stranice: http://localhost:8000/#v2

## Priprema okruženja

```
python -m venv venv
venv\Scripts\Activate.ps1      # Windows PowerShell
source venv/bin/activate       # Linux / macOS
pip install -r requirements.txt
```

## Pokretanje testova

```
pytest -v
```
