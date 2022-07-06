import boto3

s3_resource=boto3.client("s3")
#delete single object from s3 bucket -completed
s3_resource.delete_object(Bucket='totaltech',
    Key='multipletest.txt')
    
#delete multiple objects from bucket
import os
import glob

#cwd=os.getcwd()
#find all the object from the bucket
objects=s3_resource.list_objects(Bucket="totaltech")["Contents"]
print(objects)

#iteration of objects by key 
for object in objects:
    #print(object["Key"])
    #del all objects in bucket by key
    response=s3_resource.delete_object(Bucket='totaltech',
        Key=object["Key"])
    print(response)