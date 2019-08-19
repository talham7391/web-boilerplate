import boto3

ec2_client = boto3.client("ec2")


def get_instance_ipv4_address(instance_id):
    ipv4_addresses = []
    result = ec2_client.describe_instances(InstanceIds=[instance_id])
    for reservation in result["Reservations"]:
        for instance in reservation["Instances"]:
            ipv4_addresses.append(instance["PublicIpAddress"])
    if len(ipv4_addresses) == 0:
        return None
    else:
        return ipv4_addresses[0]
