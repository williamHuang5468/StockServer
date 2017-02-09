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
- [ ] 登入
    - 去 SQL 找使用者
	- [ ] has user
	- [ ] has not user
    - Session
- [ ] 註冊
    - 去 SQL 新增使用者
	- [ ] check_user_exist
	- [ ] create_user
- [ ] 登出
    - 清 Session
- [ ] SQL
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

## Using Command 

Install package:

	$ pip install -r requirements.txt

run uwsgi:

	$ uwsgi config.ini

on Browser : `127.0.0.1:9191`

## Feature

- 亂數加料雜湊加密法


