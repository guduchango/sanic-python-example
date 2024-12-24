# how to run it?

# docker commands
docker-compose build
docker-compose up
docker-compose run web python database/migrate.py
docker-compose run web python database/seed.py

#test
http://localhost:8000/items

#swagger
http://localhost:8000/docs
