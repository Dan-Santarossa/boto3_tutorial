import boto3

s3_resource=boto3.client("s3")

#print out specific bucket name by value. 4 is the 5th bucket you created !is hardcoded
s3_name=s3_resource.list_buckets()["Buckets"][4]["Name"]
print(s3_name)

#print out the creation date of the 1st bucket !is hardcoded
creation_date=s3_resource.list_buckets()["Buckets"][0]["CreationDate"] 
print(creation_date)

#print out the creation date of the 5th bucket formatted
creation_date1=creation_date.strftime("%d%m%y_%H:%M:%s")
print(creation_date1)

#print out dictionary of buckets w/ name, creation date
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket)

#print the name of bucket and the creation date   
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])