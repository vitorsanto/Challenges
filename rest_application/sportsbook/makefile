#Makefile

run: venv
    # Run REST application notebook
	$(VENV)/python manage.py migrate
	$(VENV)/python manage.py runserver

include Makefile.env