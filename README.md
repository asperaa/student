# student

It is a simple web application which is built using django framework.It majorly consists of two web pages.First one is a simple form to take
input from user about student_name,age and gender.The other web-page shows the table about all the students whose name have been
entered through the form

## Getting Started

This repository can be copied to your local machine using the following command.

```
git clone https://github.com/asperaa/student.git
```


### Prerequisites

Following packages/softwares a needed to run the webapp on your local machine

```
dj-database-url==0.5.0
Django==2.0.9
django-crispy-forms==1.7.2
gunicorn==19.9.0
psycopg2==2.7.6.1
pytz==2018.7
whitenoise==4.1.1

```


### Installing

Use the following command in your linux command line to move into your project

```
cd student
```

There is requirements.txt file the student directory which contains all the dependencies of the project.All those dependencies
can be installed using the following command:

```
pip install -r requirements.txt 
```

Do the following changes in the settings.py file

```
Comment out the postgresql database part(line 90)
Uncomment the sqlite3 database part(line 80)
```


Type the following commands to run the server on your local machine:

```
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```


