# lenme Back-End Test

## Change .sh file permissions
* Linux chmod +x entrypoint.sh
* Windows dos2unix.exe entrypoint.sh

## Build image
* docker-compose build

## Run Container
* docker-compose up

## Stop all docker containers
* docker stop $(docker ps -aq)
