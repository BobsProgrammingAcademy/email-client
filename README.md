# Email Client

This is an email client that makes API calls to send and receive emails built using **Django 4**, **HTML 5**, **CSS 3**, **Bootstrap 5** with a **Bootswatch** theme, and vanilla **JavaScript**.

![plot](https://github.com/BobsProgrammingAcademy/Email-Client/blob/main/static/images/email_client.png?raw=true)


## Table of Contents 
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Run the application](#run-the-application)
- [Run the tests](#run-the-tests)
- [View the application](#view-the-application)
- [Note](#note)
- [Copyright and License](#copyright-and-license)


### Prerequisites

Install the following prerequisites:

1. [Python 3.8-3.11](https://www.python.org/downloads/)
<br> This project uses **Django v4.2.4**. For Django to work, you must install a correct version of Python on your machine. More information [here](https://django.readthedocs.io/en/stable/faq/install.html).
2. [Visual Studio Code](https://code.visualstudio.com/download)


### Installation

#### 1. Create a virtual environment

From the **root** directory, run:

```bash
python -m venv venv
```

#### 2. Activate the virtual environment

From the **root** directory, run:

On macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\scripts\activate
```

#### 3. Install required dependencies

From the **root** directory, run:

```bash
pip install -r requirements.txt
```

#### 4. Run migrations

From the **root** directory, run:

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```


### Run the application

From the **root** directory, run:

```bash
python manage.py runserver
```


### Run the tests

From the **root** directory, run:

```bash
python manage.py test --pattern="tests.py"

```


### View the application

Go to http://127.0.0.1:8000/ to view the application.


### Note

Just remember to send an email to an email address that already exists in the database.


### Copyright and License

Copyright © 2022 Bob's Programming Academy. Code released under the MIT license.
