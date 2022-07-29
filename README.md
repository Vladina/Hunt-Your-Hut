# Hunt-Your-Hut
Property rental web site (graduation work)

## About this project
The Hunt Your Hut web site is intended to provide users with the possibility to find their perfect homes for rent in a location of their choice.


## Prerequisites

* Windows 10 x64
* PostgreSQL 13
* PgAdmin 4 v 2.29
* Pycharm Professional 2020.3

## Installation and setting up
1. Clone the project from: `https://github.com/Vladina/Hunt-Your-Hut.git`.
2. In PyCharm Professional, open the cloned project.
3. Create a virtual environment for the project. To do this, follow the steps provided below:
   
   a. Open **File**->**Settings**->**Project:TestDiploma**->**Python Interpreter**.
   
   b. In the **Python Interpreter** dialog, click the **Settings** icon, and then click **Add**.
   
   c. In the **Add Python Interpreter** dialog that appears, select **Virtual Environment**, and then click **OK**.
4. Make sure, that Django support is enabled for your project. To do this, in **Settings**->**Languages & Frameworks**, select **Django**, and then select the **Enable Django Support** check-box.
   After that, define Django project root (cloned project root), settings (TestDiploma\settings.py), and set folder pattern to track files (migrations).
   
5. Install the project dependencies: `pip install -r requirements.txt`.
6. Add project debug configuration:
   
   a. On the PyCharm toolbar, click **Add Configuration**.
   
   b. In the **Run/Debug Configuration** dialog that appears, click the **Add** icon (**+**), and then select **Django Server**.
   
   c. Enter a name for a new configuration, and then in the **Environment variables** field, add **DJANGO_SETTINGS_MODULE=TestDiploma.settings**. Click **OK**.
   
7. Create a psql database and a user:
   
   a. In **pgAmdin 4**, right-click **Login/Group Roles**, then click **Create**->**Login/Group** role.
   
   In the **Create Login/Group Role** dialog that appears, enter a name (for example: _admin_), password (for example: _11111_), and define membership (_postgres_) for a new user.
   
   Also, specify user privileges (we recommend you to set all privileges to **On**).
   
   b. Create a new database. Right-click **Databases**, select **Create**->**Database**. 
   
   In the **Create Database** dialog that appears, specify a name for a new database (for example: _mydb_) and owner (_admin_), and then click **Save**.

    
8. In **TestDiploma\settings.py**, set the database settings, as in the example below:
```
      DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': 'mydb',
           'USER': 'admin',
           'PASSWORD': '11111',
           'HOST': '127.0.0.1',
           'PORT': '5432',
       }
   }
```
9. Make migrations to connect to the created database. In PyCharm terminal, run:
   
   ```python manage.py makemigrations```

   ```python manage.py migrate```

10. Start the development server: `python manage.py runserver`. Open `http://127.0.0.1:8000/` on your browser to view the app.

11. Create a superuser to be able to fill in the database table with content. In PyCharm terminal, run:`python manage.py createsuperuser`
Enter superuser credentials. Make sure to remember them to be able to login to the _admin_ page.
    
12. On your web browser, open `http://127.0.0.1:8000/admin`, and feel free to add content to the database tables.

## Troubleshooting

###### I cannot apply migrations to the database

If you experience problems with applying migrations to the database, in PyCharm project tree, right-click the **vevn** root folder, and then click **Clean Python Compiled Files**.






