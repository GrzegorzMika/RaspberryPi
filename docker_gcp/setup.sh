docker build -t docker_gcp .
docker container run -v docker_test:/home/data -d docker_gcp


