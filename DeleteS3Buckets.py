import boto3
client = boto3.client('s3')

bucketname = "Bucket_Name"

response = client.delete_bucket(
    Bucket='bucketname',
)
print(response)