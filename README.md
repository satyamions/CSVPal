# CSVPal

CSVPal is a Django-based web application that allows users to log in, sign up, upload CSV files, and manage the data within a user-friendly interface. Users can view, update, insert new rows, and export the latest data as CSV files. The app also supports adding new columns, storing them in the database, and provides APIs for login, signup, and CSV upload.

## CSVPal Video Demo

**Part 1: Web Interface**  
[Watch the demo](https://drive.google.com/file/d/1s0o2fOTYATNC2PTT9710CJ1D4kiboFgq/view?usp=sharing) to see the web interface in action, including user authentication, CSV file uploads, data management, and export functionality.

**Part 2: API Showcase**  
[Watch the demo](https://drive.google.com/file/d/1jkP0utEgdiv7L8e9rvkYMLZwYPsez2yo/view?usp=sharing) to explore the API endpoints for login, signup, and CSV file uploads.

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

4. **Make migrations**:

    ```bash
    python manage.py makemigrations
    ```

5. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

6. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

7. **Access the application**:

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
- **Upload CSV:** **POST** `/api/upload_csv/`

Certainly! Here’s the properly formatted section for testing the application:

---

## Testing the Application

### 0. Using Python Shell

To enter the Django Python shell, run:

```bash
python manage.py shell
```

### 1. Testing Login, Signup, and Logout with Django Test Client

You can use Django's test client to test the login, signup, and logout functionality. Here’s an example script to perform these actions:

```python
from django.test import Client

# Initialize the Django test client
client = Client()

# Signup a new user
response = client.post('/api/signup/', {
    'username': 'testusernew24',
    'password': 'testpass',
    'email': 'testuser@example24.com'
}, content_type='application/json')
print("Signup Status Code:", response.status_code)
print("Signup Response:", response.content)

# Login with the new user
response = client.post('/api/login/', {
    'username': 'testusernew24',
    'password': 'testpass'
}, content_type='application/json')
print("Login Status Code:", response.status_code)
print("Login Response:", response.content)

# Logout the user
response = client.post('/api/logout/', content_type='application/json')
print("Logout Status Code:", response.status_code)
print("Logout Response:", response.content)
```

### 2. Testing CSV Upload Using Postman

To test the CSV upload functionality, follow these steps:

1. **Prepare the CSV File**: Create a CSV file (e.g., `test_data.csv`) with sample data. For example:

    ```csv
    Column1,Column2,Column3
    Value1,Value2,Value3
    Value4,Value5,Value6
    ```

2. **Open Postman**: Launch Postman on your machine.

3. **Configure the Request**:
    - **HTTP Method**: Select `POST`.
    - **Request URL**: Enter `http://127.0.0.1:8000/api/upload_csv/`.
    - **Body**:
      - Select `form-data`.
      - Add a new key with the name `file`.
      - Set the type to `File`.
      - Click `Select Files` and choose your CSV file (`test_data.csv`).

4. **Send the Request**: Click the `Send` button.

5. **Verify the Response**:
    - **Status Code**: Ensure it’s `200 OK` or `201 Created`.
    - **Response Body**: Check for the confirmation message or expected result.

**Example Postman Configuration**:

- **HTTP Method**: `POST`
- **Request URL**: `http://127.0.0.1:8000/api/upload/`
- **Body**:
  - **Type**: `form-data`
  - **Key**: `file`
  - **Value**: `Select Files` (choose `test_data.csv`)

**Example Response**:

```json
{
    "message": "CSV file uploaded successfully.",
    "data": {
        "file_name": "test_data.csv",
        "rows_uploaded": 2
    }
}
```

### 3. Testing CSV Data Management

After uploading a CSV file, you can view and manage the data through the web interface. This includes:

- **Viewing Data**: Navigate to the page where the uploaded CSV data is displayed.
- **Updating Rows**: Edit existing rows in the table.
- **Inserting New Rows**: Add new rows to the table.
- **Exporting Data**: Use the "Export" button to download the latest data as a CSV file.

### 4. Troubleshooting

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
      $env:REQUESTS_CA_BUNDLE="(response from print(certifi.where())"
      ```

This should resolve any SSL-related errors you might encounter during setup.
