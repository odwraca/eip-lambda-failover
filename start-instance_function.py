import json
import boto3

def lambda_handler(event, context):
    ec2_client=boto3.client('ec2')
    response = ec2_client.start_instances(InstanceIds=['i-0b7a613c9e0fc58ab',],)

print ('Started EC2 Instance')