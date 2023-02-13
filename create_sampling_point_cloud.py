import argparse
from pathlib import Path

import open3d
import pymeshlab
import trimesh

ms = pymeshlab.MeshSet()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--point_cloud_files', nargs='+', help='list of file path ', required=True)
    parser.add_argument('--save_dir', type=str, default=str(Path.home().joinpath('CG2RM', 'pointcloud')))
    parser.add_argument('-d','--density', type=float, default=30)

    args = parser.parse_args()

    input_files = [Path(file_str) for file_str in args.point_cloud_files]
    save_directory = Path(args.save_dir)

    save_directory.mkdir(exist_ok=True, parents=True)

    for input_obj_file in input_files:
        obj_data = trimesh.load_mesh(str(input_obj_file), file_type='obj')  # type:trimesh.base.Trimesh
        print('load', str(input_obj_file))

        area_size = int(obj_data.area)
        density = args.density
        print('area size: {}, density: {} '.format(area_size, density))

        # generate point cloud
        ms.load_new_mesh(str(input_obj_file))
        sample_number = int(area_size * density)
        print('sampling {} points ....'.format(sample_number))
        ms.generate_sampling_poisson_disk(samplenum=sample_number)

        ply_file = str(save_directory.joinpath(input_obj_file.name.replace('.obj', '_sample.ply')))
        pcd_file = str(save_directory.joinpath(input_obj_file.name.replace('.obj', '_sample.pcd')))

        ms.save_current_mesh(ply_file, save_face_color=False)
        open3d.io.write_point_cloud(pcd_file, open3d.io.read_point_cloud(ply_file))
        print('save files')
