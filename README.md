# visity
Visity - Most useful tool for following workers visits to outlet

## Deployment
+ clone the repo
+ create .env file inside main directory, in our case it is 'visity' folder (top one, not the one with settings.py)
+ put these value into `.env`: 
```
    SECRET_KEY=<DJANGO_PROJECT_SECRET_KEY>
    DEBUG=<LEAVE IT EMPTY FOR PRODUCTION, PUT ANYTHING TO ENABLE DEBUGGING>
    
    POSTGRES_DB=<DB_NAME>
    POSTGRES_USER=<USERNAME_FOR_DB>
    POSTGRES_PASSWORD=<PASSWORD_FOR_DB>
    POSTGRES_PORT=<POSTGRES_PORT, usually 5432>
    POSTGRES_HOST=db
```
+ create docker containers
```
docker-compose up -d --build
```

+ make database migrations
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```
+ create super user for admin panel
```
docker-compose exec web python manage.py createsuperuser
```
Follow all instructions of interactive form, just enter username and password, others are optional.
+ collect static files
```
docker-compose exec web python manage.py collectstatic
```
+ restart containers (just in case)
```
docker-compose restart
```
## URLs
+ `/admin/` - admin panel (you'll be asked to enter username and password of superuser, you created it a few steps earlier)
+ `/docs/` - documentation about API