# EIP Lambda Failover to EC2 Instance

## Use Case
This is simple example Lambda function that will start an EC2 instance and 'failover' an Elastic IP address to the previously powered off instance. This could be useful if you have an appliance that never readily changes and you deploy a copy of that in a powered off state in a separate availability zone. 

## Setup
This is using Python 3.8

Create a new function, author from scratch and edit the python script to reflect an EIP allocation ID and instance ID (the target) that you would like to move the EIP to. You will use the [lambda_function.py](https://github.com/odwraca/eip-lambda-failover/blob/main/lambda_function.py) for this purpose. 

Create a second function from scratch using [start-instance_function.py](https://github.com/odwraca/eip-lambda-failover/blob/main/start-instance_function.py) and then update your InstanceIds to your target instance ID.

For both functions, make sure your permissions in the execution role are set for your Lambda function to access the EC2 actions required in your function. 

1. Create a topic for SNS to capture events.
2. Create a Cloudwatch alarm to trigger based upon your needs and target the newly created SNS topic. Here are a few examples:
  - [R53 Health Check - Endpoint or IP](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-types.html)
  - [Instance Status Check](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html#types-of-instance-status-checks)
3. Go to your EIP Allocation Lambda function and add the following: 
  - Create a trigger for your Lambda Function for SNS and use the topic that is receiving your events. 
  - Create a destination with the condition of "On Success" and target the EC2 Start Instance function.

Don't forget to save and deploy your package.

At this point your function should look like this:
![Lambda EIP Failover](https://i.imgur.com/So78bzv.png "Lambda EIP Failover")


## Possible upgrades
* Spin up a replacement server in a different AZ via an AMI. 
* Build in additional protections. 
* Automatic failback
* Amazon Eventbridge Integration for Ops Items

### Caveats
* I would only recommend using this where leveraging a Network or Application Load Balancer is not possible. 
* This is not built to fail back automatically and will be a manual effort.
