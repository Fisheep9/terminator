#!/bin/bash

cd scripts

layout_name="hi-arm"
terminal_num=6

ssh_ip="n3@192.168.1.242"
# ssh_ip="n3@10.1.1.173"
# n5 10.1.1.64
# n3@10.1.1.120
# nv@10.1.1.127

python3 ssh.py $layout_name $terminal_num $ssh_ip