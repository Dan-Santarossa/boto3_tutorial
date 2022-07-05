import boto3
import os
import glob

#how to upload single file
#s3_resource=boto3.client("s3")
#s3_resource.upload_file(
    #Filename="testupload.txt",
    #Bucket="totaltech",
    #Key="testupload")
    
cwd=os.getcwd()

files=glob.glob(cwd+"*.txt")
cwd=cwd+"/"

for file in files:
    s3_resource=boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="totaltech",
    Key=file.split("/"))

print(cwd)    
print(files)    