# gargnotes
The code for the gargnotes.heroku.com

Here is the code of my website- gargnotes.heroku.com

The site runs on django framework, so the server is running python.
Specifications are:
  Django-1.7.4
  Python-2.7.4
When you clone the repository, take care to comment out #DATABASES['default'] = dj_database_url.config() in settings.py
and run python manage.py migrate to create the database,
also run python manage.py createsuperuser to use admin.
There is still some work remaining in the project.
Like adding tags, providing better sharing in posts.

Read docs.djangoproject.com/en/1.7 for understanding how django works.
