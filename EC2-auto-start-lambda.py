import boto3

def lambda_handler(event, context):
    region = context.invoked_function_arn.split(":")[3]
    ec2 = boto3.client('ec2', region_name=region)
    
    instances = list_instances_by_tag_value(ec2, "Scheduled", ["Start", "Start,Stop", "Start, Stop"])
    
    ec2.start_instances(InstanceIds=instances)
    print('Started your instances: {0}'.format(str(instances)))
    
def list_instances_by_tag_value(ec2_obj, tagkey, tagvalue):
    response = ec2_obj.describe_instances(
        Filters=[
            {
                'Name': 'tag:'+tagkey,
                'Values': tagvalue
            }
        ]
    )
    instancelist = []
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            instancelist.append(instance["InstanceId"])
    return instancelist