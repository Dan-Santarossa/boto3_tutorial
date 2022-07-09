import boto3
import pprint 

ec2=boto3.client("ec2")
# x=ec2_client.describe_instances() #describe instances and their details
# data=x["Reservations"][3]#print the details of the first instance. 0 represents the first instance
# data_instance=data["Instances"]
# for i in range (len(data_instance)):
#     print(f"instance id is {data_instance[i]['InstanceId']}")

#only getting the result of one instance ID. it is t he result of whatever int in on the 6th line

all_ec2_instance = ec2.describe_instances()
for reservation in all_ec2_instance["Reservations"]:
    for instance in reservation["Instances"]:
        print("Instance Id : {}".format(instance["InstanceId"]))

#found a better way anyway^^^^^