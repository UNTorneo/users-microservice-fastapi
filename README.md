docker build -t users-microservice-fastapi .
docker run -p 8080:8080 -e dbHost=172.17.0.3 -e dbPort=5431 -e dbUser=fastapi -e dbPassword=123 -e dbName=fastapi_db --name users-ms users-microservice-fastapi

docker container ls -a -> Muestra lista contenedores -> Extraes el CONTAINER_ID -> docker inspect CONTAINER_ID

docker container start CONTAINER_ID
docker container stop CONTAINER_ID

842e49b74d41301405f97a9206c68fd3715408c87a5ab5eab3f653d1443017fb

uvicorn app.main:app --reload
http://127.0.0.1:8080/docs

docker run --name users-db -e POSTGRES_PASSWORD=123 -e POSTGRES_USER=fastapi -e POSTGRES_DB=fastapi_db -d -p 5432:5432 postgres

{
  "username": "juanito",
  "birthday": "2020-05-05",
  "email": "juanito@eldon.com",
  "countryId": 1,
  "cityId": 1,
  "latitude": 0,
  "longitude": 0,
  "password": "juanitoelmejordelmundo"
}