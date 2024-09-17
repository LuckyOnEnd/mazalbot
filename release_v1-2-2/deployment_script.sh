git pull
sudo systemctl stop nginx
sudo docker-compose up --build -d
sudo systemctl restart nginx
