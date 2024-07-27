#!/bin/bash

cd scripts

layout_name="hi-arm"
terminal_num=6

ssh_ip="n5@10.1.1.64"
container_id="0c76"

python3 ssh_docker.py $layout_name $terminal_num $ssh_ip $container_id