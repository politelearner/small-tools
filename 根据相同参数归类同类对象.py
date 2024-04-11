import numpy as np
def classify_objects(objects, param_name):
    # 获取所有可能的参数值
    param_values = set(tuple(tuple(x) if isinstance(x, np.ndarray) else x for x in getattr(obj, param_name)) for obj in objects)

    # 初始化分类结果为一个空列表
    classified_objects = []

    # 遍历对象列表，根据参数值将对象放入对应的类别列表中
    for obj in objects:
        param_value = tuple(tuple(x) if isinstance(x, np.ndarray) else x for x in getattr(obj, param_name))
        classified_objects.append((param_value, obj))

    return classified_objects

# 示例调用
class Object:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

objects = [Object(np.array([1, 2]), 'A'), Object(np.array([4, 5]), 'B'), Object(np.array([5, 6]), 'C'),
           Object(np.array([3, 4]), 'A'), Object(np.array([2, 3]), 'B'), Object(np.array([1, 2]), 'C'),
           Object(np.array([2, 3]), 'A'), Object(np.array([3, 4]), 'B'), Object(np.array([4, 5]), 'C'),
           Object(np.array([4, 5]), 'A'), Object(np.array([5, 6]), 'B'), Object(np.array([5, 6]), 'C')]

classified_objects = classify_objects(objects, 'param1')

# 输出分类结果
for param_value, obj in classified_objects:
    print("参数值为 {} 的对象有: {}".format(param_value, obj.param2))
