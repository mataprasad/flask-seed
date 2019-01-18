# For first time

0) apt-get update \
   apt-get install -y python3 python-dev python3-pip python-virtualenv libpq-d
   update-alternatives --remove python /usr/bin/python2.7

1) python -m virtualenv venv

2) source venv/bin/activate

3) git clone https://github.com/mataprasad/flask-seed.git

4) pip install -r requirements.txt

# To Run

1) source .env
2) ./run.sh