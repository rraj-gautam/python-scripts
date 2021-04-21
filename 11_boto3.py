import boto3


s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)    

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
# print(response)    

import json
print(json.dumps(response, indent=4))