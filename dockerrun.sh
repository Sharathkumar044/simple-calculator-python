# Build the Docker image
docker build -t my-web-app .

# Run the Docker container
docker run -p 8082:80 my-web-app

