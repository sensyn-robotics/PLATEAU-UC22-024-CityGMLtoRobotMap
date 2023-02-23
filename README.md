
# 令和4年度 民間ユースケース開発　（UC22-024）「3D都市モデルとBIMを活用したモビリティ自律運行システム」の成果物
# CityGMLtoRobotMap

## 1. 概要
* 「CityGMLtoRobotMap」はCityGMLをRobotが自己位置推定などで使用できる環境地図として変換するためのツール群です。CityGMLからOBJ形式への形式変換・座標変換の機能、OBJファイルの表面をサンプリングして点群を生成できる機能、BIMとCityGMLのマージ機能があります。
* 本ツールは、令和4年度 民間ユースケース開発　（UC22-024）「3D都市モデルとBIMを活用したモビリティ自律運行システム」の中で[SnesynRobotics](https://www.sensyn-robotics.com/)が開発したものです。

## 2．「3D都市モデルとBIMを活用したモビリティ自律運行システム」について
### ユースケースの概要
都市部における建設工事では資材運搬等による交通渋滞が課題となり、自律運航可能なドローンや無人搬送車両（AGV）の活用による解決が期待されています。一方で、ドローンではGPS測位のみの飛行では受信状況が悪いビルの間などでは正確で安全な飛行を担保できないことがあります。さらに、ドローン・AGVともに運航に必要な地図情報として民間事業者が提供する3Dマップを利用せざるを得ないことから、精度担保やデータ連携、カバレッジ等の点で課題があります。
本ユースケースでは、これらの課題を解決し、資材運搬等を担うドローンやAGVの自律運行が可能となるような、LiDARやGPS等のセンサーと3D都市モデルを利用した自己位置測位を組み合わせた運航システムを開発しました。

### 開発システムの概要
ドローンの自律飛行では、屋外は3D都市モデル（建築物モデルLOD2）、屋内はBIMモデルの形状を活用してLiDARとGNSS（衛星測位システム）による自己位置推定を行うドローン自律飛行システムを、ロボット・アプリケーションの作成支援ライブラリ・ツール群であるROSを利用して構築しました。
具体的には3D都市モデル・BIMモデルをマップとして利用するLiDARによる自己位置測位（LiDAR SLAM）を行う仕組みをフルスクラッチで開発するとともに、LiDAR SLAMとGNSSの２つの測位情報を状況に応じて統合又は切り替える「FUSION」と呼ばれるシステムを構築しました。
具体的には、測位状態の良好な状態（数㎝の精度が期待される状態）を閾値として設定し、双方ともに有効な場合は測位結果を統合し、一方の精度が期待できない場合にはもう一方のみに切り替えることで、精度向上と冗長性を図る仕組み（FUSION）を開発しました。
また、3D都市モデル（建築物モデルLOD2）とBIMモデルという形式の異なる２つのモデルを同一のマップに表示するために、それぞれのモデルに原点座標を持たせて統合し、PCL（Point Cloud Library）を使って点群マップ化する方法を構築しました。

## 3．利用手順
### インストール方法
[Install](https://sensyn-robotics.github.io/PLATEAU-UC22-024-CityGMLtoRobotMap/Install.html)を参照してください。

### 使い方
[Usage](https://sensyn-robotics.github.io/PLATEAU-UC22-024-CityGMLtoRobotMap/Usage.html)を参照してください。

## ライセンス
* ソースコードおよび関連ドキュメントの著作権は国土交通省に帰属します。
* 本ドキュメントは[Project PLATEAUのサイトポリシー](https://www.mlit.go.jp/plateau/sitepolicy/)（CCBY4.0および政府標準利用規約2.0）に従い提供されています。

## 注意事項
* 本レポジトリは参考資料として提供しているものです。動作保証は行っておりません。
* 予告なく変更・削除する可能性があります。
* 本レポジトリの利用により生じた損失及び損害等について、国土交通省はいかなる責任も負わないものとします。

## 参考資料
* 3D都市モデルとBIMを活用したモビリティ自律運行システム技術検証レポート: https://www.mlit.go.jp/plateau/libraries/technical-reports/
* PLATEAU Webサイト Use caseページ「3D都市モデルとBIMを活用したモビリティ自律運行システム」: https://www.mlit.go.jp/plateau/use-case/uc22-024/
* （利用しているライブラリなどへのリンク）
  * [cjio](https://github.com/cityjson/cjio)
  * [pyproj](https://github.com/pyproj4/pyproj)
  * [trimesh](https://github.com/mikedh/trimesh)
  * [open3d](https://github.com/isl-org/Open3D)
  * [PyMeshLab](https://github.com/cnr-isti-vclab/PyMeshLab)
