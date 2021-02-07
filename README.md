# PostSocial

## Project Setup

1. Ensure Python 3 is installed on your system. Verify with this command:

    ```bash
     python -V
     # Python 3.X.Y
    ```

    If the command returns version 2, download and install Python 3.

1. Ensure Postgres is installed locally. Check the [official website](https://www.postgresql.org/download/) for instructions for your operating system.

1. Clone this project using your preferred method.

1. Change directory into this project then create and activate your virtual environment

    ```bash
    cd path/to/fccok_django
    python -m venv env

    # For Mac/Linux
    source env/bin/activate
    # For Windows (Powershell)
    .\env\Scripts\Activate.ps1
    # For Windows (CMD)
    .\env\Scripts\activate.bat
    ```

1. Install project dependencies

    ```bash
    pip install -r requirements.txt
    ```

1. Make a copy of `sample.env` and rename it to `.env`. Replace all values for local development.

1. Run migrations then start the server (make sure virtual environment is active)

    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

1. View site at [http://127.0.0.1:8000/postsocial](http://127.0.0.1:8000/postsocial). If you have trouble connecting, try replacing 127.0.0.1 with `localhost`.
