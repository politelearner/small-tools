import numpy as np

def convert_to_2d_coordinates(coords):
    # 确定共面平面的法向量
    length = len(coords)
    v1 = coords[np.random.randint(1, length)] - coords[0]
    v2 = coords[np.random.randint(1, length)] - coords[0]
    normal_vector = np.cross(v1, v2)
    
    # 检查法向量是否为零向量，如果是则选择不同的向量
    # 由于一定共面，特定修改
    while np.all(normal_vector == 0):
        v1 = coords[np.random.randint(1, length)] - coords[0]
        v2 = coords[np.random.randint(1, length)] - coords[0]
        normal_vector = np.cross(v1, v2)
        # raise ValueError("输入的三维坐标不共面。")

    # 选择共面上的两个基向量
    basis_vector1 = v1.astype(np.float64)  # 将数据类型转换为float64
    basis_vector2 = np.cross(normal_vector, basis_vector1).astype(np.float64)  # 将数据类型转换为float64
    
    # 正交化基向量
    basis_vector2 -= np.dot(basis_vector1, basis_vector2) / np.dot(basis_vector1, basis_vector1) * basis_vector1
    
    # 归一化基向量
    basis_vector1 = basis_vector1 / np.linalg.norm(basis_vector1)
    basis_vector2 = basis_vector2 / np.linalg.norm(basis_vector2)
    
    # 将三维坐标投影到基向量上，得到二维坐标
    coords_2d = []
    for coord in coords:
        x = np.dot(coord, basis_vector1)
        y = np.dot(coord, basis_vector2)
        coords_2d.append([x, y])
    
    return coords_2d

# 示例输入（共面坐标）
coordinates_3d = np.array([[-9.6250  ,  0.0000   , 5.7750],
                           [-3.8500  ,  1.9250   , 9.6250],  # 修改了第二个坐标点
                           [-9.6250  ,  3.8500   , 1.9250]]) # 修改了第三个坐标点

try:
    # 转换为二维坐标
    coordinates_2d = convert_to_2d_coordinates(coordinates_3d)
    print("二维坐标：", coordinates_2d)
except ValueError as e:
    print("错误：", e)
