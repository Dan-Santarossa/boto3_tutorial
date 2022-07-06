#!/usr/bin/env python3.7
#descibe VPCs with boto3

import boto3

client=boto3.client("ec2")

x=client.describe_vpcs()

no_of_vpcs=x["Vpcs"]

len(no_of_vpcs)

print(no_of_vpcs)
print("")

for vpc in no_of_vpcs:
    print(vpc["VpcId"])
    print(vpc["InstanceTenancy"])
    print(vpc["CidrBlock"])