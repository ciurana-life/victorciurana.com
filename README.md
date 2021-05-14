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

## Server install (GCP) ##
Clone repo:
```
git clone https://github.com/ciurana-life/victorciurana.com.git
```
Install make (or google how to on your OS):
```
sudo apt-get install build-essential
```
Run:
```
cd victorciurana.com/
# Follow terminal instructions
make d_prod_install_all
```

## DOCKER how to push images ##

Tag SOURCE_IMAGE (name | id):
```
docker tag SOURCE_IMAGE eu.gcr.io/victor-ciurana-com/NAME_FOR_REGISTRY
```

Push:
```
docker push eu.gcr.io/victor-ciurana-com/NAME_FOR_REGISTRY
```

Make sure it uploaded (from cloud console | cloud.google.com):
```
gcloud container images list-tags eu.gcr.io/victor-ciurana-com/NAME_FOR_REGISTRY
```

On the VM pull it:
```
docker pull eu.gcr.io/victor-ciurana-com/NAME_FOR_REGISTRY:latest
```
