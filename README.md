# README #

Project for [my blog](https://victorciurana.com).

## How to install and run (easy way) ##
Before you start make sure you have the following prerequisites:
1. Docker, [download](https://docs.docker.com/engine/install/) and install for your os.
2. Make:
    - On OSX -> ```brew install make```
    - On Ubuntu -> ```sudo apt-get install build-essential```
    - Other linux -> Google it ;)
3. Sops:
    ```
    curl -j -O -L https://github.com/mozilla/sops/releases/download/v3.7.1/sops_3.7.1_amd64.deb
    apt install ./sops_3.7.1_amd64.deb
    rm ./sops_3.7.1_amd64.deb
    ```


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
