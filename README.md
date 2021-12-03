# CS162_Database_Application

docker-compose build
docker-compose up
docker-compose exec -it real_estate bash
>>>python manage.py makemigrations
>>>python manage.py migrate
docker-compose up (after CTRL+C on first docker-compose up)
export DJANGO_SETTINGS_MODULE=real_estate_db.settings
python manage.py shell
>>> import real_estate_app.insert