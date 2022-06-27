# youtube-api


- Terminal Commands to run the server:
1) python3 -m venv venv
2) source venv/bin/activate  #(On Windows use `venv\Scripts\activate`)
3) python manage.py migrate  #(since, I am uploading my migrations too so there is no need to run makemigrations command again.)
4) python manage.py runserver

- Commands I've used during developement: (Devlogs)

1) sudo apt install python3-venv
2) python3 -m venv venv
3) source venv/bin/activate
4) pip install django
5) pip install djangorestframework
6)django-admin startproject backend .
7) cd backend
8) django-admin startapp api
9) cd ..
10) python manage.py migrate
11) python manage.py createsuperuser --email admin@example.com --username admin (Set password in this step)
12) python manage.py runserver (to test if everything is fine.)


// added my first commit
13) git add .
14) git commit -m "setup project youtube-api"
15) git push origin master

// after this I have started to add the requested api in the follow up commmits.

# References

1) Django-rest Framework: https://www.django-rest-framework.org/tutorial/quickstart/
2) YouTube data v3 API: https://developers.google.com/youtube/v3/getting-started
3) Search API reference: https://developers.google.com/youtube/v3/docs/search/list
