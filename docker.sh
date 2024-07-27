#!/bin/bash

cd scripts

layout_name="hi-arm"
terminal_num=6

container_id="0c76"

python3 docker.py $layout_name $terminal_num $container_id