import boto3 
ec2_client=boto3.client("ec2")

delete=ec2_client.delete_snapshot(
    SnapshotId='snap-xxxxxxxxxxxxxxxxxx',
    DryRun=False
)

import pprint; pprint.pprint(delete)