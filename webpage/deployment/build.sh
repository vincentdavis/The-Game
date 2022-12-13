#!/bin/sh

docker build -t the-game-web-image:prd -f Dockerfile .
if [ `echo $?` == 0 ]; then
	docker rm -f the-game-web
	docker run -dt --restart=always -p 8010:8010 --name the-game-web the-game-web-image:prd
fi


