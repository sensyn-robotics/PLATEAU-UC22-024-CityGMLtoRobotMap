サンプルデータを使ったGityGMltoRobotoMapの使用方法を解説します。

python gml2obj.py -s ./sample_resource/city_gml/udx/ --lat 35.4987030455 --lon 139.72337047 --alt 38.5293235779 --mapcode_level third

python gml2obj.py -s ./sample_resource/city_gml/udx/dem/533915_dem_6697.gml --lat 35.4987030455 --lon 139.72337047 --alt 38.5293235779

./IfcConvert sample_resource/bim/warehouse.ifc sample_resource/bim/warehouse.obj

mv warehouse.obj ~/CG2RM/obj/

use blender

import obj into blender
<img src="images/import_columun.jpg" width="80%">
<img src="images/import_axis.jpg" width="30%">
<img src="images/view_import_warehouse_nad_map.jpg" width="80%">
<img src="images/view_trans_warehouse_by_hand.jpg" width="80%">

python create_sampling_point_cloud.py -f $HOME/CG2RM/obj/53391597_bldg_6697.obj ./sample_resource/bim/warehouse_trans.obj --density 10  

python align_bim.py --source ~/CG2RM/pointcloud/warehouse_trans_sample.ply --target ~/CG2RM/pointcloud/53391597_bldg_6697_sample.ply  

<img src="images/align_result.jpg" width="80%">

use blender remove overwraped building

<img src="images/chice_for_remove.jpg" width="80%">
<img src="images/remove_result.jpg" width="80%">

<img src="images/output_select.jpg" width="80%">


python create_sampling_point_cloud.py -f $HOME/CG2RM/obj/53391597_bldg_6697_removed.obj  --density 10
python create_sampling_point_cloud.py -f ~/53391597_bldg_6697_removed.obj -d 10

python merge_multi_point_cloud.py -f ~/CG2RM/pointcloud/warehouse_trans_sample.pcd ~/CG2RM/pointcloud/53391597_bldg_6697_removed_sample.pcd