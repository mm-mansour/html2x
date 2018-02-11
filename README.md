# HTML2X
HTML2X is a simple yet powerful tool to convert HTML to PNG, JPG, or PDF files.
The tool uses Firefox browser in its headless mode to render the HTML and then take a screenshot. The file is converted to the needed format using Imagmagick and is served usig Python Flask; there is also a CLI version to convert files directly from command line as opposed to the API option.

The tool is presented in two easy-to-use docker containers built upon the light weight Alpine Linux distribution.

## HTML2X-webservice

### Deployment:

Start by pulling the docker image and deploying it locally. 

```bash
docker pull mwmansour/html2x-webservice
docker run --rm -p 7100:7000 docker pull mwmansour/html2x-webservice 
```

### How to use:

Use the tool directly from your browser with this GET request:

```
http://localhost:7100/?link=https://github.com/
http://localhost:7100/?link=https://github.com/&extension=pdf
http://localhost:7100/?link=https://github.com/&extension=jpg&wh=480,600
```

As you can see there is only a single required parameter, that is "link". You can also choose the target extension (available options are pdf, png, and jpg). Moreover, you can change the viewport using the "wh" argument, passing the desired width,height in pixels. 

Notice that with the webservice tool you cannot convert local files directly. You could use NGINX or any similar service to locally host your files or you could use the CLI tool to convert your files locally.

## HTML2X-cli

### Deployment:

Start by pulling the docker image and deploying it locally. 
```bash
docker pull mwmansour/html2x-cli
```

### How to use:

```bash
docker run --rm -v $(pwd):/exported/ mwmansour/html2x-cli sh html2x.sh "https://github.com/" 
docker run --rm -v $(pwd):/exported/ mwmansour/html2x-cli sh html2x.sh "https://github.com/" --extension pdf
docker run --rm -v $(pwd):/exported/ mwmansour/html2x-cli sh html2x.sh "https://github.com/" --extension jpg --wh 480,600
```

Note that you need to surround your links with double quotation marks. You can still specify the extension and viewport size just as in the webservice mode.

To use the CLI service with a local file, prefix its name with "file:///exported/":

```bash
docker run --rm -v $(pwd):/exported/ mwmansour/html2x-cli sh html2x.sh file:///exported/index.html
```

## Building the containers

If you prefer to build the containers as: you can do so by simply executing the docker_build.sh file after cloning the project.