import boto3

client = boto3.client('cloudwatch')

try:
    response = client.enable_alarm_actions(
        AlarmNames=[
            'AlarmName1',
            'AlarmName2',
            ]
            )
    print(response, "The alarms are enabled.")
    
except Exception as e:
  print(f"Error enabling CloudWatch alarms: {e}")
