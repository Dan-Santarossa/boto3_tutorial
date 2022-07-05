import boto3
s3_resource=boto3.client("s3")

#list out a dictionary of contents                    #add ["Contents"] to get a list
objects=(s3_resource.list_objects(Bucket="totaltech"))["Contents"]

#if len(objects)>0:
    #print("dummy thing")

for object in objects:
    print(object["Key"])