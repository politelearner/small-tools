import numpy as np

# 读取numpy文件
coordinates_array = np.load('final_surfaces_location.npy', allow_pickle=True)

# 打印输出
for group in coordinates_array:
    for coords in group:
        print(coords)
    print()
  