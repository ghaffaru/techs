# techs

## Installation
Use [docker](https://www.docker.com/) to set it up

```
docker-compose build
```

## Migrate

```
docker-compose run web alembic upgrade head
```

# Boot up 
```
docker-compose up
```
## Use the url to hit the endpoints
```
http://localhost:8010
```

## API Docs
```
http://localhost:8010/docs
```

## Technologies Used
* Python 3.9
* FastAPI
* Docker
* PostgreSQL
* Celery
* Redis
* SQLAlchemy
* Plotly
