Hallo! Kurz zu mir:
- Ich mache den Backend-Kurs der Developer Akademie (Django + Django REST Framework).
- Die Kurs-Videos nutzen ältere Versionen, ich arbeite mit den neuesten (Django 6, DRF 3.18+).
  Bitte hilf mir, wenn etwas anders ist als beim Mentor.
- Ich bin Anfänger, erklär Fehler bitte einfach und auf Deutsch.
- Ich tippe mit den Videos mit, also nicht alles vorwegnehmen, nur prüfen und korrigieren,
  wenn ich frage.
- Windows, VS Code, PowerShell. Virtuelle Umgebung heißt "env".
- Git: Commits OHNE Claude als Co-Author, pushen mache ich selbst.

Vorheriges Projekt: market_app (Permissions, Token-Auth, Registration, CustomLoginView).
Jetzt neues Projekt, hier die README:

README -->


# 🏆 TrophyCase API

![Django](https://img.shields.io/badge/Django-4.x-green)  
![DRF](https://img.shields.io/badge/DRF-3.x-blue)  
![Auth](https://img.shields.io/badge/Auth-Token-orange)  
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

Eine charmante, minimalistische Django REST API zum Erfassen persönlicher Trophäen und Erfolge.  
Ideal für API-Demos mit Postman oder als Backend-Grundgerüst.

---

## 🚀 Features

- 🧑‍💻 Benutzerregistrierung mit Passwort-Wiederholung  
- 🔐 Token-basierte Authentifizierung (Login / Logout)  
- 🏆 CRUD-API für eigene Achievements (Trophäen)  
- 👀 Zugriff nur auf eigene Daten  
- 🔍 Optional: Filter & Sortierung  
- ⚙️ Ready für Postman-Tests

---

## 📦 Setup

### Voraussetzungen

- Python 3.8+  
- pip / virtualenv  
- (Optional: Postman)

### Lokales Setup

```
git clone <repo-url>  
cd trophycase  
python -m venv venv  
source venv/bin/activate  # Windows: venv\Scripts\activate  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  
```

---

## 🔐 Auth-Endpoints

| Methode | Endpoint           | Beschreibung              |
|---------|--------------------|---------------------------|
| POST    | /auth/register/    | Benutzer registrieren     |
| POST    | /auth/login/       | Token erhalten (Login)    |
| POST    | /auth/logout/      | Token löschen (Logout)    |

> **Hinweis:** Authentifizierte Requests brauchen folgenden Header:

```
Authorization: Token <your_token>  
```

---

## 🏆 Achievement-API

| Methode | Endpoint                | Beschreibung                  |
|---------|-------------------------|-------------------------------|
| GET     | /api/achievements/      | Alle eigenen Trophäen         |
| POST    | /api/achievements/      | Neue Trophäe erstellen        |
| GET     | /api/achievements/<id>/ | Einzelne Trophäe anzeigen     |
| PATCH   | /api/achievements/<id>/ | Teilweise aktualisieren       |
| DELETE  | /api/achievements/<id>/ | Trophäe löschen               |

### Beispiel-Request (POST)

```
{
  "title": "Erstes Backend-Projekt",
  "description": "Django REST API erfolgreich gestartet.",
  "category": "Coding"
}
```

---

## 🗂️ Projektstruktur

```
trophycase/  
├── achievements_app/     # CRUD-API für Trophäen  
├── auth_app/             # Login / Registrierung / Logout  
├── trophycase/           # Settings, URLs, WSGI  
└── manage.py  
```

---

## 🔒 Sicherheit

- Authentifizierte API-Endpoints mit Token-Header  
- Benutzer dürfen nur auf eigene Trophäen zugreifen  
- Tokens werden beim Logout vollständig gelöscht

---

## 🧑‍🎓 Tech Stack

- Python / Django  
- Django REST Framework  
- DRF TokenAuth  
- SQLite (default)

---

## ✨ Idee & Ziel

Dieses Projekt dient als charmante Demo, um API-Konzepte mit Django REST Framework und Postman verständlich, visuell und zugänglich zu machen.
