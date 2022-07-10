import boto3 
ec2_client=boto3.client("ec2")

delete=ec2_client.delete_snapshot(
    SnapshotId='snap-0a802d2ff1e23a914',
    DryRun=True|False
)

print(delete)