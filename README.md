# CS162_Database_Application

## Introduction

A full fledged application that meets all assignment requirements specified here: https://github.com/Chrecci/cs162/blob/master/assignments/4_database.md.

This application is built using Django REST Framework, exposing an api for frontend use. Thus, if a company wanted to use this service and build out an interative user interface using React, for example, they have the full flexibility of doing so. I believe this app goes above and beyond what was required in many ways, and I want to justify both the why and how it does so. I decided to use Django for a number of reasons. The first being, I figured I could get extra practice for my own skill development, and secondly, it provides a powerful ORM and extensions that allow me to efficiently develop the database capacities for this project. Lastly, if a real estate company really told me to build something like this, I would need it to be usable enough for most people to access. Django's REST Framework provides exactly that. I don't have a react frontend built out right now, but if I wanted to, I would be very glad I put in this extra work at this stage.

## Setup

The project as is, is configured for a docker setup. For local setup, please see warning to change HOST in settings.

I HIGHLY suggest either using only a local setup or docker. Inter-mixing will mess up your postgres connection, and unless you're really good at this stuff I don't suggest you do it. It normally should be ok (just make sure you consistently change localhost vs postgres_db in settings databases HOST) but if things are messed up with postgres connection, a simple restart of your device should be fine.

### Virtual Environment
*If you're reading from direct README.md file, don't forget to ignore br (newline) tags*

```
py -3 -m venv <name_of_environment> 
```
```
<name_of_environment>\Scripts\activate
```

### Local

If you already have postgres installed and working, this way is probably faster:

Make sure HOST in real_estate/real_estate_db/settings.py line 89 is set to "localhost"

1. Install and setup postgres. Create a database called "real_estate_app_db". For help, see here: https://www.youtube.com/watch?
v=uoJjDbL-Y_E
3. Install requirements.txt after entering virtual environment (see above)
```bash
pip install -r requirements.txt
```
2. enter real_estate directory:
```bash
cd real_estate
```
4. Make migrations
```bash
python manage.py makemigrations
```
5. Migrate
```bash
python manage.py migrate
```
6. Run app. Should be accessible at http://localhost:8000
```bash
python manage.py runserver
```
### Docker-Compose

Make sure HOST in real_estate/real_estate_db/settings.py line 89 is set to "postgres_db"

1. Install Docker for you device
2. In a bash terminal at root of project, run the following. This might take a minute or so. When completed will exit terminal
```bash
docker-compose build
```
3. Let this load and run in background
```bash
docker-compose up
```
4. In a new bash terminal run the following. It should open a terminal to engage with Django app
```bash
docker exec -it real_estate bash
```
5. 
```bash
python manage.py makemigrations
```
6. 
```bash
python manage.py migrate
```
7. Going back to previous terminal, pres CTRL+C to exit "docker-compose up" job
8. Reload by running "docker-compose up" again
9. You should be able to open app at http://localhost:8000 

### Django API

For any of the models, by visiting http://localhost:8000/api/<name_of_model> you can access a form that allows you to post and create objects. You can even select foreign key objects if they are already created. It is using these endpoints that a frontend application will be able to communicate with our application. Feel free to submit information here and see that the entries show up in your postgres database. This is how you know everything is set up correctly. (Note: the uuid field does not need to be filled out, it does so automatically)

### django-admin

There is a django-admin page but its incredibly rudimentary right now. However, if you'd like to access the admin page (visitable at http://localhost:8000/admin):

```bash
python manage.py createsuperuser
```

Follow the prompt to create superuser. Then, simply log in at http://localhost:8000/admin . This is another powerful tool that a team or company would likely be interested in. It's a fully customizable interface with our database, allowing us to add, delete, edit entries. Realistically, if we wanted to create a new house listing; it's highly unlikely we would want to run a SQL command or create a models object. Instead, it is much more practical to do so here.

### Test

This is where the actual assignment requirements are completed. These files can all be found in real_estate/scripts. Not only is the basic assignment requirements met fully (every query is successful), but the project takes many extra steps to ensure the meta-task of making something usable is achieved, at least to a decent extent.

1. Insert all test data:
```
python manage.py shell<scripts/insert.py
```
2. Update data (automatically updates commission fees, selling date etc.):
```
python manage.py shell<scripts/update.py
```
3. Query data (questions proposed in assignment instructions):
```
python manage.py shell<scripts/query.py
```

### Important notes

At some point, you may or may not have to run the following command, if you see errors related to DJANGO_SETTINGS_MODULE

```
export DJANGO_SETTINGS_MODULE=real_estate_db.settings
```

To delete all data in tables and restart:
```
python manage.py flush
```
