docker volume create docker_test
docker build -t docker_test .
docker container run -v docker_test:./ -d docker_test


