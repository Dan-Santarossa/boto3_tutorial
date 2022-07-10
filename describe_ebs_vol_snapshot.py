import boto3


ec2_client=boto3.client("ec2")

response=ec2_client.describe_snapshots(SnapshotIds=['snap-02c33deea886c7537'])
import pprint; pprint.pprint(response)