# mypkg
- このパッケージは、ROS2の一部を使用して作成したものです。パブリッシャーとサブスクライバーのノードを使って、現在の日時を1秒ごとに配信し、和暦に変換して表示します。

## テスト環境
[![Build Status](https://img.shields.io/github/workflow/status/nakamura-taisei/mypkg/ROS%202%20CI?label=test&logo=github)](https://github.com/nakamura-taisei/mypkg/actions)

## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.7~3.10

## テスト環境  
- ubuntu 20.04 LTS  
- ROS 2: Foxy  
- Python: 3.8  

## 概要
- パブリッシャは現在の日時を1秒ごとに配信し、サブスクライバはその日時を受け取り、和暦に変換して表示します。
- 実行後10秒で自動的に停止する仕組みもあり、簡単にデモを試すことができます。

## 特徴  
- このシステムは、パブリッシャーノードが現在の日時を1秒ごとに配信し、その日時をサブスクライバーノードが受信します。サブスクライバーノードでは、受信した日時を和暦に変換して表示する機能を持っています  

## ノードとトピック

- ノード名: `datetime_publisher`
  - 公開トピック: `/current_datetime` (型: `std_msgs/String`)
- ノード名: `wareki_converter`
  - 購読トピック: `/current_datetime` (型: `std_msgs/String`)

## 実行方法
- cd mypkg

- パブリッシャ
  - ros2 run mypkg datetime_pub.py
- サブスクライバ
  - ros2 run mypkg japanese_sub.py

## 動作  
- パブリッシャ  
日時: 2025年01月04日 12:00:00, 曜日: 土曜日  

- サブスクライバ  
和暦: 令和7年1月4日(土曜日)
## ライセンス
- このソフトウェアパッケージは3条項BSDライセンスの下，再頒布および使用が許可されます．- © 2024 nakamura-taisei
