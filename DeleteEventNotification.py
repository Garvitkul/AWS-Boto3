import boto3
s3 = boto3.resource('s3')

Bucket_Name = 'bucket_name'

bucket_notification = s3.BucketNotification(Bucket_Name)

response = bucket_notification.put(
    NotificationConfiguration={
    },
)

print(response)

















































# response = s3.put_bucket_notification_configuration(
#     Bucket='phonsourcebucket',
#     NotificationConfiguration={
#         'LambdaFunctionConfigurations': [
#             {
#                 'Id': 'string',
#                 'LambdaFunctionArn': 'arn:aws:lambda:us-east-1:146366115606:function:VideoToAudioLambda',
#                 'Events': [
#                     's3:ObjectCreated:*'
#                 ],
#             },
#         ],
#     },
# #    ExpectedBucketOwner='string',
# #    SkipDestinationValidation=True|False
# )

# print(response)


# response = client.put_bucket_notification_configuration(
#     Bucket='phonsourcebucket',
#     NotificationConfiguration={
#         'LambdaFunctionConfigurations': [
#             {
#                 'Id': 'string',
#                 'LambdaFunctionArn': 'arn:aws:lambda:us-east-1:146366115606:function:VideoToAudiolambda',
#                 'Events': [
#                     's3:ObjectCreated:*'
#                 ],
#             },
#         ],
#     },
# #    ExpectedBucketOwner='string',
# #    SkipDestinationValidation=True|False
# )
# Bucket='phonsourcebucket',
# NotificationConfiguration={
#     'LambdaFunctionConfigurations': [
#         {
#             'Id': 'string',
#             'LambdaFunctionArn': 'arn:aws:lambda:us-east-1:146366115606:function:VideoToAudiolambda',
#             'Events': [
#                 's3:ObjectCreated:*'
#             ],
#         },
#     ],
# }

# client.put_bucket_notification_configuration(**kwargs)
# client.put_bucket_notification_configuration(Bucket, **NotificationConfiguration)
# response = bucket_notification.put(
#     NotificationConfiguration={'LambdaFunctionConfigurations': [
#         {
#             'LambdaFunctionArn': 'arn:aws:lambda:us-east-1:146366115606:function:VideoToAudiolambda',
#             'Events': [
#             's3:ObjectCreated:*'
#             ],

#         },
#     ]})