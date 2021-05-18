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

### Encrypt and decrypt commands for secret variables (call from d_prod_install) ###
ENVPROD = .envs/.prod/.env.prod
ENVPRODTMP = $(ENVPROD).tmp
ENVPROD_DB = .envs/.prod/.env.prod.db
ENVPRODTMP_DB = $(ENVPROD_DB).tmp
decrypt_env:
	@echo "${GREEN}[#] DECRYPTING ENV FILES"
	sops --decrypt $(ENVPROD) >> $(ENVPRODTMP) && rm $(ENVPROD) && mv $(ENVPRODTMP) $(ENVPROD)
	sops --decrypt $(ENVPROD_DB) >> $(ENVPRODTMP_DB) && rm $(ENVPROD_DB) && mv $(ENVPRODTMP_DB) $(ENVPROD_DB)
	@echo "-- ${RESET}"

GCPKEY = projects/victor-ciurana-com/locations/global/keyRings/victorciurana-keyring/cryptoKeys/victorciuranacom-key
encrypt_env:
	@echo "${GREEN}[#] ENCRYPTING ENV FILES"
	sops --encrypt --gcp-kms $(GCPKEY) $(ENVPROD) > $(ENVPRODTMP) && rm $(ENVPROD) && mv $(ENVPRODTMP) $(ENVPROD)
	sops --encrypt --gcp-kms $(GCPKEY) $(ENVPROD_DB) > $(ENVPRODTMP_DB) && rm $(ENVPROD_DB) && mv $(ENVPRODTMP_DB) $(ENVPROD_DB)
	@echo "-- ${RESET}"

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
	docker-compose exec web pytest --black app --flake8

d_local_remove:
	@echo "${RED}[#] REMOVING LOCAL DOCKER INSTALL${RESET}"
	docker-compose down -v
	@echo "${RED}[#] The local Docker project was removed${RESET}"

# RUN ONLY ON FRESH VM THAT HAS NOTHING (amd64 Debian buster)
# [1] Runs all the commands here: https://docs.docker.com/engine/install/debian/
#     to install Docker
# [2] Runs all the commands here: https://docs.docker.com/compose/install/
#     to install docker-compose
# [3] Logs in to gcloud
# [4] Install sops
d_prod_install_all:
	@echo "${GREEN}[# 1] Installing Docker... ${RESET}"
	sudo apt-get update
	sudo apt-get install \
		apt-transport-https \
		ca-certificates \
		curl \
		gnupg \
		lsb-release -y
	curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
	echo \
		"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
		buster stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	sudo apt-get update
	sudo apt-get install docker-ce docker-ce-cli containerd.io -y
	@echo "${GREEN}[# 1] Running Docker hello world ${RESET}"
	sudo docker run hello-world
	@echo "${GREEN}[# 1] If you saw the hello world, you are done :) ${RESET}"

	@echo "${GREEN}[# 2] Installing docker-compose ...${RESET}"
	sudo curl -L "https://github.com/docker/compose/releases/download/1.29.1/docker-compose-Linux-x86_64" -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose
	docker-compose --version
	@echo "${GREEN}[# 2] If you saw the docker-compose version, you are done :) ${RESET}"

	@echo "${GREEN}[# 3] Loging in to gcloud please follow terminal instructions ${RESET}"
	gcloud auth login
	gcloud auth application-default login
	gcloud auth configure-docker
	gcloud auth list
	@echo "${GREEN}[# 3] If you see yourself on the ACTIVE ACCOUNT your are done :) ${RESET}"

	@echo "${GREEN} [# 4] Installing sops ... ${RESET}"
	curl -j -O -L https://github.com/mozilla/sops/releases/download/v3.7.1/sops_3.7.1_amd64.deb
	apt install ./sops_3.7.1_amd64.deb
	rm ./sops_3.7.1_amd64.deb
	@echo "${GREEN} [# 4] Sops installed ${RESET}"

	@echo "If all is green and worked run 'make decrypt_env && make d_prod_install'"

d_prod_install:
	@echo "${GREEN}[#] STARTING RPOD DOCKER INSTALL${RESET}"
	docker pull nginx:1.19.0-alpine
	export CLOUDSDK_PYTHON=/usr/bin/python3
	chmod +x entrypoint.prod.sh
	docker-compose -f docker-compose.prod.yml pull
	docker-compose -f docker-compose.prod.yml up -d
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

docker_push:
	docker-compose -f docker-compose.prod.yml build
	docker-compose -f docker-compose.prod.yml push

docker_pull:
	export CLOUDSDK_PYTHON=/usr/bin/python3
	docker-compose -f docker-compose.prod.yml pull
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
