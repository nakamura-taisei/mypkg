import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import datetime
import locale

class WeatherSubscriber(Node):
    def __init__(self):
        super().__init__('weather_subscriber')
        self.subscription = self.create_subscription(
            String,
            'datetime_topic',
            self.callback,
            10
        )
        self.subscription  # 購読を有効化
        self.start_time = self.get_clock().now()  # 開始時間を記録
        self.timer_10s = self.create_timer(10.0, self.stop_node)  # 10秒後に停止

    def callback(self, msg):
        try:
            # 受信データをISO形式の日付として解析
            datetime_obj = datetime.datetime.fromisoformat(msg.data)
            # 和暦に変換
            wareki = self.convert_to_wareki(datetime_obj)

            # ログに表示
            self.get_logger().info(f"受信日時: {msg.data}")
            self.get_logger().info(f"和暦: {wareki}")
        except ValueError as e:
            self.get_logger().error(f"日時データの解析に失敗しました: {e}")

    def convert_to_wareki(self, dt):
        # 和暦変換（日本語ロケール設定）
        era_map = {
            (2019, 5, 1): ("令和", 2019),  # 令和
            (1989, 1, 8): ("平成", 1989),  # 平成
            (1926, 12, 25): ("昭和", 1926),  # 昭和
            (1912, 7, 30): ("大正", 1912),  # 大正
            (1868, 1, 25): ("明治", 1868),  # 明治
        }

        for start_date, (era_name, era_start) in sorted(era_map.items(), reverse=True):
            if dt >= datetime.datetime(*start_date):
                year_in_era = dt.year - era_start + 1
                era_year = "元" if year_in_era == 1 else str(year_in_era)
                return f"{era_name}{era_year}年{dt.month}月{dt.day}日（{self.get_weekday_jp(dt)}）"

        return "不明な元号"

    def get_weekday_jp(self, dt):
        # 日本語の曜日を取得
        locale.setlocale(locale.LC_TIME, 'ja_JP.UTF-8')
        return dt.strftime("%A")

    def stop_node(self):
        self.get_logger().info("10秒経過。ノードを終了します。")
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = WeatherSubscriber()
    rclpy.spin(node)
    node.destroy_node()

if __name__ == '__main__':
    main()

