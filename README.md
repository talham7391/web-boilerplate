# web-boilerplate

Boilerplate to launch any service to AWS easily.

# Infrastructure

Your service will be launched using AWS ECS backed by an EC2 instance. You can modify `templates/infrastructure.yaml` if you need a bigger instance. The default is `t2.micro`.

# Usage

1. Dockerize your service.
2. Build an image, tag it, and publish it to an image registry.
3. Make sure your service listens on a port defined by the environment variable `HOST_PORT`.
4. Make sure your aws credentials are properly setup in `~/.aws`.
5. Run the following commands to launch your infrastructure:
    1. `pipenv install`
    2. `pipenv shell`
    3. `python cli.py cloud-deploy --service-name <service_name> --image-name <image_name_with_tag>`
6. Run `cloud-deploy-address --service-name <service_name>` to get the URL of your service.

# Examples

An example has been provided in the `samples` folder using a simple Golang service.
