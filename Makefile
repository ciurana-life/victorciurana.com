ENV = env/bin/
PIP = $(ENV)pip
MANAGE = $(ENV)python3 manage.py

local_install:
	@echo "Starting local install..."
	python3 -m venv env
	$(PIP) install -r requirements.txt
	echo "DEBUG=True" >> .env
	$(MANAGE) collectstatic --no-input
	$(MANAGE) makemigrations
	$(MANAGE) makemigrations blog
	$(MANAGE) migrate
	@echo "local_install ended, you can now run: make local_run"

local_run:
	$(MANAGE) runserver

secret:
	$(ENV)python3 -c "import secrets; print(f'SECRET_KEY={secrets.token_urlsafe(100)}')" >> .env

server_install:
	@echo "Server install"

server_update:
	git pull
	$(MANAGE) makemigrations
	$(MANAGE) makemigrations blog
	$(MANAGE) migrate
	sudo systemctl restart gunicorn-victorciurana.com
