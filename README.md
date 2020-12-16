# EIP Lambda Failover to EC2 Instance

## Usage
This is simple example Lambda function that will allow you to 'failover' an Elastic IP address.

## Setup
This is using Python 3.8

Create a new function, author from scratch and edit the python script to reflect an EIP allocation ID and instance ID (the target) that you would like to move the EIP to.

1. Create a topic for SNS to capture events.
2. Create a Cloudwatch alarm to trigger based upon your needs. For example, a healthcheck of some kind.
3. Create a trigger for your Lambda Function for SNS and use the topic that is receiving your events. 

## Possible upgrades
Spin up a replacement server in a different AZ via an AMI.

### Caveats
This would only work if the server was on standby and the use case would be for some reason, a Network Load Balancer was not possible. 
