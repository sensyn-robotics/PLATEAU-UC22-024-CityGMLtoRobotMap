# 使用手順・方法

1 - CityGMLをobjに変換  
2 - （BIMを使う場合のみ）BIMをobjに変換  
3 - obj から点群生成  
4 - （BIMを使う場合のみ）obj(CityGMLから)とobj(BIM)の位置合わせを行う  
5 - 複数の点群を一つの点群にまとめる

### 1.CityGMLをobjに変換


#### create obj model from city gml
CityGML形式のデータを データをダウンロードした後

https://www.geospatial.jp/ckan/dataset/plateau-tokyo23kuからCityGML形式のデータをダウンロードし解凍します。

「~/Downlods/plateau-tokyo23ku」にファイルがあるとします。
を実行すると$HOME/CG2RM/obj の中にobjファイルが生成されます。

```
python3 gml2obj.py　-s path/to/plateau_data/udx --lat 35.6895014 --lon 139.6917337 --alt 30 --mapcodelevel third
```

```
usage: gml2obj.py [-h] -s SOURCE_DIR --lat LAT --lon LON --alt ALT [--save_dir SAVE_DIR] [-u] [--mapcode_level {first,second,third}] [--lod {max,1,2,3,4}]

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE_DIR, --source_dir SOURCE_DIR
                        pass city gml source directory.
  --lat LAT             Latitude
  --lon LON             Longitude
  --alt ALT             Altitude
  --save_dir SAVE_DIR   output directory
  -u, --update          over write already generated cityjson, filterd_lods.gml files.
  --mapcode_level {first,second,third}
                        map mesh code. first code include large area. third code include small area.
  --lod {max,1,2,3,4}   extract lods. if use choose 1~4 , this filter only extract same level lods. If you choose max. extract max level lod from same building.

```



また,次のコマンドを使用することで生成したobjファイルを表示することができます。
```
python3 view_obj.py $HOME/CG2RM/obj_file.obj
```


### 2.BIMを使う場合のみ）BIMをobjに変換

BIMをobjに変換する場合はIfcConvertを使用します。以下のコマンドで変換を行います。
```
./IfcConvert input_bim.ifc output_obj.obj
```

### 3.obj から点群生成

生成したobjファイルからメッシュ表面をサンプリングすることで点群を生成します。以下のコマンドで実行します。densityは面積あたりにサンプリングする点群の数の目安です。
```
python create_sampling_point_cloud.py -f $HOME/CG2RM/obj/obj_file.obj --density 30
```

```
usage: create_sampling_point_cloud.py [-h] -f POINT_CLOUD_FILES [POINT_CLOUD_FILES ...] [--save_dir SAVE_DIR] [-d DENSITY]

optional arguments:
  -h, --help            show this help message and exit
  -f POINT_CLOUD_FILES [POINT_CLOUD_FILES ...], --point_cloud_files POINT_CLOUD_FILES [POINT_CLOUD_FILES ...]
                        list of file path
  --save_dir SAVE_DIR
  -d DENSITY, --density DENSITY

```
コマンドを実行すると$HOME/CG2RM/pointcloud の中にply,とpcdファイルが生成されます。

### 4.（BIMを使う場合のみ）obj(CityGMLから)とobj(BIM)の位置合わせを行う

位置合わせを行いたいobj(CityGMLから)とobj(BIM)とそれぞれから生成された点群を指定し
```
python3 align_bim.py
```
コマンドを実行することでCityGMLが持つ座標系に合うようにBIMを位置調整した結果が得られます。

### 5.複数の点群を一つの点群にまとめる

複数の点群ファイルを一つに統一する場合、以下のようにコマンドを実行することで統合することが可能です。
````
python3 create_sampling_point_cloud.py -f file_1.pcd file_2.pcd ...
````

