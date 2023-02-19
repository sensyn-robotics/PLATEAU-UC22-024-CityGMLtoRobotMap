
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
基本的には [Github Pages](https://docs.github.com/ja/pages)を使い、初心者向けの手順書を作成ください。
### インストール方法
[Github Pages](https://docs.github.com/ja/pages)を参照してください。

### 使い方
[Github Pages](https://docs.github.com/ja/pages)を参照してください。

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



## インストール方法


確認済動作環境: Ubuntu18,python3.8

1. dependency
   sudo apt install -y build-essential curl libffi-dev libssl-dev zlib1g-dev liblzma-dev libbz2-dev libreadline-dev libsqlite3-dev libncurses5-dev
   libncursesw5-dev tk-dev git 
   sudo apt install default-jre

2. install python 3.8 envirnment

````
curl https://pyenv.run | bash

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

source ~/.bashrc
pyenv install 3.8.13
````

3. python3.8 をinstallした後
````
   pip install --upgrade pip
   pip install poetry
   poetry install
   # swich python environment
   poetry shell
````
4.citygml-tools  
https://github.com/citygml4j/citygml-tools/releases/download/v2.0.0/citygml-tools-2.0.0.zip

2. （BIMを使う場合のみ）ifc converter  
   https://blenderbim.org/docs-python/ifcconvert/installation.html

## 使用手順・方法

1 - CityGMLをobjに変換  
2 - （BIMを使う場合のみ）BIMをobjに変換  
3 - obj から点群生成  
4 - （BIMを使う場合のみ）obj(CityGMLから)とobj(BIM)の位置合わせを行う  
5 - 複数の点群を一つの点群にまとめる

### 1.CityGMLをobjに変換

CityGML形式のデータを

#### create obj model from city gml

まず https://www.geospatial.jp/ckan/dataset/plateau-tokyo23kuからCityGML形式のデータをダウンロードします。
データをダウンロードした後`python3 gml2obj.py　-s path/to/plateau_data/udx --lat 35.6895014 --lon 139.6917337 --alt 30 --mapcodelevel third`
を実行すると$HOME/CG2RM/obj の中にobjファイルが生成されます。
また,次のコマンドを使用することで生成したobjファイルを表示することができます。
`python3 view_obj.py $HOME/CG2RM/obj_file.obj`

##### extract lod3

`./citygml-tools-2.0.0/citygml-tools filter-lods --lod=3 --mode=maximum *.gml`

### 2.BIMを使う場合のみ）BIMをobjに変換

BIMをobjに変換する場合はIfcConvertを使用します。以下のコマンドで変換を行います。
`./IfcConvert input_bim.ifc output_obj.obj`

### 3.obj から点群生成

生成したobjファイルからメッシュ表面をサンプリングすることで点群を生成します。以下のコマンドで実行します。densityは面積あたりにサンプリングする点群の数の目安です。
`python create_sampling_point_cloud.py -f $HOME/CG2RM/obj/obj_file.obj --density 30`
コマンドを実行すると$HOME/CG2RM/pointcloud の中にply,とpcdファイルが生成されます。

### 4.（BIMを使う場合のみ）obj(CityGMLから)とobj(BIM)の位置合わせを行う

位置合わせを行いたいobj(CityGMLから)とobj(BIM)とそれぞれから生成された点群を指定し
`python3 align_bim.py`コマンドを実行することでCityGMLが持つ座標系に合うようにBIMを位置調整した結果が得られます。

### 5.複数の点群を一つの点群にまとめる

複数の点群ファイルを一つに統一する場合、以下のコマンドを実行することで統合することが可能です。
`python3 create_sampling_point_cloud.py -f file_1.pcd file_2.pcd ...`

