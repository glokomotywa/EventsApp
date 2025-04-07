# EventsApp - Aplikacja do zarządzania wydarzeniami  
**Repozytorium**: [https://github.com/glokomotywa/EventsApp](https://github.com/glokomotywa/EventsApp)  

## 📋 Spis treści  
1. [Opis](#-opis)  
2. [Wymagania](#-wymagania)  
3. [Instalacja](#-instalacja)  
4. [Konfiguracja](#-konfiguracja)  
5. [Uruchomienie](#-uruchomienie)  
6. [Struktura projektu](#-struktura-projektu)  
7. [Funkcje](#-funkcje)  
---

## 📝 Opis  
Aplikacja webowa oparta na Django, która umożliwia:  
- **Rejestrację i logowanie użytkowników**  
- **Tworzenie wydarzeń** z opisem, datą i lokalizacją  
- **Komentowanie** istniejących wydarzeń  
- **Wyrażanie zainteresowania** poprzez przycisk "Jestem zainteresowany"  

---

## 🛠 Wymagania  
- Python 3.9 lub nowszy  
- System kontroli wersji Git (opcjonalnie)  
- Zalecane środowisko wirtualne (`virtualenv`)  

---

## 🚀 Instalacja  
1. Sklonuj repozytorium:  
```bash  
git clone https://github.com/glokomotywa/EventsApp.git  
cd EventsApp  
```
2. Utwórz i aktywuj środowisko wirtualne
```bash
# Linux/macOS  
python3 -m venv venv  
source venv/bin/activate  

# Windows  
python -m venv venv  
.\venv\Scripts\activate  
```
3. Zainstaluj zależności
```bash
pip install -r requirements.txt  
```

## ⚙ Konfiguracja
1. Wykonaj migracje do bazy danych
```bash
python manage.py migrate  
```
2. Utwórz konto administratora
```bash
python manage.py createsuperuser  
```bash

## ▶ Uruchomienie
```bash
python manage.py runserver  
```
- Strona główna: http://127.0.0.1:8000/
- Panel administracyjny: http://127.0.0.1:8000/admin

## ✨ Funkcje
✨ Funkcje

Dla użytkowników:

- Rejestracja i logowanie przez formularz
- Tworzenie wydarzeń z:
	- Tytułem
	- Szczegółowym opisem
	- Datą i godziną
	- Lokalizacją
- Komentowanie w sekcji dyskusji
- Przycisk "Jestem zainteresowany" – licznik uczestników

Dla administratorów:

- Pełna kontrola nad:
	- Użytkownikami
	- Wydarzeniami
	- Komentarzami
- Funkcja eventstats:
	- Wyświetlanie statystyk dla wydarzeń
```bash
python manage.py eventstats
```
