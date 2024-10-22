# Logical Operators 

## Conditionals 

```yaml
# services.yaml 
apiVersion: v1 service.yaml
kind: Service
metadata:
  name: {{ .Release.Name }}-nginx
  # - beginning the if trims the whitespaces 
  {{- if .Values.orgLabel }}
  labels:
    org: {{ .Values.orgLabel }}
  {{- else if eq .Values.orgLabel "hr" }}
  labels:
    org: human resources
  {{- end }}
spec:
  ports:
    - port: 80
      name: http
  selector:
    app: hello-world
```

Conditionally create a service account: 

```yaml 
# values.yaml 
serviceAccount:
  # Specifies whether a ServiceAccount should be created
  create: true
```

```yaml
#serviceaccount.yaml 
# only creates if the value is set to true
{{- if .Values.serviceAccount.create }}
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{. Release. Name }}-robot-sa
{{- else }}
```

or use with

```yaml 
# values.yaml
serviceAccount:
  # Specifies whether a service account should be created
  create: false
  # Annotations to add to the service account
  annotations: {}
  # The name of the service account to use.
  # If not set and create is true, a name is generated using the fullname template
  name: webapp-sa
  labels: 
    tier: frontend
    type: web
    mode: proxy
```

```yaml
#serviceaccount.yaml 
{{- with .Values.serviceAccount.create }}
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ $.Values.serviceAccount.name }}
  labels:
    app: webapp-color
{{- end }}
```

**Equality operator**
Here is an example for quality, notice the statement is slightly different to many programming languages: 

```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: {{ .Values.service.name }}
  namespace: default
spec:
  ports:
  - port: 8080
    protocol: TCP
    targetPort: 8080
    {{-if eq .Values.service.type "NodePort" }}
    nodePort: {{ .Values.service.nodePort }}
    {{-end }}
  selector:
    name: webapp-color
  type: {{ .Values.service.type }}
status:
  loadBalancer: {}
```

## Logical Function Operators

`eq` equal
`ne` not equal
`lt` less than
`le` less than or equal to
`gt` greater than
`ge` greater than or equal to
`not` negation
`empty` value is empty

## With Blocks / Scoping 

By default the scope used is the root scope for values. A with block 
allows you to prepend a scope for a block to make it easier to specify variable values without having very long names for a scope: 

For example: 

`.Values.app.ui.bg` 

Can be shortened to: 

> [!NOTE]
> You can refer to the root scope with a with scoped block with the character `$`

```yaml 
apiVersion: v1 configmap.yaml
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-appinfo
data:
  {{- with .Values.app }}
    {{- with.ui }}
    background: {{.bg }}
    foreground: {{ .fg }}
    {{- end }}
  {{- with .db }}  
  database: {{ .name }}
  connection: {{ .conn }}
  {{- end }}
  release: {{ $.Release.Name }}
  {{- end }}
```

## Ranges (Loops)

```yaml
#values.yaml
regions:
- ohio
- newyork
- ontario
- london
- singapore
- mumbai
- chicago
```

```yaml 
#configmap.yaml 
apiVersion: v1
kind: ConfigMap
metadata:
name: {{ .Release.Name }}-regioninfo
data:
regions:
{{- range .Values.regions }}
- {{ . | quote }}
{{- end }}
```

```yaml 
{{- with .Values.serviceAccount.create }}
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ $.Values.serviceAccount.name }}
  labels:
    {{- range $key, $val := $.Values.serviceAccount.labels }}
    {{ $key }}: {{ $val }}
    {{- end }}
    app: webapp-color
{{- end }}
```

## Named Templates 

A way to create re-usable lines for Helm Charts. This starts by naming a file with the `_`. 
All files with an underscore are skipped. 


For example a file name `_helpers.tpl` we define a labels template: 
```yaml
# To call the scope in another file add the . for the scope! 
{{- define "labels" }}
   app.kubernetes.io/name: {{ .Release.Name }}
   app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{- define "annotations" }}
annotation-key: annotation-value
{{- end }}
```

> [!IMPORTANT]
> The spacing within your template file is important as it's added as-is. Use the `indent` function to fix this, but cal lthe template with the `include` function rather than the 
`template` action.

Subsequently, we can make use of this in our `service.yaml` file: 

```yaml
apiVersion: v1 service.yaml
kind: Service
metadata:
  name: {{ Release. Name }}-nginx
  labels:
   {{- template "labels" . }} # Add a dot to add the SCOPE to the template! 
spec:
  ports:
  - port: 80
    targetPort: http
    protocol: TCP
    name: http
  selector:
    app: hello-world
```

Deployment.yaml:
```yaml
apiVersion: apps/v1 deployment.yaml
kind: Deployment
metadata:
  name: {{ .Release.Name }}-nginx
  labels:
     {{- template "labels" . ｝｝
spec:
  selector:
  matchLabels:
  {{- include "1abels". | indent 2}}
template:
  metadata:
  labels:
  {{- include "labels" . | indent 4}}
  spec:
    containers:
    - name: nginx
      image: "nginx:1.16.0"
      imagePullPolicy: IfNotPresent
      ports:
        - name: http
          containerPort: 80
          protocol: TCP
```

> [!NOTE]
> As noted, add the `.` when referencing the template to add the scope for variables. 

## Chart Hooks 

Can trigger an action when something with a chart changes. For example, running a DB backup when a chart is upgraded.

Create a job instead of a pod to run a 1-time action when triggered. 


### Hook Weights
In Helm, hooks are executed in a specific order based on their **weights**. Here’s how it works:

1.  **Weight Sorting**: Hooks are sorted by their assigned weights, which can be positive or negative numbers. By default, if no weight is specified, it is set to **0**.
2.  **Execution Order**: Hooks with lower weights (more negative) are executed first. For example, a hook with a weight of **\-5** will run before one with a weight of **5**.
3.  **Same Weight Handling**: If multiple hooks have the same weight, they are sorted by their resource kind and then by name in ascending order.

[So, the general ascending order of execution is from the most negative weight to the most positive weight, ensuring a deterministic order for your hooks](https://www.golinuxcloud.com/helm-hook-weight-order-kubernetes/)[1](https://www.golinuxcloud.com/helm-hook-weight-order-kubernetes/)[2](https://helm.sh/docs/topics/charts_hooks/).


### Types of Hooks 

| Hook          | Action   | Hook          |
|---------------|----------|---------------|
| pre-install   | install  | post-install   |
| pre-delete    | delete   | post-delete    |
| pre-upgrade   | upgrade  | post-upgrade   |
| pre-rollback   | rollback | post-rollback  |


### Hook Examples
Job Example: 
```yaml 
apiVersion: batch/v1 
kind: Job
metadata:
  name: {{ .Release.Name }}-nginx
annotations:
  "helm.sh/hook": pre-upgrade
  "helm.sh/hook-weight": "5" 
  "helm.sh/hook-delete-policy": hook-succeeded # delete if hook succeeds 
spec:
  template:
    metadata:
      name: {{ .Release.Name }}-nginx
    spec:
      restartPolicy: Never
      containers:
      - name: pre-upgrade-backup-job
        image: "alpine"
        command: ["/bin/backup.sh"]
```

Post Upgrade Hook 

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: upgrade-hook
  annotations:
    "helm.sh/hook": post-upgrade
spec:
  template:
    spec:
      containers:
      - name: upgrade-hook
        image: alpine
        command: ["echo", "Successfully Upgraded!"]
      restartPolicy: Never
  backoffLimit: 4
```
