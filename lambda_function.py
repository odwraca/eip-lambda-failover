import json
import boto3

def lambda_handler(event, context):
    ec2_client=boto3.client('ec2')
    response = ec2_client.associate_address(AllocationId='eipalloc-0d40dbc72e97b5d67',InstanceId='i-0b7a613c9e0fc58ab',)

print ('Completed EIP Move')