#!/bin/bash

# デフォルトディレクトリをホームに設定
dir=~
# 引数があれば、そのディレクトリに設定
[ "$1" != "" ] && dir="$1"

# ros2_ws ディレクトリに移動
cd $dir/ros2_ws

# mypkg パッケージをビルド

colcon build

source $dir/.bashrc
# datetime_weather.launch.py を実行（10秒間タイムアウトし、ログは /tmp/mypkg.log に保存）
timeout 10 ros2 launch mypkg datetime_weather.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'datetime_weather.launch.py: 10'

