# Stop and remove app_config docker container that hosts Rokwire App Config API
sudo apt-get update
if [ -x "$(command -v docker)" ]; then
    echo "Update Docker"
    sudo apt-get --only-upgrade install docker.io
else
    echo "Install Docker"
    #install docker from Ubuntu repository
    sudo apt-get install docker.io
fi

name="app_config"

matchingStarted=$(sudo docker ps --filter="name=$name" -q | xargs)
if [ ! -z $matchingStarted ]; then 
    echo "Stop app_config docker container"
    sudo docker stop $matchingStarted
fi

matching=$(sudo docker container ls -a --filter="name=$name" -q | xargs)
if [ ! -z $matching ]; then
    echo "Remove app_config docker container"
    sudo docker rm $matching
fi