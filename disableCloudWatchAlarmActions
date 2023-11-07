import boto3

client = boto3.client('cloudwatch')

try:
    response = client.disable_alarm_actions(
        AlarmNames=[
            'AlarmName1',
            'AlarmName2',
]
)
    print(response, "The alarms are disabled.")

except Exception as e:
  print(f"Error disabling CloudWatch alarms: {e}")

