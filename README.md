# SyntacticAI


This is a project given for by SyntaticAI during a placement-drive held at our colleg University Visvesvaraya College of Engineering.
This repo contains a proxy web server project created using Django, Gunicorn, Nginx and PostGRESQL.
I have used Django alongside Gunicorn and Nginx to create a secure WSGI gateway and the web server can hosted as a production-ready server. I was able to host it on my localhost.

I am a beginner python developer and I could at the best of my abilties do this project to my level of understanding.
i was not able to successfully complete it and hence I am submmitting whatever i ahve completed with the limited time I had to work with,since there has been a covid case in my family I have had only 24 hours to build this project upto this point.
I thank the company for the oppurtunity of letting me expand my knowledge with this project.


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

Create a virtual environment for the project:
>```sudo -H pip3 install --upgrade pip```
>```sudo -H pip3 install virtualenv```

With virtualenv installed, we can start forming our project. Create and move into a directory where we can keep our project files:
>```mkdir ~/myproject```
>```cd ~/myproject```

Within the project directory, create a Python virtual environment by typing:
>```virtualenv myprojectenv```

This will create a directory called myprojectenv within your myproject directory. Inside, it will install a local version of Python and a local version of pip. We can use this to install and configure an isolated Python environment for our project.

Before we install our project’s Python requirements, we need to activate the virtual environment. You can do that by typing:
>```source myprojectenv/bin/activate```

With your virtual environment active, install Django, Gunicorn, and the psycopg2 PostgreSQL adaptor with the local instance of pip:
>```pip install django gunicorn psycopg2```

Create a new Django Project:
>```django-admin.py startproject myproject ~/myproject```

At this point, your project directory (~/myproject in our case) should have the following content:

~/myproject/manage.py: A Django project management script.
~/myproject/myproject/: The Django project package. This should contain the __init__.py, settings.py, urls.py, and wsgi.py files.
~/myproject/myprojectenv/: The virtual environment directory we created earlier.
Adjust the Project Settings
The first thing we should do with our newly created project files is adjust the settings. Open the settings file in your text editor:

>```nano ~/myproject/myproject/settings.py```
 
Start by locating the ALLOWED_HOSTS directive. This defines a list of the server’s addresses or domain names may be used to connect to the Django instance. Any incoming requests with a Host header that is not in this list will raise an exception. Django requires that you set this to prevent a certain class of security vulnerability.

In the square brackets, list the IP addresses or domain names that are associated with your Django server. Each item should be listed in quotations with entries separated by a comma. If you wish requests for an entire domain and any subdomains, prepend a period to the beginning of the entry. In the snippet below, there are a few commented out examples used to demonstrate:

>```~/myproject/myproject/settings.py
. . .
The simplest case: just add the domain name(s) and IP addresses of your Django server
ALLOWED_HOSTS = [ 'example.com', '203.0.113.5']
To respond to 'example.com' and any subdomains, start the domain with a dot
ALLOWED_HOSTS = ['.example.com', '203.0.113.5']
ALLOWED_HOSTS = ['your_server_domain_or_IP', 'second_domain_or_IP', . . .]```
 
Next, find the section that configures database access. It will start with DATABASES. The configuration in the file is for a SQLite database. We already created a PostgreSQL database for our project, so we need to adjust the settings.

Change the settings with your PostgreSQL database information. We tell Django to use the psycopg2 adaptor we installed with pip. We need to give the database name, the database username, the database user’s password, and then specify that the database is located on the local computer. You can leave the PORT setting as an empty string:

~/myproject/myproject/settings.py
. . .

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

. . .
 
Next, move down to the bottom of the file and add a setting indicating where the static files should be placed. This is necessary so that Nginx can handle requests for these items. The following line tells Django to place them in a directory called static in the base project directory:

~/myproject/myproject/settings.py
. . .

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
 
Save and close the file when you are finished.

Complete Initial Project Setup
Now, we can migrate the initial database schema to our PostgreSQL database using the management script:

>```~/myproject/manage.py makemigrations```
>```~/myproject/manage.py migrate```
 
Create an administrative user for the project by typing:

>```~/myproject/manage.py createsuperuser```
 
You will have to select a username, provide an email address, and choose and confirm a password.

We can collect all of the static content into the directory location we configured by typing:

>```~/myproject/manage.py collectstatic```

Create an exception for port 8000 by typing:

>```sudo ufw allow 8000```
 
Finally, you can test our your project by starting up the Django development server with this command:

>```~/myproject/manage.py runserver 0.0.0.0:8000```
 
In your web browser, visit your server’s domain name or IP address followed by :8000:

http://server_domain_or_IP:8000
You should see the default Django index page:

Django index page

If you append /admin to the end of the URL in the address bar, you will be prompted for the administrative username and password you created with the createsuperuser command:

Django admin login

After authenticating, you can access the default Django admin interface:

Django admin interface

When you are finished exploring, hit CTRL-C in the terminal window to shut down the development server.

Testing Gunicorn’s Ability to Serve the Project
The last thing we want to do before leaving our virtual environment is test Gunicorn to make sure that it can serve the application. We can do this by entering our project directory and using gunicorn to load the project’s WSGI module:

>```gunicorn --bind 0.0.0.0:8000 myproject.wsgi```
 
This will start Gunicorn on the same interface that the Django development server was running on. You can go back and test the app again.

