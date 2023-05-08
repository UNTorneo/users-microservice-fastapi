Comandos para ejecutar la base datos
docker run --name users-db -e POSTGRES_PASSWORD=123 -e POSTGRES_USER=fastapi -e POSTGRES_DB=fastapi_db -d -p 5432:5432 postgres

Ejecutar microservicio en docker
Crear imagen
docker build -t users-ms .

Valentina
docker run -p 8080:8080 -e dbHost=172.17.0.2 -e dbPort=5432 -e dbUser=fastapi -e dbPassword=123 -e dbName=fastapi_db -d users-ms

Sebastian
docker run -p 8088:8080 -e dbHost=172.17.0.2 -e dbPort=5444 -e dbUser=fastapi -e dbPassword=123 -e dbName=fastapi_db --name users-ms users-ms

docker container ls -a -> Muestra lista contenedores -> Extraes el CONTAINER_ID -> docker inspect CONTAINER_ID

docker container start CONTAINER_ID
docker container stop CONTAINER_ID

Para ejecutar en el local
uvicorn app.main:app --reload

Swagger
http://127.0.0.1:8080/docs

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