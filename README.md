# Email Client

This is an email client that makes API calls to send and receive emails built using **Django 4.0.4**, **Bootstrap 5.1.3** and vanilla **JavaScript**.

![plot](https://github.com/BobsProgrammingAcademy/Email-Client/blob/main/static/images/email_client.png?raw=true)


## Table of Contents 
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Run the application](#run-the-application)
- [View the application](#view-the-application)
- [Note](#note)


## Prerequisites

Install the following prerequisites:

1. [Python 3.9.12 or higher](https://www.python.org/downloads/)
2. [Visual Studio Code](https://code.visualstudio.com/download)


## Installation

### 1. Create a virtual environment

From the **root** directory run:

```bash
python -m venv venv
```

### 2. Activate the virtual environment

From the **root** directory run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

### 3. Install required dependencies

From the **root** directory run:

```bash
pip install -r requirements.txt
```

### 4. Run migrations

From the **root** directory run:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

## Run the application

From the **root** directory run:

```bash
python manage.py runserver
```

## View the application

Go to http://127.0.0.1:8000/ to view the application.

## Note

Just remember to send an email to an email address that already exists in the database.
