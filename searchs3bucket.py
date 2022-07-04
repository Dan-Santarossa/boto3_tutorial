import boto3

resource=boto3.resource("s3")
list(resource.buckets.all())

for bucket in resource.buckets.all():
    print(bucket.name)