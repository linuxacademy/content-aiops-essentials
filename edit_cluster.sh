cp instance.yaml instance.yaml.backup
sed -i "s/MAX_SIZE/$1/" instance.yaml
sed -i "s/MIN_SIZE/$1/" instance.yaml
sed -i "s/CLUSTER_NAME/$KOPS_CLUSTER_NAME/" instance.yaml
cat instance.yaml | kops replace -f -
kops update cluster --yes
