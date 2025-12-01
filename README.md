# Hotel-Booking-Management-Django-DRF with Core Python, Django, and Django REST Framework (DRF).
Hotel booking management with Django & DRF


Customer
username - admin
password - admin

Manager
username - ashish@41
password - testpassword123


# Tech Stack:
- Backend: Django, Django REST Framework (DRF)
- Language: Python 3.x
- Database: SQLite (default, can switch to PostgreSQL/MySQL)
- Frontend: HTML, CSS, JavaScript (Django Templates)
- Environment: Virtual Environment (venv)


# Step to do for Djanog DRF project : 
- Follow these steps to set up and run your Django DRF project successfully
- Make sure Python is installed: python --version
- If not, download it from https://www.python.org/downloads/

1. first create envirnoment before everything
   ❯ python3 -m env myenv
   activate environment: source myenv/bin/active

2. check versions
   ❯ python3 --version
    ❯ python3 -m django --version

3. Then install Django using pip:
   ❯ pip install django

4. Create a New Django Project
   ❯ django-admin startproject "project_name"
   
5. Navigate into the project folder:
   ❯ cd myproject
   
6. Run the server:
   ❯ python manage.py runserver

7. Now visit:
   ❯ http://127.0.0.1:8000/
   (You’ll see the “Django Welcome Page”)

8. Create a Django App
    ❯ python manage.py startapp "app_name"

9. Add the App_name to settings.py

10.  Create a View
    - views.py

11. Add a URL for the View
    - urls.py
    - Then connect your app’s urls.py to the main project’s urls.py:

12. Now visit:  http://127.0.0.1:8000/
 ( You’ll see your on web page)

13. Create Models (Database Tables)
    - models.py
   
15. Apply Migrations :
    ❯ python manage.py makemigrations
    ❯ python manage.py migrate
      
16.  Create Admin Superuser
    ❯ python manage.py createsuperuser

17.  Register Models in Admin
    - admins.py

18. Run your server again:
   ❯ python manage.py runserver

19. Now visit: http://127.0.0.1:8000/admin/
   - (Login with your superuser credentials.)

19.  Add Templates (HTML Files)

