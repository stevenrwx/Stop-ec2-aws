import boto3

ec2_client = boto3.client(
    'ec2', 
    aws_access_key_id = "",
    aws_secret_access_key = "",
    region_name='eu-west-2'
)

filters = [{'Name': 'instance-state-name', 'Values': ['running']}]

ec2 = ec2_client.describe_instances(Filters=filters)

instance_ids = []
arns = []
instance_role_arn = "<your_approved_instance_iam_arn>"


def get_instances(ec2):

    for i in ec2['Reservations']:
        for instances in i['Instances']:
            if 'IamInstanceProfile' in instances:
                arn = str(instances['IamInstanceProfile']['Arn'])
                if arn != instance_role_arn:
                    global instance_ids
                    instance_ids.append(instances['InstanceId'])
                    global arns
                    arns.append(arn)
            else:
                    no_iam = instances['InstanceId']
                    print(f"instances running without Iam Role attached: ", no_iam)

            return instance_ids, arns

print(get_instances(ec2))


def stop_ec2():
        for ids in instance_ids:
            id = str(ids)
            ec2_client.stop_instances(InstanceIds=[id])
            print(f"stopping :", id)

stop_ec2()
