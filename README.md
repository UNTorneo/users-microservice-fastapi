docker build -t users-microservice-fastapi .
docker run -p 8080:8080 -e dbHost=172.17.0.2 -e dbPort=5432 -e dbUser=fastapi -e dbPassword=123 -e dbName=fastapi_db -d users-microservice-fastapi

docker container ls -a -> Muestra lista contenedores -> Extraes el CONTAINER_ID -> docker inspect CONTAINER_ID

docker container start CONTAINER_ID
docker container stop CONTAINER_ID

842e49b74d41301405f97a9206c68fd3715408c87a5ab5eab3f653d1443017fb

uvicorn app.main:app --reload
http://127.0.0.1:8080/docs