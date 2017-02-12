pip install virtualenvwrapper
export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh

pip install virtualenwrapper-win

mkvirtualenv venv

workon venv

deactivate

rmvirtualenv venv

BASE DE DATOS

sudo -su postgres
createdb ehealt_database

psql -U postgres -d ehealth_database
create user "ehealth_user" with password 'ehealth123'
grant all privileges on database "ehealth_database" to "ehealth_user"

sudo pip install django==1.10
