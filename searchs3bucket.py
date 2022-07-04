import boto3

resource=boto3.resource("s3")

bucket_list=list(resource.buckets.all())


for bucket in resource.buckets.all():
    print(bucket_list)