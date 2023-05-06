Comandos para ejecutar la base datos
docker build -t fastapi-db .
docker run -d -t -i -p 5432:5432 --name fastapi-db fastapi-db

Dockerfile de la base de datos
FROM postgres:15.2
ENV POSTGRES_PASSWORD=123
ENV POSTGRES_USER=fastapi
ENV POSTGRES_DB=fastapi_db
EXPOSE 5432

Ejecutar microservicio en docker
docker build -t users-microservice-fastapi .
docker run -p 8080:8080 -e dbHost=172.17.0.2 -e dbPort=5432 -e dbUser=fastapi -e dbPassword=123 -e dbName=fastapi_db -d users-microservice-fastapi

docker container ls -a -> Muestra lista contenedores -> Extraes el CONTAINER_ID -> docker inspect CONTAINER_ID

docker container start CONTAINER_ID
docker container stop CONTAINER_ID

Para ejecutar en el local
uvicorn app.main:app --reload

Swagger
http://127.0.0.1:8080/docs