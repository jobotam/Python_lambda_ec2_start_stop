import boto3
# instanceid = ['i-0f636df6cc6b0d432']
region = "ap-east-1"
ec2 = boto3.client('ec2', region_name = region)

def lambda_handler(event, context):
    # TODO implement
    ec2_tag_filter = [{'Name':'tag:ecv', 'Values':['test']}]
    ec2_instances = ec2.describe_instances(Filters=ec2_tag_filter)
    ec2_reservation = ec2_instances['Reservations'] 
        
    for instances_info in ec2_reservation:
        instance = instances_info['Instances']
        for instance_id in instance:
            response = instance_id['State']
            instance_id = instance_id['InstanceId']
            # print(instance_id)
            # response = ec2.describe_instance_status(InstanceIds=[instance_id],IncludeAllInstances=True)
            if response['Name'] == 'stopped' :
            # if response['InstanceStatuses'][0]['InstanceState']['Name'] == 'stopped':
                ec2.start_instances(InstanceIds=[instance_id])
                print('started your instances: ' + str(instance_id)) 
            else :
                # print('the state of instances of ' +  str(instance_id) + ' is ' +  response['InstanceStatuses'][0]['InstanceState']['Name'])
                print('the state of instances of ' +  str(instance_id) + ' is ' + str(response))
                
    # response = ec2.describe_instance_status(InstanceIds=[event['param1'],event['param2']],IncludeAllInstances=True)
    # if response['InstanceStatuses'][0]['InstanceState']['Name'] == 'stopped':
    # # print(response['InstanceStatuses'][0]['InstanceState']['Name'])
    #     ec2.start_instances(InstanceIds=[event['param1'],event['param2']])
    #     print('started your instances: ' + str(event))
    # else :
    #     print('the state of instances is ' +  response['InstanceStatuses'][0]['InstanceState']['Name'])
    return {
        # 'statusCode': 200,
        # 'body': json.dumps('Hello from Lambda!')
    }
