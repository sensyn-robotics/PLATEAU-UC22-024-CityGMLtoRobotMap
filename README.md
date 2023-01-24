
# CityGMLtoRobotMap

## install 
ubuntu18 上で動作確認を行いました。

1. citygml-tools  
https://github.com/citygml4j/citygml-tools/releases/download/v2.0.0/citygml-tools-2.0.0.zip

2. （BIMを使う場合のみ）ifc converter　  
https://blenderbim.org/docs-python/ifcconvert/installation.html

3. python3.8 をinstallした後  
`pip3 install poetry`  
`poetry install`


## 使用手順・方法
1 - CityGMLをobjに変換  
2 - （BIMを使う場合のみ）BIMをobjに変換  
3 - obj から点群生成  
4 - （BIMを使う場合のみ）obj(CityGMLから)とobj(BIM)の位置合わせを行う  
5 - 複数の点群を一つの点群にまとめる  

### 1.CityGMLをobjに変換
CityGML形式のデータを
#### create obj model from city gml
まず https://www.geospatial.jp/ckan/dataset/plateau-tokyo23ku　からCityGML形式のデータをダウンロードします。 
データをダウンロードした後`python3 gml2obj.py　-s path/to/plateau_data/udx --lat 35.6895014 --lon 139.6917337 --alt 30 --mapcodelevel third`
を実行すると$HOME/CG2RM/obj　の中にobjファイルが生成されます。
また,次のコマンドを使用することで生成したobjファイルを表示することができます。
`python3 view_obj.py $HOME/CG2RM/obj_file.obj`

#####  extract lod3
`./citygml-tools-2.0.0/citygml-tools filter-lods --lod=3 --mode=maximum *.gml`

### 2.BIMを使う場合のみ）BIMをobjに変換
BIMをobjに変換する場合はIfcConvertを使用します。以下のコマンドで変換を行います。
`./IfcConvert input_bim.ifc output_obj.obj`

### 3.obj から点群生成
生成したobjファイルからメッシュ表面をサンプリングすることで点群を生成します。以下のコマンドで実行します。densityは面積あたりにサンプリングする点群の数の目安です。
`python create_sampling_point_cloud.py -f $HOME/CG2RM/obj/obj_file.obj --density 30`
コマンドを実行すると$HOME/CG2RM/pointcloud　の中にply,とpcdファイルが生成されます。

### 4.（BIMを使う場合のみ）obj(CityGMLから)とobj(BIM)の位置合わせを行う
位置合わせを行いたいobj(CityGMLから)とobj(BIM)とそれぞれから生成された点群を指定し
`python3 align_bim.py`コマンドを実行することでCityGMLが持つ座標系に合うようにBIMを位置調整した結果が得られます。

### 5.複数の点群を一つの点群にまとめる
複数の点群ファイルを一つに統一する場合、以下のコマンドを実行することで統合することが可能です。
`python3 create_sampling_point_cloud.py -f file_1.pcd file_2.pcd ...`