docker build -f Dockerfile.gen -t skinatro/log-output-gen .
docker build -f Dockerfile.read -t skinatro/log-output-read .
docker push skinatro/log-output-gen
docker push skinatro/log-output-read