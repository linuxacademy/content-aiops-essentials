cd /home/cloud_user
mkdir -p nodework
cd nodework
wget https://github.com/prometheus/node_exporter/releases/download/v0.17.0/node_exporter-0.17.0.linux-amd64.tar.gz
tar -xvzf node*.gz
cd node_exporter-0.17.0.linux-amd64
sudo cp node_exporter /usr/local/bin
cd ..
wget https://raw.github.com/linuxacademy/content-aiops-essentials/master/node_exporter.service
sudo cp node_exporter.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl start node_exporter
sudo systemctl status node_exporter
