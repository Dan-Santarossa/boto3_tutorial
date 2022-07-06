import boto3

s3_resource=boto3.client("s3")
#delete single object from s3 bucket -completed
s3_resource.delete_object(Bucket='totaltech',
    Key='multipletest.txt')
    
#delete multiple objects from bucket
import os
import glob

#cwd=os.getcwd()

objects=s3_resource.list_objects(Bucket="totaltech")["Contents"]
print(objects)

for object in objects:
    print(object["Key"])