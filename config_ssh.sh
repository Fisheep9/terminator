#!/bin/bash

ssh_ip="n3@10.1.1.173"

# 生成SSH密钥对（如果尚未存在）
if [ ! -f ~/.ssh/id_rsa ]; then
    ssh-keygen -t rsa -N "" -f ~/.ssh/id_rsa
fi

echo "ssh-keygen success"

# 将公钥复制到远程服务器
ssh-copy-id $ssh_ip

echo "ssh-copy-id success"