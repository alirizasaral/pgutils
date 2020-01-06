docker rm -f sampledb
docker run -p 5432:5432 --name sampledb -e POSTGRES_USER=docker -e POSTGRES_PASSWORD=docker sampledb:latest