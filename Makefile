build:
	docker-compose build api

start:
	docker-compose up api

daemon:
	docker-compose up -d api

db/connect:
	docker exec -it testdb psql -Upostgres