import boto3
client = boto3.client('s3')

bucketlist = client.list_buckets()
print(bucketlist)