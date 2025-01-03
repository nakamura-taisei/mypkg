import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    # datetime_pub.py ノードの設定
    datetime_pub_node = launch_ros.actions.Node(
        package='mypkg',      # パッケージの名前
        executable='datetime_pub',  # 実行するファイルの名前
        output='screen'  # ログを端末に表示
    )
    
    # weather_sub.py ノードの設定
    weather_sub_node = launch_ros.actions.Node(
        package='mypkg',  # パッケージ名
        executable='weather_sub',  # 実行するファイルの名前
        output='screen'  # ログを端末に表示
    )

    return launch.LaunchDescription([datetime_pub_node, weather_sub_node])

