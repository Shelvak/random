#!/bin/bash

NS='Ingrase el namespace: : '
options=("default" "staging" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "default")
            namespace="default"
            break
            ;;
        "staging")
            namespace="staging"
            break
            ;;
        "Quit")
            exit
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

echo " "
echo "Ingrese elnombre del pod"
read nombrepod

workdir=`pwd`


echo "Script generador de Pod  Cloud"
echo "Namespace: " $namespace
echo "Pod name: " $nombrepod


function obtenerPod()
{
    podname=$(kubectl get pod -l app=sidekiq -n $namespace |grep |head -n 1|awk '{print $1}')
    echo $podname
}

pod=$(obtenerPod)
echo Pod Seleccionado: $pod


kubectl -n $namespace get pod $pod -o json|jq --arg namespace $namespace --arg name ${nombrepod}-migrator '.kind = "Pod"| .apiVersion = "v1" | del(.metadata,.spec.affinity,.spec.nodeName,.spec.nodeSelector,.spec.tolerations,.spec.restartPolicy,.spec.schedulerName,.status,.spec.dnsPolicy,.spec.containers[].livenessProbe,.spec.containers[].readinessProbe,.spec.containers[].terminationMessagePath,.spec.containers[].terminationMessagePolicy,.spec.enableServiceLinks)|. + {"metadata"}|.metadata += {"labels"}|.metadata.labels += {"app": "migrator"}| .spec.containers[] += {"command"}|.spec.containers[].command = ["tail"] |.spec.containers[].command += ["-F"] |.spec.containers[0].args = []| .spec += {restartPolicy: "Never"}|.metadata += {"name": "'$nombrepod'"} |.spec.nodeSelector += {entorno:"staging"} |.metadata += {"namespace": "default"}' > $nombrepod.json
sed -i '/enableServiceLinks/d' $nombrepod.json
