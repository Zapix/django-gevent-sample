django-gevent-sample
==================

Simple django socketio application based on gevent


Setup application
-----------------

Configure ubuntu with required libs

```sh
    $ sudo apt-get install -y python-pip
    $ sudo apt-get install -y python-dev
    $ sudo apt-get install -y libevent-dev
    $ sudo apt-get install -y libzmq-dev
```

Setup virtual env & install requirements.txt

```sh
    $ mkvirtualenv testapp
    $ pip install -r requirements.txt
```

Start application
-----------------

Start generator on console

```sh
    $ cd geventsample
    $ ./manage.py genrandom
```

Start server on another tab

```sh
   $ ./run.py
```

open in browser http://127.0.0.1:8000/
