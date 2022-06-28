# Youtube API

<br/>

- Terminal Commands to run both the Frontend and the Backend servers:
1) `python3 -m venv venv`  (After clonning the project, run this command in the root directory of the project)
2) `source venv/bin/activate`  (On Windows use `venv\Scripts\activate`)
3) `pip install -r requirements.txt`
4) `python manage.py migrate`  (Since I am uploading my migrations too, so there is no need to run `python manage.py makemigrations` command again.)
5) `cd react-frontend`
6) `npm i -f`
7) `cd ..`
8) `python manage.py runserver`  (to run the backend server at port 8000)
9) In seperate Terminal run: `cd react-frontend && npm start` (to start the front-end server at port 3000)

<br/><br/>

- Commands I've used during developement: (Devlogs)

1) `sudo apt install python3-venv`
2) `python3 -m venv venv`
3) `source venv/bin/activate`
4) `pip install django`
5) `pip install djangorestframework`
6) `django-admin startproject backend .`  (take care of the trailing `.`)
7) `cd backend`
8) `django-admin startapp api`
9) `cd ..`
10) `python manage.py migrate`
11) `python manage.py createsuperuser --email admin@example.com --username admin` (Set password in this step)
12) `python manage.py runserver` (to test if everything is fine.)
13) `git add .` 
14) `git commit -m "setup project youtube-api"`
15) `git push origin master`  --pushed my first commit

16) `pip install google-api-python-client django-cors-headers`
17) `npx create-react-app react-frontend`
18) `cd react-frontend`   (run npm start to test)
19) `npm i axios`
20) `npm install -f @material-ui/core @material-ui/icons @mui/material` (Since, material-ui 4.0 is not yet supported for React v17. In future we can remove '-f')


# References

1) Django-rest Framework: https://www.django-rest-framework.org/tutorial/quickstart/
2) YouTube data v3 API: https://developers.google.com/youtube/v3/getting-started
3) Search API reference: https://developers.google.com/youtube/v3/docs/search/list
4) Adding Filters in Django rest Framework: https://www.django-rest-framework.org/api-guide/filtering/
