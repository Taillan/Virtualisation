# SY3 - Virtualisation

Pour ce projet nous avons fait le choix de nous servir d'une application de Quizz réalisé au cours d'un projet précédent et qui possèdent l'avantage d'être un projet en "trois-tiers" avec front / back-end / database.
Nous avons décidé de réaliser une dockerisation de ces trois parties et de les exposer sur un noeud kubernetes en se servant de minikube.
Ne souhaitant pas se placer sur un cloud public (aws / gcloud) avec un risque de facturation et possèdant déjà un serveur à la maison, nous avons décider de déployer notre noeud kube sur une VM Debian d'un Hyperviseur Proxmox exposé à travers le domaine suivant : https://sy3.monnot.org


## Cloudskillsboost profiles

![Monnot](k8s/devops/profile_monnot.png)
![Taillandier](k8s/devops/profile_taillandier.png)

## Docker

### Build images

```Bash
docker build src/BDD/ -t mariadb
docker build src/quiz-api/ -t flask
docker build src/quiz-ui/ -t vuejs
```

### Run Containers

```Bash
docker run -d -e MYSQL_HOST="" -e MYSQL_USER="root" -e MYSQL_PASSWORD="rootroot" -e MYSQL_DB="QuizzDB" -p 5000:5000 --name flask flask
docker run -d -p 80:80 --name vuejs vuejs
docker run -d -p 3306:3306 --name mysql mysql
```

## Schema cluster k8s

![cluster](k8s/devops/DevOps.png)

```Bash
kubectl get all && kubectl get ingress
NAME                         READY   STATUS    RESTARTS   AGE
pod/flask-7db7dff94d-bsb4l   1/1     Running   0          33h
pod/mysql-775dc84fcc-bqglz   1/1     Running   0          33h
pod/vuejs-f7bd99f46-mhlrc    1/1     Running   0          33h

NAME                    TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/flask-service   ClusterIP   10.107.241.231   <none>        80/TCP           33h
service/kubernetes      ClusterIP   10.96.0.1        <none>        443/TCP          46d
service/mysql-service   NodePort    10.105.121.208   <none>        3306:30306/TCP   33h
service/vuejs-service   ClusterIP   10.110.173.199   <none>        80/TCP,443/TCP   32h

NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/flask   1/1     1            1           33h
deployment.apps/mysql   1/1     1            1           33h
deployment.apps/vuejs   1/1     1            1           33h

NAME                               DESIRED   CURRENT   READY   AGE
replicaset.apps/flask-7db7dff94d   1         1         1       33h
replicaset.apps/mysql-775dc84fcc   1         1         1       33h
replicaset.apps/vuejs-f7bd99f46    1         1         1       33h

NAME          CLASS    HOSTS            ADDRESS        PORTS   AGE
sy3-ingress   <none>   sy3.monnot.org   192.168.67.2   80      32h
```

## Minikube setup

```Bash
minikube start --cpus 4 --memory 8192
minikube addons enable ingress
minikube ip
echo 'alias kubectl="minikube kubectl --"' >> ~/.bashrc
source ~/.bashrc
```

## Kubernetes Commands

```bash
kubectl get pod
kubectl get service
kubectl exec [pod] -- bash
kubectl logs [pod] -n [namespace]
kubectl describe pod [pod] -n [namespace]
```

## Database Mysql deployment

```Bash
kubectl apply -f database/deployment.yaml
kubectl apply -f database/service.yaml
```

## Back-end Flask deployment

```Bash
kubectl apply -f back/deployment.yaml
kubectl apply -f back/service.yaml
```

```Bash
minikube service mysql-service --url

http://192.168.49.2:30306
```

On modifie le fichier `k8s/back/configmap.yaml` avec les bonnes informations.

## Front-end Vuejs deployment

```bash
kubectl apply -f front/deployment.yaml
kubectl apply -f front/service.yaml
```

## Ingress Nginx deployment

```Bash
kubectl apply -f devops/ingress.yaml
```

En local :
```bash
minikube ip # IP du cluster
echo "192.168.X.X	front-end.intra" >> /etc/hosts 
```