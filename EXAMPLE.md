python gml2obj.py -s ./sample_resource/city_gml/udx/ --lat 35.4987030455 --lon 139.72337047 --alt 38.5293235779 --mapcode_level third

python gml2obj.py -s ./sample_resource/city_gml/udx/dem/533915_dem_6697.gml --lat 35.4987030455 --lon 139.72337047 --alt 38.5293235779

./IfcConvert sample_resource/bim/warehouse.ifc sample_resource/bim/warehouse.obj

mv warehouse.obj ~/CG2RM/obj/

use blender

python create_sampling_point_cloud.py -f $HOME/CG2RM/obj/53391597_bldg_6697.obj ./sample_resource/bim/warehouse_trans.obj --density 10

python align_bim.py --source ~/CG2RM/pointcloud/warehouse_trans_sample.ply --target ~/CG2RM/pointcloud/53391597_bldg_6697_sample.ply 


