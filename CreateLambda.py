import boto3

client = boto3.client('lambda')

response = client.create_function(
    Code={
        'S3Bucket': 'Bucket_Name_Where_Your_Code_Resides',
        'S3Key': 'code.zip',
    },
    FunctionName='Function_Name',
    Handler='lambda_handler',
    MemorySize=256,
    Publish=True,
    Role='Role Which Needs To Be Assigned to Lambda to Perform Action',
    Runtime='python3.11',
    Timeout=15,
    TracingConfig={
        'Mode': 'Active',
    },
)

print(response)