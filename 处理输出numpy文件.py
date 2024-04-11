import numpy as np

# 读取txt文件
with open('surfaces location.txt', 'r', encoding="UTF-8") as file:
    lines = file.readlines()

# 解析坐标数据
coordinates_list = []
current_coords = []
for line in lines:
    if line.startswith('#'):  # 如果行以#开头，则将之前的坐标数据作为一组
        if current_coords:
            coordinates_list.append(np.array(current_coords))
            current_coords = []  # 重置当前坐标列表
        continue
    parts = line.strip().split()
    if len(parts) >= 4:  # 至少包含四个数值，包括标识符
        current_coords.append([float(parts[0]), float(parts[2]), float(parts[1])])

# 最后一组坐标数据
if current_coords:
    coordinates_list.append(np.array(current_coords))

# 将列表中的每组坐标数据转换为numpy数组
final_coordinates_array = np.array(coordinates_list, dtype=object)

# 保存为numpy文件
np.save('final_surfaces_location.npy', final_coordinates_array)
