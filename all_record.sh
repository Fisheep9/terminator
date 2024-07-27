#!/bin/bash
get_doc_num(){
    local doc_num=$(ls ./bag/ | grep $name | wc -l)
    echo $doc_num
}

name="all_hi_arm_"
doc_num=$(get_doc_num)
name+=${doc_num}
echo $name
rosbag record -a -o ./bag/$name
