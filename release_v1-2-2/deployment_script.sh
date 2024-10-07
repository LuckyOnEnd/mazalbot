git pull
sudo systemctl stop nginx
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

docker-compose down
docker-compose up --build -d
sudo systemctl restart nginx

