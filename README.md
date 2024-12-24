# how to run it?

## enviroment
cp .env.example .env

## docker commands
```
docker commands
docker-compose build
docker-compose up
docker-compose run web python database/migrate.py
docker-compose run web python database/seed.py
```

## test url

http://localhost:8000/items

## swagger url
http://localhost:8000/docs
