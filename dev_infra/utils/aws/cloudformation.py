import boto3

cf_client = boto3.client("cloudformation")


def get_ec2s_from_stack(stack_name):
    ec2_instances = []
    stack = cf_client.describe_stack_resources(StackName=stack_name)
    as_client = boto3.client("autoscaling")
    for resource in stack["StackResources"]:
        if resource["ResourceType"] == "AWS::AutoScaling::AutoScalingGroup":
            output = as_client.describe_auto_scaling_groups(
                AutoScalingGroupNames=[resource["PhysicalResourceId"]]
            )
            for asg in output["AutoScalingGroups"]:
                for instance in asg["Instances"]:
                    ec2_instances.append(instance)
    return ec2_instances
