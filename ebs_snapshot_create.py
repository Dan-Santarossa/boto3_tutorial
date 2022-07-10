import boto3

#call ec2 client
ec2_client=boto3.client("ec2")

#create snapshot from PythonLUIT instnace in Cloud9
response=ec2_client.create_snapshot(Description='This is my root volume snapshot of PythonLUIT Cloud9.', 
        VolumeId='vol-0982da85cefc9dc9d',) 


import pprint; pprint.pprint(response)