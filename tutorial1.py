#!/usr/bin/env python3.7
import boto3
#create s3 bucket in us-east-2 region
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("totaltech-private")
response = bucket.create(
    ACL='private',
    CreateBucketConfiguration={
        'LocationConstraint':'us-east-2'
    },
   
)

print(response)