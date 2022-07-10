from urllib import response
import boto3
ec2_client=boto3.client("ec2")

ec2_client.create_volume(AvailabilityZone='us-east-1a',
    Encrypted=True,
    Size=12,
    SnapshotId='snap-0a802d2ff1e23a914',
    VolumeType='gp2')
