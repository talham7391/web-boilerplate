import boto3


def to_cloud(stack_name, cluster_name, image_name, app_port="8080"):
    cf_client = boto3.client("cloudformation")
    with open("templates/infrastructure.yaml") as f:
        template_body = f.read()
    cf_client.create_stack(
        StackName=stack_name,
        TemplateBody=template_body,
        Parameters=[{
            "ParameterKey": "ClusterName",
            "ParameterValue": cluster_name,
        }, {
            "ParameterKey": "AppImage",
            "ParameterValue": image_name,
        }, {
            "ParameterKey": "AppPort",
            "ParameterValue": app_port,
        }],
        Capabilities=["CAPABILITY_IAM"],
    )
