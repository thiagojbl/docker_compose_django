pip install --upgrade pip
pip install -r requirements.txt
useradd thiago
chown -R thiago:thiago /code/docker_compose_django
chown -R thiago:thiago /code/manage.py
python manage.py runserver 0.0.0.0:8000 