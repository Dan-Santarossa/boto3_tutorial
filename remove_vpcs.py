#!/usr/bin/env python3.7
#how to remove vpcs using python/boto3

import boto3

client=boto3.client("ec2")

response = client.delete_vpc(
    VpcId='vpc-enter vpc id'
)

print(response)

# delete_vpc(**kwargs)
# Deletes the specified VPC. You must detach or delete all gateways and resources that are associated with the VPC before you can delete it. 
# For example, you must terminate all instances running in the VPC, delete all security groups associated with the VPC (except the default one), 
# delete all route tables associated with the VPC (except the default one), and so on.

