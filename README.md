# Microblog

A full-featured microblogging application built with Flask.

## Features

- **User Authentication**: Login, Registration, Password Reset, Email confirmations.
- **User Profiles**: User avatars, "About Me" sections, Follow/Unfollow functionality.
- **Internationalization (i18n)**: Full support for English and Spanish translations.
- **Full-Text Search**: Integration with Elasticsearch for searching posts.
- **Background Tasks**: Asynchronous tasks using Redis and RQ (e.g., email sending, data export).
- **Live Translations**: Integrated translation service for user posts.
- **Responsive Design**: Uses Bootstrap for mobile-friendly UI.

## Technology Stack

- **Backend**: Python, Flask, Flask-SQLAlchemy, Flask-Login, Flask-Migrate, Flask-Babel.
- **Database**: SQLite (Development), extensible to PostgreSQL/MySQL.
- **Search**: Elasticsearch.
- **Task Queue**: Redis & RQ.
- **Frontend**: Jinja2 Templates, Bootstrap, Moment.js.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/microblog.git
    cd microblog
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory:
    ```ini
    FLASK_APP=microblog.py
    SECRET_KEY=your-secret-key
    MAIL_SERVER=localhost
    MAIL_PORT=8025
    ELASTICSEARCH_URL=http://localhost:9200
    REDIS_URL=redis://localhost:6379/0
    MS_TRANSLATOR_KEY=your-azure-key  # Optional
    ```

5.  **Initialize the Database:**
    ```bash
    flask db upgrade
    ```

6.  **Run the Application:**
    ```bash
    flask run
    ```

## Testing

Run the unit tests:
```bash
python tests.py
```

## Translations

Update translations:
```bash
flask translate update
```

Compile translations:
```bash
flask translate compile
```
