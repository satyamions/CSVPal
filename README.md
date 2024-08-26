# CSVPal

CSVPal is a Django-based web application that allows users to log in, sign up, upload CSV files, and manage the data within a user-friendly interface. Users can view, update, insert new rows, and export the latest data as CSV files. The app also supports adding new columns, storing them in the database, and provides APIs for login, signup, and CSV upload.

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

### Web Interface
- **Sign Up/Login:** Sign up or log in to access the application.
- **Upload CSV:** Upload a CSV file using the "Upload" button.
- **Manage Data:** View the CSV data in a table. You can update existing rows or insert new ones.
- **Export CSV:** Click the "Export" button to download the updated CSV file.

### API Endpoints
- **Login:** **POST** `/api/login/`
- **Signup:** **POST** `/api/signup/`
- **Upload CSV:** **POST** `/api/upload/`

## Troubleshooting

If you encounter issues with SSL certificates when installing dependencies, you can resolve them by following these steps:

1. Install `certifi` using pip with trusted hosts:

    ```bash
    pip install certifi --trusted-host pypi.org --trusted-host files.pythonhosted.org
    ```

2. Import `certifi` and check the certificate path:

    ```python
    import certifi
    print(certifi.where())
    ```

3. Set the `REQUESTS_CA_BUNDLE` environment variable:

    - On Windows PowerShell:

      ```bash
      $env:REQUESTS_CA_BUNDLE=""
      ```

This should resolve any SSL-related errors you might encounter during setup.
