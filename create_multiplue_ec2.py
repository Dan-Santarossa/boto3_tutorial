import boto3

ec2_resource=boto3.resource("ec2", "us-east-2")#created for us-east-2 obliterate env

ec2_resource.create_instances(ImageId='ami-02d1e544b84bf7502', 
    InstanceType='t2.micro',
    MaxCount=5,
    MinCount=3)
