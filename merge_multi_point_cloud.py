import argparse
import random
import sys
from pathlib import Path

import numpy as np
import open3d as o3d

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--point_cloud_files', nargs='+', help='list of file path ', required=True)
    parser.add_argument('-t', '--type', type=str, default='pcd', choices=['ply', 'pcd'])
    parser.add_argument('--save_dir', type=str, default=str(Path.home().joinpath('CG2RM', 'pointcloud')))
    args = parser.parse_args()
    input_files = [Path(file_str) for file_str in args.point_cloud_files]

    if len(input_files) < 2:

        sys.exit()

    pc_list = [o3d.io.read_point_cloud(str(file_path)) for file_path in input_files]
    point_cloud_base = None

    for pc in pc_list:
        pc.paint_uniform_color([random.random(), random.random(), random.random()])

        pc_load = np.asarray(pc.points)
        pc_color = np.asarray(pc.colors)

        if point_cloud_base is not None:
            p_load = np.concatenate((np.asarray(point_cloud_base.points), pc_load), axis=0)
            p_color = np.concatenate((np.asarray(point_cloud_base.colors), pc_color), axis=0)
        else:
            point_cloud_base = pc

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(p_load)
    pcd.colors = o3d.utility.Vector3dVector(p_color)

    save_directory = Path(args.save_dir)
    save_directory.mkdir(exist_ok=True, parents=True)
    f_name = 'marge_points'
    o3d.io.write_point_cloud(str(save_directory.joinpath(f_name + '.' + args.type)), pcd)
