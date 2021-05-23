# SyntacticAI


This is a project given for by SyntaticAI during a placement-drive held at our colleg University Visvesvaraya College of Engineering.
This repo contains a proxy web server project created using Django, Gunicorn, Nginx and PostGRESQL.
I have used Django alongside Gunicorn and Nginx to create a secure WSGI gateway and the web server can hosted as a production-ready server. I was able to host it on my localhost.
I used the following steps to host the webserver on my local machine:

First we  check if our system is up to date :
>```sudo apt-get update```

Next we install the following requirements : 
>```sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx```

Log into interactive session of PostGRESQL:
>```sudo -u postgres psql```

Create your database for the project:
>```CREATE DATABASE myproject;```

Next, create a database user for our project. Make sure to select a secure password:
>```CREATE USER myprojectuser WITH PASSWORD 'password';```

Tweak a few of the default settings:
>```ALTER ROLE myprojectuser SET client_encoding TO 'utf8';```
>```ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';```
>```ALTER ROLE myprojectuser SET timezone TO 'UTC';```

Now, we can give our new user access to administer our new database:
>```GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;```

Exit by typing:
>```\q```
