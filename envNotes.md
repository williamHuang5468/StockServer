# envNotes

## Ubuntu16

Step

- Install Git
- Install pyenv

### Install Git

	sudo apt install git

Meet problem

- [Unable to lock admin](http://askubuntu.com/questions/15433/unable-to-lock-the-administration-directory-var-lib-dpkg-is-another-process)

### Install pyenv

- [Tut](http://blog.codylab.com/python-pyenv-management/)

Issue : `pyenv command not found`

follow `Tut` step, and restart terminal.

- curl `command`
- add three code to `~/.Bashrc`
- restart terminal.

Using `pyenv`

- $ pyenv version # check version
- $ pyenv install `version number`(eg. `3.5.2`)
- pyenv status
	- $ pyenv global
	- $ pyenv local
	- $ pyenv shell

Using `pyenv-virtualenv`

- add a virtualenv `flaskEnv`
	- $ $ pyenv virtualenv flaskEnv

In this local check the setting

- $ pyenv local flaskEnv 

Change to the virtualenv

- $ source /home/william/.pyenv/versions/flaskEnv/bin/activate
	- Get the `(flaskEnv) william@ubuntu:~/Desktop/StockServer$`


### uwsgi

- (venv) $ pip install uwsgi
