cd /home/cloud_user
mkdir -p promwork
cd promwork
wget https://github.com/prometheus/prometheus/releases/download/v2.8.0-rc.0/prometheus-2.8.0-rc.0.linux-amd64.tar.gz
tar -xvzf prom*.gz
cd prometheus-2.8.0-rc.0.linux-amd64
sudo cp prometheus /usr/local/bin
sudo cp promtool /usr/local/bin
sudo mkdir -p /etc/prometheus
sudo cp -r ./consoles /etc/prometheus
sudo cp -r ./console_libraries /etc/prometheus
cd ..
wget https://raw.github.com/linuxacademy/content-aiops-essentials/master/prometheus.yml
sudo cp prometheus.yml /etc/prometheus
wget https://raw.github.com/linuxacademy/content-aiops-essentials/master/prometheus.service
sudo cp prometheus.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl status prometheus
