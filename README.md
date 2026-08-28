# Flashcard Learning App

A small web app for creating and learning flashcards. I built it as a school project to practice Python, Flask and working with a database.

## Features

- Create, edit and delete folders and subfolders
- Create, edit and delete flashcards
- Study cards from a selected folder and its subfolders
- Shuffle cards for each study session
- Mark cards as known or repeat them later
- Store data in a local SQLite database
- German user interface

## Technologies

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2
- HTML, CSS and JavaScript

## Running the App

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/flashcard-learning-app.git
cd flashcard-learning-app
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the app

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. A local SQLite database is created automatically when the app is started for the first time.

## Project Structure

```text
.
├── app.py                 # Flask application, routes and database models
├── requirements.txt       # Python dependencies
├── static/
│   └── style.css          # Stylesheet
└── templates/
    ├── index.html         # Folder and flashcard management
    └── lernen.html        # Study view
```

## How It Works

The app has two database models. `Ordner` stores folders and subfolders, while `Karte` stores the questions, answers and review dates. Flask handles the pages and actions, and JavaScript is used for the interactive learning view.

## AI-Assisted Development

This project was created as a school project with support from AI tools. I used it to learn about Flask routes, SQLAlchemy models, SQLite databases, Jinja templates and JavaScript.
