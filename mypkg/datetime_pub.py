import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime

def main(args=None):
    # ROS 2の初期化
    rclpy.init(args=args)

    # シンプルなノードの作成
    node = Node("datetime")  # この部分で単一のNodeインスタンスを作成
    node.get_logger().info("待機中")

    # パブリッシャーの作成
    publisher = node.create_publisher(String, 'datetime_topic', 10)

    # コールバック関数の定義
    def timer_callback():
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y年%m月%d日 %H:%M:%S")
        weekdays = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
        day_of_week = weekdays[current_time.weekday()]
        message = f"日時: {formatted_time}, 曜日: {day_of_week}"

        msg = String()
        msg.data = message
        publisher.publish(msg)
        node.get_logger().info(f"配信: {message}")

    # タイマーの作成
    timer = node.create_timer(1.0, timer_callback)

    # 10秒後に停止する仕組み
    def stop_node():
        node.get_logger().info("10秒経過。ノードを終了します。")
        rclpy.shutdown()

    node.create_timer(10.0, stop_node)

    # ノードの実行
    rclpy.spin(node)

    # クリーンアップ
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

