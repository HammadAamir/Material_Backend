echo "BUILD START"
uname -a
apt-get install pkg-config python3-dev default-libmysqlclient-dev build-essential
python3.9 -m venv env 
source env/bin/activate
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"