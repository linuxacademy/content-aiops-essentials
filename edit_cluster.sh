cp instance.yaml instance.yaml.backup
sed -i "s/  maxSize: 2/  maxSize: $1/" instance.yaml
sed -i "s/  minSize: 2/  minSize: $1/" instance.yaml
cat instance.yaml | kops replace -f -
kops update cluster --yes
