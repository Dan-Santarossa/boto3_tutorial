import boto3
s3_resource=boto3.client("s3")

objects=(s3_resource.list_objects(Bucket="totaltech"))["Contents"]

for object in objects:
    print(object["Key"])