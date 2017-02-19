
Darknet on Valohai Example
==========================

Building the Docker Image
-------------------------

You don't need to do this if you can use the already built version defined in the YAML.

```bash
# Check latest darknet commit id at https://github.com/pjreddie/darknet for naming the image.
b61bcf5

# Build the Dockerfile to an image, change name to whatever Docker repo you will be using.
nvidia-docker build -t 905675611115.dkr.ecr.eu-west-1.amazonaws.com/valohai/darknet:gpu-b61bcf5 ./gpu

# Check that it works.
nvidia-docker run --rm 905675611115.dkr.ecr.eu-west-1.amazonaws.com/valohai/darknet:gpu-b61bcf5 /darknet/darknet
# => usage: /darknet/darknet <function>

# Push to the Docker repository.
`aws ecr get-login --region eu-west-1` # required only in AWS ECR context.
nvidia-docker push 905675611115.dkr.ecr.eu-west-1.amazonaws.com/valohai/darknet:gpu-b61bcf5
```
