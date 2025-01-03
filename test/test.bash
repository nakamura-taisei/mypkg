#!/bin/bash

# デフォルトディレクトリをホームに設定
dir=~
# 引数があれば、そのディレクトリに設定
[ "$1" != "" ] && dir="$1"

# ros2_ws ディレクトリに移動
cd $dir/ros2_ws

# mypkg パッケージをビルド
echo "Building the package..."
colcon build --packages-select mypkg

# ビルドが成功したか確認
if [ $? -ne 0 ]; then
    echo "Error: colcon build failed."
    exit 1
fi

# datetime_weather.launch.py を実行（10秒間タイムアウトし、ログは /tmp/mypkg.log に保存）
echo "Launching the package..."
timeout 10 ros2 launch mypkg datetime_weather.launch.py > /tmp/mypkg.log

