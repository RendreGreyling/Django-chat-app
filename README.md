# Django-chat-app

Simple Django chat room application to demonstrate realtime message sending and recieving using channels and websockets.

## Getting Started

### Project setup and run
<br />

Replace database details in chatproject/settings.py with that of your database:
```python
DATABASES = {
    'default': {
        'ENGINE': 'dbengine',
        'NAME': 'dbname',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'hosturl',
        'PORT': 'port',
    }
}
```

> Install dependencies
```bash
pip install channels
pip install daphne
```

> Migrate database and create superuser
```bash
python manage.py makemigrate
python manage.py migrate
python manage.py createsuperuser
```
> Run the server
```bash
python manage.py runserver
```

Navigate to admin console which will be on: localhost:8000/admin and log in with created superuser credentials. 
Navigate to Chats and create chat rooms.

<br />

## Screenshots
![Screenshot 2023-11-01 170112](https://github.com/RendreGreyling/Django-chat-app/assets/92786005/57ada3f3-901c-43e6-9ced-5b0dec3ec51b)



