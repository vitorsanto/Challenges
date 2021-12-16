#Makefile

test: venv
    # Run REST application test suit
	$(VENV)/pytest

run: venv
    # Run REST application notebook
	$(VENV)/python manage.py migrate
	$(VENV)/python manage.py runserver

include Makefile.env