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
* Tox, and write how to run tests with it and pytest
* Create Makefile for all the commands and deployment
* Change this file with all the new data:
    - ci, tests, etc, new requirements files
* makefile needs to create .env file with DEBUG on local install

