echo "BUILD START"
python3.9 -m venv env
source env/bin/activate
pip install --upgrade pip
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD END"