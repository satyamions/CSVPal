# CSVPal

CSVPal is a Django-based web application designed to simplify the process of uploading, managing, and manipulating CSV files. The application provides a user-friendly interface for working with CSV files and includes authentication features for secure access.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (login, signup, logout).
- Upload and manage CSV files.
- View and manipulate CSV data through an intuitive interface.

## Project Structure

```
CSVPal/
│
├── .venv/                # Virtual environment
├── myproject/            # Project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL configuration
│   ├── wsgi.py
│   └── __pycache__/
│
├── myapp/                # Application directory
│   ├── __init__.py
│   ├── admin.py          # Admin configuration
│   ├── apps.py           # App configuration
│   ├── forms.py          # Forms used in the app
│   ├── models.py         # Database models
│   ├── serializers.py    # Serializers for REST API 
│   ├── tests.py          # Unit tests
│   ├── views.py          # Views handling the logic
│   ├── migrations/       # Database migrations
│   └── __pycache__/
│
├── templates/            # HTML templates
│   ├── display.html
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   └── upload.html
│
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## Setup and Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/satyamions/CSVPal.git
    cd csvpal
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

6. **Access the application**:

    Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Authentication**: Users can sign up, log in, and log out.
- **CSV Upload**: Authenticated users can upload CSV files.
- **View and Manage**: Uploaded CSV files can be viewed and managed through the web interface.
