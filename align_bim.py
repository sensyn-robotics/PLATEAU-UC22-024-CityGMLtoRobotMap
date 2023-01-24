import trimesh
from pathlib import Path
from trimesh import registration, convex, visual
from trimesh.exchange import ply
from trimesh.transformations import identity_matrix, rotation_matrix, concatenate_matrices, euler_from_matrix, translation_matrix
import copy
import numpy as np
import math


def get_homogeneous_matrix(x, y, z, roll, pitch, yaw):
    alpha, beta, gamma = 0.123, -1.234, 2.345
    origin, xaxis, yaxis, zaxis = [0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]
    I = identity_matrix()
    Rx = rotation_matrix(math.radians(roll), xaxis)
    Ry = rotation_matrix(math.radians(pitch), yaxis)
    Rz = rotation_matrix(math.radians(yaw), zaxis)
    R = concatenate_matrices(Rx, Ry, Rz)
    T = translation_matrix([x, y, z])

    M = concatenate_matrices(T, R)

    return M


def points_matching(map_mesh: trimesh.points.PointCloud, building_mesh):
    mesh_to_other, _, _ = registration.icp(building_mesh.vertices, map_mesh.vertices, max_iterations=150, threshold=1e-7,scale=False,reflection=False)

    return mesh_to_other


def mesh_matching(map_mesh, building_mesh, with_convex=False):
    sample = 500
    icp_first = 1
    icp_final = 200

    if with_convex:
        mesh_to_other, _ = registration.mesh_other(convex.convex_hull(building_mesh), map_mesh, samples=sample, icp_first=icp_first, icp_final=icp_final)
    else:
        mesh_to_other, _ = registration.mesh_other(building_mesh, map_mesh, samples=sample, icp_first=icp_first, icp_final=icp_final)

    return mesh_to_other


def transform_obj(trans, building_mesh):
    pass


def get_point_in_base_coordinate(base_point_lat, base_point_lon, target_lat, target_lon):
    x, y = 0, 0

    return x, y


if __name__ == '__main__':
    root_dir = ''
    source_mesh = trimesh.load_mesh(str(root_dir + 'obj/53391597_bldg_6697.obj'), file_type='obj')  # type:trimesh.base.Trimesh
    target_mesh = trimesh.load_mesh(str(root_dir + 'bim/untitled.obj'), file_type='obj')  # type:trimesh.base.Trimesh

    dem_mesh = trimesh.load_mesh(str(root_dir + 'cut_dem.obj'), file_type='obj')  # type:trimesh.base.Trimesh

    source_points = trimesh.load_mesh(str(root_dir + 'ply/base_merge.ply'), file_type='ply')  # type:trimesh.base.Trimesh
    # dem_points = trimesh.load_mesh(str(root_dir + 'ply/cut_dem_sample.ply'), file_type='ply')  # type:trimesh.base.Trimesh
    target_points = trimesh.load_mesh(str(root_dir + 'ply/untitled_trans_sample.ply'), file_type='ply')  # type:trimesh.base.Trimesh

    if isinstance(target_mesh, trimesh.scene.scene.Scene):
        mesh_list = []
        for mesh in target_mesh.geometry.values():
            if isinstance(mesh, trimesh.Trimesh):
                mesh_list.append(mesh)

        target_mesh = trimesh.util.concatenate(mesh_list)

    # offset = get_homogeneous_matrix(-10,-30,3,0,0,120)
    offset = get_homogeneous_matrix(0,0,0,0,0,5)


    target_mesh.apply_transform(offset)
    target_points.apply_transform(offset)
    original_input_mesh = copy.deepcopy(target_mesh)

    # input ifc/obj, target lat lon
    # 35.6682252,139.8189464
    target_lat = 35.6682252
    target_lon = 139.8189464

    base_point_lat = 1
    base_point_lon = 1
    x, y = get_point_in_base_coordinate(base_point_lat, base_point_lon, target_lat, target_lon)
    # hogenoou max from x,y
    # bias rotation
    # id_t = trimesh.transformations

    # add initial trans
    # merged_source_mesh = trimesh.util.concatenate([copy.deepcopy(dem_mesh), copy.deepcopy(source_mesh)])

    print('start align')

    # trans = mesh_matching(source_mesh, target_mesh, with_convex=False)

    trans = points_matching(source_points, target_points)
    # trans = mesh_matching(source_mesh, target_mesh, with_convex=True)

    print(trans)

    # trans[2][3] += 0.7
    # print(trans[2][3])
    target_mesh.apply_transform(trans)
    target_points.apply_transform(trans)

    # target_mesh.show()
    print('source centroid', source_mesh.centroid, 'target centroid', target_mesh.centroid)
    target_mesh.visual.face_colors = [200, 200, 100, 100]
    source_mesh.visual.face_colors = [200, 200, 200, 100]
    original_input_mesh.visual.face_colors = [200, 100, 100, 100]

    # target_mesh = visual.ColorVisuals(target_mesh,face_colors=(100,100,100,200))
    # source_mesh = visual.ColorVisuals(source_mesh,face_colors=(100,100,100,100))

    # mesh = trimesh.util.concatenate([target_mesh, source_mesh])
    scene = trimesh.Scene([target_mesh, original_input_mesh, source_mesh, dem_mesh])
    scene.show()
    # mesh.show(smooth=False)

    # target_points.export(str('/Users/akifumi/citygml_test/bim/untitled_trans_2.ply'))
    # target_mesh.export(str('/Users/akifumi/citygml_test/bim/untitled_trans_2.obj'))
