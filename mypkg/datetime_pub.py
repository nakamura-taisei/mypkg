import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime

class DateTimePublisher(Node):
    def __init__(self):
        super().__init__('datetime_publisher')
        self.publisher_ = self.create_publisher(String, 'datetime_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_message)  # 1秒ごとに実行
        self.start_time = self.get_clock().now()  # 開始時間を記録
        self.timer_10s = self.create_timer(10.0, self.stop_node)  # 10秒後に停止
        self.count = 0

    def publish_message(self):
        self.count += 1
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y年%m月%d日 %H:%M:%S")
        weekdays = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
        day_of_week = weekdays[current_time.weekday()]
        message = f"カウント: {self.count}, 日時: {formatted_time}, 曜日: {day_of_week}"
        msg = String()
        msg.data = message
        self.publisher_.publish(msg)
        self.get_logger().info(f"配信: {message}")

    def stop_node(self):
        self.get_logger().info("10秒経過。ノードを終了します。")
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = DateTimePublisher()
    rclpy.spin(node)
    node.destroy_node()

if __name__ == '__main__':
    main()

