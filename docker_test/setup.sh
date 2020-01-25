docker volume create docker_test_volume
docker build -t docker_test .
docker run -v docker_test_volume:/home/data -d docker_test


