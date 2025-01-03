#!/bin/bash

# デフォルトディレクトリをホームに設定
dir=~
# 引数があれば、そのディレクトリに設定
[ "$1" != "" ] && dir="$1"

# ros2_ws ディレクトリに移動
cd $dir/ros2_ws

# ROS 2 の環境設定
source /opt/ros/foxy/setup.bash  # 適切なディストリビューションを指定
source $dir/ros2_ws/install/setup.bash

# mypkg パッケージをビルド
colcon build --packages-select mypkg

# datetime_weather.launch.py を実行（10秒間タイムアウトし、ログは /tmp/mypkg.log に保存）
timeout 10 ros2 launch mypkg datetime_weather.launch.py > /tmp/mypkg.log

