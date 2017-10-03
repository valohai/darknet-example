You don't need to do this if you can use the already built version defined in your `valohai.yaml`.

```bash
# Check latest darknet commit id at https://github.com/pjreddie/darknet for naming the image.
62b781a

# Build the Dockerfile to an image, change name to whatever Docker repo you will be using.
nvidia-docker build -t valohai/darknet:62b781a-cuda8.0-cudnn5-devel-ubuntu16.04 .

# Check that it works.
nvidia-docker run --rm valohai/darknet:62b781a-cuda8.0-cudnn5-devel-ubuntu16.04 /darknet/darknet
# => usage: /darknet/darknet <function>
```
