# StockServer

## Use it

	1. $ source venv/bin/activate

	2. $ python manage.py

	3. $ uwsgi --socket 127.0.0.1:8080 --protocol=http -w manage:app

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
- [x] 登入
    - 去 SQL 找使用者
	- [x] has user
	- [x] has not user
    - Session
- [x] 註冊
    - 去 SQL 新增使用者
	- [x] check_user_exist
	- [x] create_user
- [x] 登出
    - 清 Session
- [x] SQL
    - [x] [Install PostgreSQL](https://www.fullstackpython.com/blog/postgresql-python-3-psycopg2-ubuntu-1604.html)
    - [x] [Psycopg](http://initd.org/psycopg/docs/index.html)
    - [x] 建立表格
        - User
            - Username
            - Password
            - Salt
    - [x] create
            - [x] user
            - [x] table
- send data by json

## Millstone

- [x] Function
	- [x] Login
	- [x] Logout
	- [x] Register
- [x] SQL
	- table
	- command

## Using Command

Install package:

	$ pip install -r requirements.txt


run uwsgi:

	$ uwsgi --socket 127.0.0.1:8080 --protocol=http -w manage:app


	> not to use it "$ uwsgi config.ini" # it can't work

on Browser : `127.0.0.1:9191`

## Feature

- 亂數加料雜湊加密法