Note: The admin interface will not have any of the styling applied since Gunicorn does not know about the static CSS content responsible for this.

We’re now finished configuring our Django application. We can back out of our virtual environment by typing:

>```deactivate```
 
The virtual environment indicator in your prompt will be removed.

Create a Gunicorn systemd Service File

Create and open a systemd service file for Gunicorn with sudo privileges in your text editor:

>```sudo nano /etc/systemd/system/gunicorn.service```
 
Start with the [Unit] section, which is used to specify metadata and dependencies. We’ll put a description of our service here and tell the init system to only start this after the networking target has been reached:

/etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
After=network.target
 
Next, we’ll open up the [Service] section. We’ll specify the user and group that we want to process to run under. We will give our regular user account ownership of the process since it owns all of the relevant files. We’ll give group ownership to the www-data group so that Nginx can communicate easily with Gunicorn.

We’ll then map out the working directory and specify the command to use to start the service. In this case, we’ll have to specify the full path to the Gunicorn executable, which is installed within our virtual environment. We will bind it to a Unix socket within the project directory since Nginx is installed on the same computer. This is safer and faster than using a network port. We can also specify any optional Gunicorn tweaks here. For example, we specified 3 worker processes in this case:

/etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myproject
ExecStart=/home/sammy/myproject/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/sammy/myproject/myproject.sock myproject.wsgi:application
 
Finally, we’ll add an [Install] section. This will tell systemd what to link this service to if we enable it to start at boot. We want this service to start when the regular multi-user system is up and running:

/etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myproject
ExecStart=/home/sammy/myproject/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/sammy/myproject/myproject.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
 
With that, our systemd service file is complete. Save and close it now.

We can now start the Gunicorn service we created and enable it so that it starts at boot:

>```sudo systemctl start gunicorn```
>```sudo systemctl enable gunicorn```
 
We can confirm that the operation was successful by checking for the socket file.

Check for the Gunicorn Socket File
Check the status of the process to find out whether it was able to start:

>```sudo systemctl status gunicorn```
 
Next, check for the existence of the myproject.sock file within your project directory:

>```ls /home/sammy/myproject```
 
Output
manage.py  myproject  myprojectenv  myproject.sock  static
If the systemctl status command indicated that an error occurred or if you do not find the myproject.sock file in the directory, it’s an indication that Gunicorn was not able to start correctly. Check the Gunicorn process logs by typing:

>```sudo journalctl -u gunicorn```
 
Take a look at the messages in the logs to find out where Gunicorn ran into problems. There are many reasons that you may have run into problems, but often, if Gunicorn was unable to create the socket file, it is for one of these reasons:

The project files are owned by the root user instead of a sudo user
The WorkingDirectory path within the /etc/systemd/system/gunicorn.service file does not point to the project directory
The configuration options given to the gunicorn process in the ExecStart directive are not correct. Check the following items:
The path to the gunicorn binary points to the actual location of the binary within the virtual environment
The --bind directive defines a file to create within a directory that Gunicorn can access
The myproject.wsgi:application is an accurate path to the WSGI callable. This means that when you’re in the WorkingDirectory, you should be able to reach the callable named application by looking in the myproject.wsgi module (which translates to a file called ./myproject/wsgi.py)
If you make changes to the /etc/systemd/system/gunicorn.service file, reload the daemon to reread the service definition and restart the Gunicorn process by typing:

>```sudo systemctl daemon-reload```
>```sudo systemctl restart gunicorn```
 
Make sure you troubleshoot any of the above issues before continuing.

Configure Nginx to Proxy Pass to Gunicorn
Now that Gunicorn is set up, we need to configure Nginx to pass traffic to the process.

Start by creating and opening a new server block in Nginx’s sites-available directory:

>```sudo nano /etc/nginx/sites-available/myproject```
 
Inside, open up a new server block. We will start by specifying that this block should listen on the normal port 80 and that it should respond to our server’s domain name or IP address:

/etc/nginx/sites-available/myproject

server {
    listen 80;
    server_name server_domain_or_IP;
}
 
Next, we will tell Nginx to ignore any problems with finding a favicon. We will also tell it where to find the static assets that we collected in our ~/myproject/static directory. All of these files have a standard URI prefix of “/static”, so we can create a location block to match those requests:

/etc/nginx/sites-available/myproject

server {

    listen 80;
    server_name server_domain_or_IP;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sammy/myproject;
    }
}
 
Finally, we’ll create a location / {} block to match all other requests. Inside of this location, we’ll include the standard proxy_params file included with the Nginx installation and then we will pass the traffic to the socket that our Gunicorn process created:

/etc/nginx/sites-available/myproject

server {

    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sammy/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/sammy/myproject/myproject.sock;
    }
}
 
Save and close the file when you are finished. Now, we can enable the file by linking it to the sites-enabled directory:

>```sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled```
 
Test your Nginx configuration for syntax errors by typing:

>```sudo nginx -t```
 
If no errors are reported, go ahead and restart Nginx by typing:

>```sudo systemctl restart nginx```
 
Finally, we need to open up our firewall to normal traffic on port 80. Since we no longer need access to the development server, we can remove the rule to open port 8000 as well:

>```sudo ufw delete allow 8000```
>```sudo ufw allow 'Nginx Full'```
 
You should now be able to go to your server’s domain or IP address to view your application.

