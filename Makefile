ENV = env/bin/
PIP = $(ENV)pip
MANAGE = $(ENV)python3 manage.py

# Define colors
ifneq (,$(findstring xterm,${TERM}))
	RED          := $(shell tput -Txterm setaf 1)
	GREEN        := $(shell tput -Txterm setaf 2)
	RESET := $(shell tput -Txterm sgr0)
else
	RED          := ""
	GREEN        := ""
	RESET        := ""
endif

# You can use colors like this:
# @echo "${RED}RED${RESET}"

### Easy to use Docker commands ###

d_local_install:
	@echo "${GREEN}[#] STARTING LOCAL DOCKER INSTALL${RESET}"
	chmod +x entrypoint.sh
	docker-compose build
	docker-compose up -d --build
	docker-compose exec web python manage.py makemigrations
	docker-compose exec web python manage.py makemigrations blog
	docker-compose exec web python manage.py migrate --noinput
	docker-compose exec web python manage.py createsuperuser --noinput
	@echo "${GREEN}[#] Docker is up and running${RESET}"
	@echo "${GREEN}[#] An admin user was created:${RESET}"
	@echo "${GREEN}[#]     user: asuka${RESET}"
	@echo "${GREEN}[#]     password: eva02${RESET}"
	@echo "${GREEN}[#] You can now go to http://127.0.0.1:8000${RESET}"

d_local_remove:
	@echo "${RED}[#] REMOVING LOCAL DOCKER INSTALL${RESET}"
	docker-compose down -v
	@echo "${RED}[#] The local Docker project was removed${RESET}"

d_prod_install:
	@echo "${GREEN}[#] STARTING RPOD DOCKER INSTALL${RESET}"
	docker pull nginx:1.19.0-alpine
	chmod +x entrypoint.prod.sh
	docker-compose -f docker-compose.prod.yml build
	docker-compose -f docker-compose.prod.yml up -d --build
	docker-compose exec web python manage.py migrate --noinput
	docker-compose exec web python manage.py createsuperuser --noinput
	docker-compose exec web python manage.py collectstatic --noinput
	@echo "${GREEN}[#] Docker is up and running${RESET}"
	@echo "${GREEN}[#] An admin user was created:${RESET}"
	@echo "${GREEN}[#]     user: asuka${RESET}"
	@echo "${GREEN}[#]     password: eva02${RESET}"
	@echo "${GREEN}[#] You can now go to http://127.0.0.1:1337${RESET}"

d_prod_remove:
	@echo "${RED}[#] REMOVING PROD DOCKER INSTALL${RESET}"
	docker-compose -f docker-compose.prod.yml down -v
	@echo "${RED}[#] The prod Docker project was removed${RESET}"

ENVPROD = .envs/.prod/.env.prod
ENVPRODTMP = $(ENVPROD).tmp
ENVPROD_DB = .envs/.prod/.env.prod.db
ENVPRODTMP_DB = $(ENVPROD_DB).tmp
decrypt_env:
	@echo "${GREEN}[#] DECRYPTING ENV FILES"
	sops --decrypt $(ENVPROD) >> $(ENVPRODTMP) && rm $(ENVPROD) && mv $(ENVPRODTMP) $(ENVPROD)
	sops --decrypt $(ENVPROD_DB) >> $(ENVPRODTMP_DB) && rm $(ENVPROD_DB) && mv $(ENVPRODTMP_DB) $(ENVPROD_DB)

GCPKEY = projects/victor-ciurana-com/locations/global/keyRings/victorciurana-keyring/cryptoKeys/victorciuranacom-key
encrypt_env:
	@echo "${GREEN}[#] ENCRYPTING ENV FILES"
	sops --encrypt --gcp-kms $(GCPKEY) $(ENVPROD) > $(ENVPRODTMP) && rm $(ENVPROD) && mv $(ENVPRODTMP) $(ENVPROD)
	sops --encrypt --gcp-kms $(GCPKEY) $(ENVPROD_DB) > $(ENVPRODTMP_DB) && rm $(ENVPROD_DB) && mv $(ENVPRODTMP_DB) $(ENVPROD_DB)

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
	$(PIP) install -r requirements.txt
	$(MANAGE) makemigrations
	$(MANAGE) makemigrations blog
	$(MANAGE) migrate
	sudo systemctl restart gunicorn-victorciurana.com
