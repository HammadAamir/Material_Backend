echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
python3 manage.py loaddata superuser_data.json
echo "BUILD END"