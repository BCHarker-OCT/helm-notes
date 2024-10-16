# Anatomy of Helm Charts

## Writing Helm Charts

Although Helm charts are not programs in and of themselves, we can also have Helm charts do certain actions for us when performing tasks. For example, backing up a database before running an upgrade. 

To create a helm chart use the command: `helm create nginx-chart`


## Templating 

The Template directive looks like follows, to allow us to create variable items that can be dynamically updated within the Helm charts:
```yaml
{{ .Release.Name}}-nginx
```

**CASE-Sensitive templating values we might want to use:**
```yaml
# Release
Release.Name
Release.Namespace
Release.IsUpgrade
Release.IsInstall
Release.Revision
Release.Service
# Chart 
Chart.Name
Chart.ApiVersion
Chart.Version
Chart.Type
Chart.Keywords
Chart.Home
# Cluster Capabilites 
Capabilities.KubeVersion
Capabilities.ApiVersions
Capabilities.HelmVersion
Capabilities.GitCommit
Capabilities.GitTreeState
Capabilities.GoVersion
# Values (user-defined, so case may vary)
Values.replicaCount
Values.image
```

## Templating Examples 

```yaml 
# service.yaml
apiVersion: v1 
kind: Service
metadata:
  name: {{ •Release.Name }}-svc
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app: hello-world
```

```yaml 
#deployment.yaml 
apiVersion: apps/v1 deployment.yaml
kind: Deployment
metadata:
  name: {{ .Release.Name }}-nginx
spec:
  replicas: {{ .Values.replicaCount }}
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
      - name: hello-world
        image: {{ .Values.image.repository }}:{{ .Values.image.tag }}
      - name: http
        containerPort: 80
         protocol: TCP
```

```yaml
#values.yaml OR --set replicaCount=2 --set image=ngix
replicaCount: 2
image: nginx
  repository: nginx
  pullPolicy: IfNotPresent
  tag: "1.16.0"
```

## Verify your Chart 

### Linting 
Run the helm lint command and specify the path to your directory:

`helm lint ./nginx-chart`

### Template 
Checks that templating values will be used as expected when the Helm chart is run. 
`helm template ./nginx-chart`

> Render chart templates locally and display the output.

> Any values that would normally be looked up or retrieved in-cluster will be
faked locally. Additionally, none of the server-side testing of chart validity
(e.g. whether an API is supported) is done.

### Dry Run 
Catches issues in the manifest not caught by template or the linter.
`helm install hellow-world-1 ./nginx-chart --dry-run`

## Functions 

Just like in programming functions to perform certain actions. 

```yaml
# Uppercase function 
{{ upper .Values.image.reopistory }} --> image: NGINX 
{{ quote .Values.image.repository }} --> image: "nginx" 
{{ replace "x" "y" .Values.image.repository }} --> image: nginy
{{ shuffle .Values.image.repository }} --> image: "xginn"

# Additional functions 
abbrev, abbrevboth, camelcase, cat, 
contains, hasPrefix, hasSuffix, indent,
initials, kebabcase, lower, nindent, 
nospace, plural, print, printf, printin, 
quote, randAlpha, randAlphaNum, randA

# Default function 

{{ default "nginx" .Values.image.reopository }}
```

Documentation: [helm.sh String Functions](https://helm.sh/docs/chart_template_guide/function_list/#string-functions)

## Pipelines 

Allow you to pipe multiple functions one after the other using pipes, just like in Bash. 

```yaml
{{ .Values.image.repoistory |upper|quote }} --> image: "NGINX"
```

