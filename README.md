# data-pipelines-with-airflow

An Airflow data pipeline that copies data from JSON files in a S3 Bucket to Redshift for further processing. 

## Airflow configuration
Before starting the pipeline you have to create a Redshift Cluster on AWS.
The next step is to create the following variables and connections in Airflow:

### Variables
* s3_bucket: udacity-dend
* s3_prefix: data-pipelines

### Connections
* aws_credentials --> AWS Key and AWS Secret
* redshift -->

