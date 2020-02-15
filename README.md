## Local Settings
The file `AMS/local_settings.py` contains the settings you need for your local environment. It may contain database settings or debug settings.

## Custom Error Pages
To render custom error pages, `DEBUG` must be set to `False` in `settings.py` (`local_settings.py` preferred). If there is a problem loading static content, use `python manage.py runserver --insecure`.