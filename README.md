# StockServer

## Env

- Ubuntu 16

## Install

- Python3.5.2
- Pyenv
- virtualenv
- Flask

## Todo - Install Env

- [x] Install Git
- [x] Install pyenv
	- [x] 3.5.2
	- [x] virtualenv `FlaskEnv`
- [x] [Flask](http://www.jianshu.com/p/84978157c785)
	- [x] Setting
- [x] uWSGI
	- [x] Setting
	- $ uwsgi config.ini
- [x] nginx
	- [x] Setting - [x] Issue : Can't restart
		- The `/etc/nginx/site.../default` has some problem
		- example: add symbol on end `;`
- [x] Supervisor
	- [x] Setting
	- [x] work unknow

## Using Command 

Install package:

	$ pip install -r requirements.txt

run uwsgi:

	$ uwsgi config.ini

on Browser : `127.0.0.1:9191`


