#!/usr/bin/env python3.7
#descibe VPCs with boto3

import boto3

client=boto3.client("ec2")

x=client.describe_vpcs()

no_of_vpcs=x["Vpcs"]

len(no_of_vpcs)

#print amount of vpcs in my account 
print(len(no_of_vpcs))
print(no_of_vpcs)
print("")

#print specific attributes for my vpcs
for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    print(vpc["InstanceTenancy"])
    print(vpc["CidrBlock"])
    
#how to describe one vpc based on vpc id
y=client.describe_vpcs(VpcIds=["vpc-0bbf93ba870e43c99"])
print("")
print(y)