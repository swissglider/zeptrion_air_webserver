# sudo pip3 install virtualenv
# sudo apt-get install python-virtualenv
virtualenv venv
. venv/bin/activate


$VENV/bin/pip install -e .

export FLASK_APP=main.py

flask run
