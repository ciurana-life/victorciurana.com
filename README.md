# README #

Project for [my blog](https://victorciurana.com).

## How to install and run (easy way) ##
Before you start make sure you have the following prerequisites:
1. Docker, [download](https://docs.docker.com/engine/install/) and install for your os.
2. Make:
    - On OSX -> ```brew install make```
    - On Ubuntu -> ```sudo apt-get install build-essential```
    - Other linux -> Google it ;)

Now you can just run the following command that will do everything for you:
```
make d_local_install
```

If you want to edit the css run on a different terminal:
```
make d_scss
```

Run tests:
```
make d_test
```

Any other command that requires ./manage.py:
```
docker-compose exec web python manage.py YOUR_COMMANDS
```

For a list of all commands read the ```Makefile```.

## How to install and run (no Docker, no make) ##
You want it the hard way boy!

Prerequisites:
Install (poetry)[https://python-poetry.org/docs/#installation]
```
https://python-poetry.org/docs/#installation
```

Once you have poetry you have to open a shell and install the requirements:
```
poetry shell
poetry install
```

You can exit the shell with just ```exit```.
Now you can run normal manage commands with:
```
poetry run ./manage.py YOUR_COMMAND
```




### TODO ###
TODO:
* Deploy still on workings
https://testdriven.io/blog/django-lets-encrypt/

-- Staging delpoyment

```
docker-compose -f docker-compose.staging.yml up -d --build
```

Commands to put on the makefile after up
```
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py createsuperuser --noinput
docker-compose exec web python manage.py collectstatic --noinput
```

debug ```docker-compose logs```

bring it down
```
docker-compose -f docker-compose.staging.yml down -v
```

-- Production Install
**[1] - You need to decrypt the env files** use this commands:
```
gcloud auth login
gcloud auth application-default login
```
And make sure you have the keyring:
```
gcloud kms keys list --location global --keyring victorciurana-keyring
```

After that install sops
__(make sure you are sudo)__
__(put on make on d_prod_install):__
```
curl -j -O -L https://github.com/mozilla/sops/releases/download/v3.7.1/sops_3.7.1_amd64.deb
apt install ./sops_3.7.1_amd64.deb
rm ./sops_3.7.1_amd64.deb
```

Install ```make```(top of this file),and you can decrypt them with
__(put on make on d_prod_install):__
```
make decrypt_env
```

-- Production update
something like (to decide inside docker or not):
```
git checkout .envs/.prod/.env.prod
git checkout .envs/.prod/.env.prod.db
git pull
./manage.py makemigrations
```


-- You need to do nothing from above if you push the image
-- DOCKER how to push images

Tag SOURCE_IMAGE (name | id):
```
docker tag SOURCE_IMAGE eu.gcr.io/victor-ciurana-com/NAME_FOR_REGISTRY
```

Push:
```
docker push eu.gcr.io/victor-ciurana-com/NAME_FOR_REGISTRY
```

Make sure it uploaded (from cloud console):
```
gcloud container images list-tags eu.gcr.io/victor-ciurana-com/NAME_FOR_REGISTRY
```

On the VM pull it:
```
docker pull eu.gcr.io/victor-ciurana-com/NAME_FOR_REGISTRY:latest
```


--- Multi stage for otp or, create a nginx path to a different admin pannel,
that requires a nginx user and password

TODO:
1. Issue production certificate and change the prod.yml
2. Decrypt on server the .envs
3. Change the Makefile for server installing (something for the otp) and updating
    - Also the staging install and update
4. RESDIS cahcke at url level

production