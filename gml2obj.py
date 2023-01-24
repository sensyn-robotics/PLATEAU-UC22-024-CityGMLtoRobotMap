import argparse
import math
import subprocess
from os.path import exists
from pathlib import Path
from statistics import mean

from cjio import cityjson
from pyproj import Transformer

from mesh_code_util import specify_code


def reproject(CS: cityjson.CityJSON, target_epsg: int):
    imp_digits = math.ceil(abs(math.log(1, 10)))
    CS.decompress()
    # p1 = pyproj.Proj(init='epsg:%d' % (CS.get_epsg()))
    # p2 = pyproj.Proj(init='epsg:%d' % (epsg))
    from_crs = 'epsg:%d' % (CS.get_epsg())
    to_crs = 'epsg:%d' % (target_epsg)
    print("1", CS.j['vertices'][0])
    transformer = Transformer.from_crs(from_crs, to_crs)
    trans_points = list(transformer.itransform(CS.j['vertices']))
    print("2", trans_points[0])
    CS.j['vertices'] = [list(item) for item in trans_points]

    CS.set_epsg(target_epsg)
    CS.update_bbox()
    CS.update_bbox_each_cityobjects(True)
    # -- recompress by using the number of digits we had in original file
    # CS.compress(1)
    return CS


def reproject_custom(CS: cityjson.CityJSON, lat: float, lon: float, altitude):
    """'
      https://gis.stackexchange.com/questions/299426/transform-coordinates-from-custom-projection-to-lat-long-pyproj

            std::sprintf(
            proj_enu_crs,"+proj=etmerc +ellps=GRS80 +lon_0=%.10f +lat_0=%.10f +x_0=0 +y_0=0 "
            "+z_0=-%.10f +k_0=1",base_point_longitude_, base_point_latitude_, base_point_altitude_);
    """

    imp_digits = math.ceil(abs(math.log(1, 10)))
    CS.decompress()
    from_crs = 'epsg:%d' % (CS.get_epsg())
    to_crs = "+proj=etmerc +ellps=GRS80 +lon_0={} +lat_0={} +x_0=0 +y_0=0 +z_0={} +k_0=1".format(lon, lat, altitude)

    transformer = Transformer.from_crs(from_crs, to_crs)
    CS.j['vertices'] = [list(item) for item in transformer.itransform(CS.j['vertices'])]
    CS.set_epsg(None)

    CS.update_bbox()
    CS.update_bbox_each_cityobjects(True)
    # -- recompress by using the number of digits we had in original file
    # CS.compress(imp_digits)


def print_vertex_centroid(CJ: cityjson.CityJSON):
    points = CJ.j['vertices']
    ct = [0, 0, 0]
    ct[0] = mean(list(item[0] for item in points))
    ct[1] = mean(list(item[1] for item in points))
    ct[2] = mean(list(item[2] for item in points))

    print('centroid calc', ct)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('city_json_file', type=str)
    parser.add_argument('-s', '--source_dir', type=str, required=True)
    parser.add_argument('--number', type=str, default='53392575')
    parser.add_argument('--lat', type=float, default=35.6809591)
    parser.add_argument('--lon', type=float, default=139.7673068)
    parser.add_argument('--alt', type=float, default=17.0)
    parser.add_argument('--mapcode_level')
    parser.add_argument('--save_dir', type=str, default=str(Path.home().joinpath('CG2RM', 'obj')))
    parser.add_argument('-u', '--update', action='store_true')

    args = parser.parse_args()

    first, second, third = specify_code(args.lat, args.lon)
    print('first', first, 'second', second, 'third', third)

    map_number = third  # args.number  # 53392575
    source_dir = args.source_dir
    extension = "*.gml"
    glob_gml_files = Path(source_dir).rglob(str(map_number) + extension)
    target_part_list = ['bldg', 'brid', 'dem', 'tran']
    numbers_gml_file = []

    # search target gml files
    for path in glob_gml_files:
        for item in target_part_list:
            if str(item) in str(path):
                numbers_gml_file.append(path)

    for item in numbers_gml_file:
        print(item)

    # city gml to city json:  no coordinate trans
    for gml_file in numbers_gml_file:
        json_path = str(gml_file).replace('.gml', '.json')
        if not exists(json_path) or args.update:
            subprocess.run(
                ["citygml-tools-2.0.0/citygml-tools",
                 "to-cityjson", "--vertex-precision=15", "--template-precision=15",
                 "--cityjson-version=1.0", str(gml_file)])
        else:
            print(json_path, 'is already exist')

    # transform and generate obj
    obj_save_directory = Path(args.save_dir)
    obj_save_directory.mkdir(exist_ok=True, parents=True)

    for gml_path in numbers_gml_file:

        # print(args.city_json_file)
        input_gml_file = str(gml_path).replace('.gml', '.json')  # args.city_json_file
        obj_file = obj_save_directory.joinpath(gml_path.name.replace(".gml", ".obj"))

        if exists(obj_file) and (not args.update):
            print(obj_file, 'is already exist')
        else:
            print('converting ', obj_file)
            with open(input_gml_file, mode='r', encoding='utf-8-sig') as f:
                CJ = cityjson.reader(file=f, ignore_duplicate_keys=True)
                print(CJ.get_info())
            # CJ.filter_lod()
            # with Timer() as t1:
            print("Before point 1", CJ.j['vertices'][0])

            # transform points from EPSG:6697 to base points
            CJ = reproject(CJ, 4326)  # 4326 = wgs84

            reproject_custom(CJ, args.lat, args.lon, args.alt)
            # invert(CJ, 35.6457381, 139.7218593)
            print("After point 1", CJ.j['vertices'][0])
            print("bbox", CJ.get_bbox())

            print_vertex_centroid(CJ)
            # CJ.get_info()
            result_obj = CJ.export2obj().getvalue()
            # print(result_obj)
            # print("Elapsed_time for export obj:{0}".format(t1.elapsed) + "[sec]")

            with open(obj_file, mode='w') as out_file:
                out_file.write(result_obj)

        # # convert to obj
