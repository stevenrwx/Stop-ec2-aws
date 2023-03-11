# Stop-ec2-aws

- Python script checks all EC2 instances running in eu-west-2 region and verifies that the IAM role attached is the correct one specified in the ''' instance_role_arn ''' variable
- Instances that aren't using the approved instance IAM role will be stopped

### Python preq

- Python 3.9.16
- boto3 library
- aws_access_key_id
- aws_secret_access_key
- instance_role_arn = "<your_approved_instance_iam_arn>"
