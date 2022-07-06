#!/usr/bin/env python3.7
#create a vpc using boto3/python

import boto3

client=boto3.client("ec2") #VPC is associated with EC2

client.create_vpc(CidrBlock='10.0.0.0/16')