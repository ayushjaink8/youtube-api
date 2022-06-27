# youtube-api


Terminal Commands:
1) python3 -m venv venv
2) source venv/bin/activate  #(On Windows use `venv\Scripts\activate`)
3) python manage.py migrate  #(since, I am uploading migrations too so no there is need to run makemigrations again.)



// Commands I've used during developement: 

sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install django
pip install djangorestframework
django-admin startproject backend .
cd backend
django-admin startapp api
cd ..
python manage.py migrate
python manage.py createsuperuser --email admin@example.com --username admin (Set password in this step)
python manage.py runserver (to test if everything is fine.)

git add .
git commit -m "setup project youtube-api"
git push origin master
