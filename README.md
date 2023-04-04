docker build -t users-microservice-fastapi .
docker run -p 8080:8080 -e DB_HOST=172.17.0.2 -e DB_PORT=5432 -e DB_USER=fastapi -e DB_PASSWORD=123 -e DB_NAME=fastapi_db -d users-microservice-fastapi

docker container ls -a -> Muestra lista contenedores -> Extraes el CONTAINER_ID

docker container start CONTAINER_ID
docker container stop CONTAINER_ID

d88d14d2bca01e46e9a870f7f8a7333f23ed193f0e8ab0d917eab8a4dc8f3c88

uvicorn app.main:app --reload