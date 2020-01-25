docker build -t docker_gcp .
docker run -v docker_test_volume:/home/data -d docker_gcp


