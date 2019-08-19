import click
from dev_infra import deploy
from dev_infra.utils.aws import cloudformation
from dev_infra.utils.aws import ec2


@click.group()
def cli():
    pass


@cli.command()
@click.option("--service-name", default="web-service")
@click.option("--image-name")
def cloud_deploy(service_name, image_name):
    stack_name = f"{service_name}-stack"
    cluster_name = f"{service_name}-cluster"
    deploy.to_cloud(stack_name, cluster_name, image_name)


@cli.command()
@click.option("--service-name", default="web-service")
def cloud_deploy_address(service_name):
    stack_name = f"{service_name}-stack"
    instances = cloudformation.get_ec2s_from_stack(stack_name)
    for instance in instances:
        address = ec2.get_instance_ipv4_address(instance["InstanceId"])
        print(address)


if __name__ == "__main__":
    cli()
