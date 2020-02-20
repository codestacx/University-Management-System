## Getting Started
### Installation

1. Install Python 3.
2. Make sure you are in the project directory, then install project dependencies by running:

    `pip install -r requirements.txt`

3. Install (if not already) and run MySQL. Connect it with this project in `settings.py`.

### Running

1. Make sure you are in the project directory, then run:

    `python manage.py runserver`

## Local Settings
The file `AMS/local_settings.py` contains the settings you need for your local environment. It may contain database settings or debug settings.

## Custom Error Pages
To render custom error pages, `DEBUG` must be set to `False` in `settings.py` (`local_settings.py` preferred). If there is a problem loading static content, use `python manage.py runserver --insecure`.