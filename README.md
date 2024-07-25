# Flask Application

A simple Flask application featuring user authentication and blog functionality.

## Features

- User registration and login
- Blog creation and display
- Password hashing and authentication
- SQLite database

## Prerequisites

- Python 3.x
- pip (Python package manager)
- virtualenv (optional but recommended)

## Setup

### 1. Clone the Repository

```
git clone https://github.com/rittiikkk/flaskApp.git
cd flaskApp
```
### 2. Create a Virtual Environment

```
python -m venv venv

```
### 3. Activate the Virtual Environment
##### On Windows:

```
venv\Scripts\activate
```

##### On macOS/Linux:

```
source venv/bin/activate
```
### 4. Install Dependencies
```sh
pip install -r requirements.txt
```

### 5. Set Up Environment Variables
##### Create a .env file in the root directory and add the following content:
#### .env file

```
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///site.db
Replace your_secret_key with a secure key for your application.
```
### 6. Initialize the Database
```
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```
### 7. Run the Application
```
flask run
```
Navigate to http://127.0.0.1:5000/ in your web browser to view the application.
