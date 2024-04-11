def find_value(arr, target):
   
    for i, value in enumerate(arr):
        if value == target:
            return i
    return None

# 示例用法
arr = [1, 2, 3, 4, 5]
target = 3

# 调用函数查找目标值
index = find_value(arr, target)

if index is not None:
    print(f"找到目标值 {target}，位于列表的索引位置 {index}。")
else:
    print(f"未找到目标值 {target}。")
