# Packaging Signing and Uploading

## Packaging 
Run the command: `helm package ./nginx-chart`

This will package the chart into a file .tgz. 

## Creating a Key 

```bash
gpg --full-generate-key "John Smith
# Helm prefers the old type of keyring 
gpg --export-secret-keys > ~/.gnupg/secring.gpg

# List keys 
gpg --list-keys


# To download a key for verification of a chart 
gpg --revc-keys --keyserver keyserver.ubuntu.com <ID>
```

## Signing 

Signed charts allow us to use a Private Key and creates a provenance file that makes it easy to track the developer of a chart. 

```bash
helm package --sign --key 'John Smith' --keyring ~/.gnupg/secring.gpg ./nginx-chart
```

## Provenance film 

When packaged Helm creates a `.prov` provenance file to track the provenance of the chart, which is stored outside the package. 

```bash
$ ls
nginx-chart nginx-chart-0.1.0.tgz nginx-chart-0.1.0.tgz.prov
```

The file includes a sh256sum that can be used to make sure the checksum of the package matches that of the provenance file. 

The signature inside the file assures that the hash is not changed unexpectedly. 

## Importing and Verifying a Chart

```bash 
helm install --verify nginx-chart-0.1.0
```

## Uploading 



An upload would contain at minimum the following: 

- `index.yaml` file

Move these files to a new directory: 
- package file 
- provenance file

### Generate the index.yaml file 

```bash 
helm repo index nginx-chart-files/ --url https://repo-example.com/charts
```

### Possible Upload Providers 

- Google 
- AWS 
- DigitalOcean 
- GitHub