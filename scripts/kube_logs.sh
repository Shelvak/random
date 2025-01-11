#!/bin/zsh

HELP=$(<<EOF
  Use:
  ./kube_logs.sh example1
  ./kube_logs.sh example2
  ./kube_logs.sh example3
EOF
)

if [ -z "$1" ]
then
    echo $HELP
    exit 1
fi

# kubectl exec -it $(kubectl get pods |grep example-deploy | awk '{print $1}' |shuf |head -n1) bash

case "$1" in
    example1)
        containers=$(kubectl get pods -l app=example1 | grep Running | shuf | awk '{ print $1 }' )
        ;;
    example2)
        containers=$(kubectl get pods -l app=example2 | grep Running | awk '{ print $1 }' )
        ;;
    example3)
        containers=$(kubectl get pods -l app=example3 | grep Running | awk '{ print $1 }' )
        ;;
    *)
        echo $HELP
        exit 1
esac

if [ ! -z "$containers" ]
then
    lines=${2:-1000}
    echo "Logging last $lines lines in \n $containers..."
    echo $containers | uniq | xargs -I{} --max-args=1 --max-procs=$(echo $containers|wc -l) kubectl logs -f --tail=$lines {}
else
    echo "No container"
    exit 1
fi
