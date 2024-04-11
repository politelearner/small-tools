import numpy as np

def view_npz_contents(file_path):
    # 加载 .npz 文件
    npz_file = np.load(file_path,allow_pickle=True)
    
    # 打印 .npz 文件中的所有数组名
    print("Arrays in {}:".format(file_path))
    for array_name in npz_file.files:
        print("  -", array_name)
    
    # 打印每个数组的形状和内容
    for array_name in npz_file.files:
        print("\nContents of {}:".format(array_name))
        array_data = npz_file[array_name]
        print("Shape:", array_data.shape)
        print(array_data)

# 示例调用
view_npz_contents('example.npz')
