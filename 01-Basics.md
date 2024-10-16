# Basics of Helm 

## What is Helm? 
Helm tracks changes, which allows for an easy rollback when a change didn't go as expected. 

```bash
# Commands
helm install wordpress 
helm upgrade wordpress
helm rollback wordpress
helm uninstall wordpress
```

## Installing and Configuring It

- [See the documentation on installation](https://helm.sh/docs/intro/install/)
- Setup Debug via ENV var: `$HELM_DEBUG`
- Enable verbose output: `--verbose`

## Helm 2 vs 3 Changes 

- Helm 1.0 Feb 2016 
- Helm 2.0 Nov 2016
  - Extra component called Tiller, which was the middle-man. Tiller ran in god mode to make any changes needed in the cluster. 
  - Manual changes will be ignored by Helm, potentially causing issues during a rollback. 
- Helm 3.0 Nov 2019
  - 3-way strategic merge patch 
  - Helm 3 looks at previous chart, current chart, and live state. Preserves what you might have added manually outside of helm. 

## Helm Components 

- helm cli 
- charts 
  - collection of files 
- release
  - revision created each time a chart is applied
- metadata
  - data about data 
  - stored as kubernetes secrets 
- `values.yaml`
  - generally only fiel you need to modify to update 

*Specify a release name:*
`helm install <release> bitnami/wordpress`

See: [Artifacthub.io](https://artifacthub.io)

## Helm Charts 
Charts are text files. Templating allows us to link charts to deployment items in the cluster.

- `values.yaml` values to be used for templating
- `chart.yaml` information about the chart, api verion, app version, type


```yaml
apiVersion: v2    # Helm 3 is v2, Helm 2 didn't have this at all 
appVersion: 5.8.1 # Version of wordpress being deployed
version: 12.1.27  # Version of the chart 
name: wordpress   # name of chart 
description: Web publishing platform for building blogs and websites.
type: application # 2 types library (utility for building chart )/ app for app
dependencies:
  - condition: mariadb.enabled # has its own helm chart 
    name: mariadb
    repository: https://charts.bitnami.com/bitnami
    version: 9.x.x
    ‹code hidden >
keywords:
  - application
  - blog
  - wordpress
maintainers:
  - email: containers@bitnami.com
    name: Bitnami
home: https: //github.com/bitnami/charts/tree/master/bitnami/wordpress
icon: https://bitnami.com/assets/stacks/wordpress/img/wordpress-stack-220x234.png
```


### Helm Chart Structure 

```bash
tree hello-world-chart 
hello-world-chart
├── Chart.yaml
├── LICENSE
├── README.md
├── templates/
└── values.yaml
```

## Helm CLI 

```bash
helm 
helm help 
helm rollback 
helm repo --help 
helm repo update --help
helm search hub wordpress # search artifact hub 
helm search repo wordpress # search repo for a keyword in charts 

# Add repo 
helm repo add bitname https://charts.bitnami.com/bitnami
helm repo list 
helm repo update 
```

## Customizing Chart Parameters 

We can use the set option at the command line to specify values for the chart deploy. 

```bash
helm install --set wordpressBlogName="Helm Tutorial" my-blog bitnami/wordpress
```

**Using custom-values.yaml** 

```bash
helm install --values custom-values.yaml my-blog bitnami/wordpress
```

Pull the chart to use values

```bash 
helm pull bitnami/wordpress          # pulls compress chart 
helm pull --untar  bitnami/wordpress # uncompresses the chart 
```

## Adding a repository of chart 

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo search wordpress
helm install amaze-surf bitnami/apache

## List release and uninstall release
helm list
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
amaze-surf      default         1               2024-10-12 18:42:30.255089323 +0000 UTC deployed        apache-11.2.20  2.4.62     
crazy-web       default         1               2024-10-12 18:43:21.425960422 +0000 UTC deployed        nginx-18.2.2    1.27.2     
happy-browse    default         1               2024-10-12 18:43:14.662976145 +0000 UTC deployed        nginx-18.2.2    1.27.2     

helm uninstall happpy-browse
## Remove a repo 
helm repo remove hashicorp
"hashicorp" has been removed from your repositories
```

## Lifecycle Management 
Each release can be managed independently, even if based on the same chart. 

```bash
## Pass in specific version of chart 
helm install nginx-release bitnami/nginx --version 7.1.0
helm upgrade nginx-release bitnami/nginx

## Get info about a release 
helm history nginx-release

helm rollback nginx-release <revision>
```

A rollback counts as a new revision. So rolling out version 1, upgrading, then rolling back goes to the next version in the chart, which would be version 3! 

## Running a deployment upgrade of a Helm Chart 


Finding Versions with this command: 
`helm search repo bitnami/nginx --versions`


```bash
controlplane ~ ➜  helm list
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART         APP VERSION
dazzling-web    default         3               2024-10-12 22:47:27.575188773 +0000 UTC deployed        nginx-12.0.4  1.22.0     

controlplane ~ ➜  helm upgrade dazzling-web bitnami/nginx --version 13
Release "dazzling-web" has been upgraded. Happy Helming!
NAME: dazzling-web
LAST DEPLOYED: Sat Oct 12 22:51:34 2024
NAMESPACE: default
STATUS: deployed
REVISION: 4
TEST SUITE: None
NOTES:
CHART NAME: nginx
CHART VERSION: 13.2.34
APP VERSION: 1.23.4

** Please be patient while the chart is being deployed **
NGINX can be accessed through the following DNS name from within your cluster:

    dazzling-web-nginx.default.svc.cluster.local (port 80)

To access NGINX from outside the cluster, follow the steps below:

1. Get the NGINX URL by running these commands:

  NOTE: It may take a few minutes for the LoadBalancer IP to be available.
        Watch the status with: 'kubectl get svc --namespace default -w dazzling-web-nginx'

    export SERVICE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].port}" services dazzling-web-nginx)
    export SERVICE_IP=$(kubectl get svc --namespace default dazzling-web-nginx -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
    echo "http://${SERVICE_IP}:${SERVICE_PORT}"

controlplane ~ ➜  helm list
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
dazzling-web    default         4               2024-10-12 22:51:34.94929947 +0000 UTC  deployed        nginx-13.2.34   1.23.4  
```