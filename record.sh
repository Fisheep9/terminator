#!/bin/bash
get_doc_num(){
    local doc_num=$(ls ./bag/ | grep $name | wc -l)
    echo $doc_num
}

name="hi_arm_"
doc_num=$(get_doc_num)
name+=${doc_num}
echo $name
# rosbag record -a -o ./bag/$name

rosbag record -O /home/hilab/code/script_repo/bag/$name /mavros/debug_value/debug_vector /position_cmd_delta /current_pose_delta /ekf/ekf_odom /endeffector_status