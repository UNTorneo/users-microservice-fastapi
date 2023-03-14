docker build -t users-microservice-fastapi .
docker run -p 8080:80 -e DB_HOST=172.17.0.2 -e DB_PORT=5432 -e DB_USER=fastapi -e DB_PASSWORD=123 -e DB_NAME=fastapi_db users-microservice-fastapi