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

### Deploy notes tmp ###
Move the nginx conf to /etc/nginx/sites-available/, then run:
```
cd ../sites-enabled
sudo ln -s ../victorciurana.com .
```

Move gunicorn conf:
```
mv deploy_tools/gunicorn-systemd.template.service /etc/systemd/system/gunicorn-victorciurana.com.service
sudo systemctl daemon-reload
sudo systemctl enable gunicorn-victorciurana.com
sudo systemctl start gunicorn-victorciurana.com
```

Check all ok:
```
sudo journalctl -u gunicorn-victorciurana.com
```

Reload nginx:
```
sudo systemctl reload nginx
```

For reloading the app after any change:
```
sudo systemctl restart gunicorn-victorciurana.com
```

Follow [this post](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-20-04) on how to put https.


### TODO ###
TODO:
* Deploy still on workings
https://testdriven.io/blog/django-lets-encrypt/