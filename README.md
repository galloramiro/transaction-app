# transaction-app

### Set up the envirorment
- go to backend/app/ and create the .env using the .env.template
- Install [docker](https://docs.docker.com/get-docker/)
- Build the containers `docker-compose up --build` (*)
  

(*) If you have an exit code in the frontend run `docker-compse run --rm frontend npm install`

Now you can explore and work in the proyect.

### Backend
```
# Basic commands
$ docker-compose run --rm backend python manage.py migrate
$ docker-compose run --rm backend python manage.py createcachetable
$ docker-compose run --rm backend python manage.py createsuperuser

# Run tests
$ docker-compose run --rm backend pytest -vv
```
