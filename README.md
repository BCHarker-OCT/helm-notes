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
   - [Conditionals](./02-Anatomy-of-Helm-Charts.md#conditionals)

## Resources 

- [glasskube-tutorial](https://glasskube.dev/blog/what-is-helm-in-kubernetes/)


## Chapter Sections 

Using the python script now instead, but this was a nice simple way to do it. 

`ggrep "^##" 01-Basics.md | gsed -E 's/^###/   -/; s/^##/ -/'`

