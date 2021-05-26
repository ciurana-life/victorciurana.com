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
D_MANAGE = docker-compose exec web python manage.py
d_local_install:
	@echo "${GREEN}[#] STARTING LOCAL DOCKER INSTALL${RESET}"
	chmod +x entrypoint.sh
	docker-compose build
	docker-compose up -d --build
	$(D_MANAGE) makemigrations
	$(D_MANAGE) makemigrations blog
	$(D_MANAGE) migrate --noinput
	$(D_MANAGE) createsuperuser --noinput
	@echo "${GREEN}[#] Docker is up and running${RESET}"
	@echo "${GREEN}[#] An admin user was created:${RESET}"
	@echo "${GREEN}[#]     user: asuka${RESET}"
	@echo "${GREEN}[#]     password: eva02${RESET}"
	@echo "${GREEN}[#] You can now go to http://127.0.0.1:8000${RESET}"

d_scss:
	$(D_MANAGE) sass static/sass/ templates/static/css/ --watch -t compressed

d_test:
	docker-compose exec web pytest --cache-clear --black app --flake8

d_local_remove:
	@echo "${RED}[#] REMOVING LOCAL DOCKER INSTALL${RESET}"
	docker-compose down -v
	@echo "${RED}[#] The local Docker project was removed${RESET}"

d_prod_install:
	@echo "${GREEN}[#] STARTING RPOD DOCKER INSTALL${RESET}"
	docker pull nginx:1.19.0-alpine
	export CLOUDSDK_PYTHON=python3
	chmod +x entrypoint.prod.sh
	docker pull eu.gcr.io/victor-ciurana-com/victorciuranacom_web:latest
	docker pull eu.gcr.io/victor-ciurana-com/victorciuranacom_nginx-proxy:latest
	# docker-compose -f docker-compose.prod.yml pull
	docker-compose -f docker-compose.prod.yml up -d --force-recreate --remove-orphans
	# OPT error
	# $(D_MANAGE) makemigrations
	$(D_MANAGE) migrate --noinput
	$(D_MANAGE) createsuperuser --noinput
	$(D_MANAGE) collectstatic --noinput
	@echo "${GREEN}[#] Docker is up and running${RESET}"
	@echo "${GREEN}[#] An admin user was created:${RESET}"
	@echo "${GREEN}[#]     user: asuka${RESET}"
	@echo "${GREEN}[#]     password: eva02${RESET}"
	@echo "${GREEN}[#] You can now go to http://victorciurana.com${RESET}"

d_prod_remove:
	@echo "${RED}[#] REMOVING PROD DOCKER INSTALL${RESET}"
	docker-compose -f docker-compose.prod.yml down -v
	@echo "${RED}[#] The prod Docker project was removed${RESET}"


docker_pull:
	export CLOUDSDK_PYTHON=python3
	docker pull eu.gcr.io/victor-ciurana-com/victorciuranacom_web:latest
	docker pull eu.gcr.io/victor-ciurana-com/victorciuranacom_nginx-proxy:latest
	# docker-compose -f docker-compose.prod.yml pull
	docker-compose -f docker-compose.prod.yml up -d --force-recreate --remove-orphans
	docker system prune -af

	docker ps

### Commands to run without docker ###
MANAGE = poetry run ./manage.py
local_install:
	@echo "Starting local install..."
	$(MANAGE) collectstatic --no-input
	$(MANAGE) makemigrations
	$(MANAGE) makemigrations blog
	$(MANAGE) migrate
	@echo "local_install ended, ${GREEN}you can now run: make local_run${RESET}"

local_run:
	$(MANAGE) runserver
