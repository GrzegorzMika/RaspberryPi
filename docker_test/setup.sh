docker volume create docker_test
docker build -t docker_test
docker container run -v -d docker_test:/ docker_test


