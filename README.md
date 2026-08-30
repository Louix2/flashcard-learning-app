# Flashcard Learning App

*Built: January/February 2026*

A small web app for creating and studying flashcards. I built it as a school project to get a better understanding of Python, Flask and how a database works, since I didn't really know any of that before (and honestly still can't fully explain every part of the code).

The idea is basically a simple version of Anki: you sort your flashcards into folders (and subfolders), then pick a folder and study the cards inside it.

## Features

- Create, edit and delete folders and subfolders
- Create, edit and delete flashcards
- Study cards from a selected folder, including its subfolders
- Cards are shuffled each study session
- Mark a card as known or have it come back later
- Data is stored locally in an SQLite database
- Interface is in German

## Tech Stack

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2
- HTML, CSS, JavaScript

## Setup

Clone the repo:

```bash
git clone https://github.com/Louix2/flashcard-learning-app.git
cd flashcard-learning-app
```

Create a virtual environment.

Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```bash
python -m pip install -r requirements.txt
```

Run the app:
```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. The SQLite database file is created automatically the first time you start the app.

## Project Structure

```
.
├── app.py              # Flask app, routes, database models
├── requirements.txt
├── static/
│   └── style.css
└── templates/
    ├── index.html       # folder/flashcard management
    └── lernen.html       # study view
```

## How It Works

There are two database models: `Ordner` (folders) and `Karte` (flashcards, with question, answer and review status). Flask handles the routes and logic, Jinja renders the templates, and a bit of JavaScript takes care of the study view (shuffling, flipping cards, etc.).

## What I Learned

This was my first bigger project outside of school exercises, so a lot of this was new to me:

- How Flask routes and templates work together
- Structuring a project into folders and subfolders
- Basic frontend interactivity with JavaScript

## Notes

I used an AI coding assistant while building this, mainly for debugging and explaining concepts I didn't understand yet. The idea was inspired by Anki, adapted to what I wanted to build myself, and I decided on the structure and features on my own.
