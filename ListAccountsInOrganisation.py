# Import libraries
import boto3

accountNo = "<accountNo"
role = "<role>"

# Define a function to assume role in the AWS account and provide temporary credentials
def assumeRole(accountNo):
    # Initialize the STS client
    sts_client = boto3.client('sts')
    # Assume the role in AWS account
    response = sts_client.assume_role(
        RoleArn=f"arn:aws:iam::{accountNo}:role/{role}",
        RoleSessionName="MySession",
        DurationSeconds=900 # You can change this based on your requirement - It is the session active time
    )
    # Extract the temporary credentials from the response
    credentials = response['Credentials']
    # Return credentials
    return credentials

# Define a function to create session using temporary credentials
def create_session(accountNo):
    # Get the temporary credentials by assuming the role
    credentials = assumeRole(accountNo)
    
    # Create a boto3 session with the temporary credentials
    session = boto3.Session(
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken']
    )    
    # Return the session
    return session

def getAccounts(accountNo):
    accounts = []
    session = create_session(accountNo)
    client = session.client('organizations')
    paginator = client.get_paginator('list_accounts')
    page_iterator = paginator.paginate()
    for page in page_iterator:        
        for acct in page['Accounts']:
            accounts.append(acct)
    return accounts

accounts = getAccounts(accountNo)
print(accounts)
