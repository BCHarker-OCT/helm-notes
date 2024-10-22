# README

This repo is for notes related to learning about Helm. Notes have been organized below and have links to their respective sections. 

## Notes 

- [Basics of Helm](./01-Basics.md)
   - [What is Helm?](./01-Basics.md#what-is-helm)
   - [Installing and Configuring It](./01-Basics.md#installing-and-configuring-it)
   - [Helm 2 vs 3 Changes](./01-Basics.md#helm-2-vs-3-changes)
   - [Helm Components](./01-Basics.md#helm-components)
   - [Helm Charts](./01-Basics.md#helm-charts)
      - [Helm Chart Structure](./01-Basics.md#helm-chart-structure)
   - [Helm CLI](./01-Basics.md#helm-cli)
   - [Customizing Chart Parameters](./01-Basics.md#customizing-chart-parameters)
   - [Adding a repository of chart](./01-Basics.md#adding-a-repository-of-chart)
   - [Lifecycle Management](./01-Basics.md#lifecycle-management)
   - [Running a deployment upgrade of a Helm Chart](./01-Basics.md#running-a-deployment-upgrade-of-a-helm-chart)
- [Anatomy of Helm Charts](./02-Anatomy-of-Helm-Charts.md)
   - [Writing Helm Charts](./02-Anatomy-of-Helm-Charts.md#writing-helm-charts)
   - [Templating](./02-Anatomy-of-Helm-Charts.md#templating)
   - [Templating Examples](./02-Anatomy-of-Helm-Charts.md#templating-examples)
   - [Verify your Chart](./02-Anatomy-of-Helm-Charts.md#verify-your-chart)
      - [Linting](./02-Anatomy-of-Helm-Charts.md#linting)
      - [Template](./02-Anatomy-of-Helm-Charts.md#template)
      - [Dry Run](./02-Anatomy-of-Helm-Charts.md#dry-run)
   - [Functions](./02-Anatomy-of-Helm-Charts.md#functions)
   - [Pipelines](./02-Anatomy-of-Helm-Charts.md#pipelines)
- [Logical Operators](./03-Advanced-Features.md)
   - [Conditionals](./03-Advanced-Features.md#conditionals)
   - [Logical Function Operators](./03-Advanced-Features.md#logical-function-operators)
   - [With Blocks / Scoping](./03-Advanced-Features.md#with-blocks--scoping)
   - [Ranges (Loops)](./03-Advanced-Features.md#ranges-loops)
   - [Named Templates](./03-Advanced-Features.md#named-templates)
   - [Chart Hooks](./03-Advanced-Features.md#chart-hooks)
      - [Hook Weights](./03-Advanced-Features.md#hook-weights)
      - [Types of Hooks](./03-Advanced-Features.md#types-of-hooks)
      - [Hook Examples](./03-Advanced-Features.md#hook-examples)
- [Packaging Signing and Uploading](./04-Packaging-Signing-Upload.md)
   - [Packaging](./04-Packaging-Signing-Upload.md#packaging)
   - [Creating a Key](./04-Packaging-Signing-Upload.md#creating-a-key)
   - [Signing](./04-Packaging-Signing-Upload.md#signing)
   - [Provenance film](./04-Packaging-Signing-Upload.md#provenance-film)
   - [Importing and Verifying a Chart](./04-Packaging-Signing-Upload.md#importing-and-verifying-a-chart)
   - [Uploading](./04-Packaging-Signing-Upload.md#uploading)
      - [Generate the index.yaml file](./04-Packaging-Signing-Upload.md#generate-the-indexyaml-file)
      - [Possible Upload Providers](./04-Packaging-Signing-Upload.md#possible-upload-providers)

## Resources 

- [glasskube-tutorial](https://glasskube.dev/blog/what-is-helm-in-kubernetes/)
- [Semantic Versioning 2.0.0](https://semver.org)


## Chapter Sections 

Using the python script now instead, but this was a nice simple way to do it. 

`ggrep "^##" 01-Basics.md | gsed -E 's/^###/   -/; s/^##/ -/'`

