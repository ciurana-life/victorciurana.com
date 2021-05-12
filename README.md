# README #

Project for [my blog](https://victorciurana.com).


### Prerequisites ###
You will need to search your Chromedriver for your chrome version and install it to be able to run the funcitonal tests. Also, you will need sudo.

Another thing to have in mind is that funcional tests won't run correctly if you dont run __collectstatic__, because selenium won't find some elements to click.


### How to run (local) ###
__The current Python version is 3.8.3__
Here is [a guide on how to install](https://tech.serhatteker.com/post/2019-12/how-to-install-python38-on-ubuntu/)

Create the environment and install the requirements:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

*create .env file with required variables*

Collect static:
```
./manage.py collectstatic --no-input
```

Migrations:
```
./manage.py makemigrations
./manage.py migrate
```

Run the project with:
```
./manage.py runserver
```

If you want to edit the styles run this in another terminal at the same time:
```
./manage.py sass static/sass/ templates/static/css/ --watch -t compressed
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
* Make changes so that my server still runs the code and serves the page.
* Specify how to run with make, and how to istall make.
* Make needs the sass command for developing.
* Docker prod configuration
* REST

### TMP changing to poetry ###
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

Now you can run a make command that will do the intial settings:
```
make local_install
```

Finally you can run the development server with:
```
make local_run
```
