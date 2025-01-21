# Reversal Services
This is the backend for the reversal + app. It is a set of micro services.

For running a microservice for local testing, please refer the respective README file.

### Prerequisite

Download and setup [Docker Desktop](https://www.docker.com/products/docker-desktop/)

Check if docker is installed properly:
```cmd
docker --version
```
Docker comes with docker-compose plugin. If not, you can install it from [here](https://docs.docker.com/compose/install/).
```cmd
docker-compose --version
```


### Starting the services

```cmd
docker-compose up --build
/* the above command picks the config from the docker-compose.yml file */
```



