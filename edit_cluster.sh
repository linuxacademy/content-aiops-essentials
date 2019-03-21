cp cluster.yaml cluster.yaml.backup
sed -i 's/      name: nodepool1/      name:nodepool1\n      count: 3/' cluster.yaml
