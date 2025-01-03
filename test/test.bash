#!/bin/bash

# デフォルトディレクトリをホームに設定
dir=~
# 引数があれば、そのディレクトリに設定
[ "$1" != "" ] && dir="$1"

# ros2_ws ディレクトリに移動
cd $dir/ros2_ws

# mypkg パッケージをビルド
colcon build --packages-select mypkg

# ros2_ws をソース
source $dir/ros2_ws/install/setup.bash

# datetime_weather.launch.py を実行（10秒間タイムアウトし、ログは /tmp/mypkg.log に保存）
timeout 10 ros2 launch mypkg datetime_weather.launch.py > /tmp/mypkg.log

