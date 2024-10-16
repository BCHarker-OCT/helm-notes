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
  {{- end }}
spec:
  ports:
    - port: 80
      name: http
  selector:
    app: hello-world
```