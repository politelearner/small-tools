def are_lines_intersecting(line1, line2):
    # 解析直线的端点
    x1, y1 = line1.coords[0][0], line1.coords[0][1]
    x2, y2 = line1.coords[1][0], line1.coords[1][1]

    x3, y3 = line2.coords[0][0], line2.coords[0][1]
    x4, y4 = line2.coords[1][0], line2.coords[1][1]

    # 计算斜率，注意处理斜率为无穷大的情况
    if x2 - x1 != 0:
        m1 = (y2 - y1) / (x2 - x1)
    else:
        m1 = float('inf')

    if x4 - x3 != 0:
        m2 = (y4 - y3) / (x4 - x3)
    else:
        m2 = float('inf')

    # 如果斜率相同，则直线平行，不会相交
    if m1 == m2:
        return False

    # 计算交点的 x 坐标
    if m1 == float('inf'):
        x_intersect = x1
    elif m2 == float('inf'):
        x_intersect = x3
    else:
        x_intersect = (m1 * x1 - m2 * x3 + y3 - y1) / (m1 - m2)
    
    # 如果交点的 x 坐标在两条直线的端点之间，则相交
    if min(x1, x2) <= x_intersect <= max(x1, x2) and \
       min(x3, x4) <= x_intersect <= max(x3, x4):
        return True
    else:
        return False

# 示例直线
from shapely.geometry import LineString

line1 = LineString([(0, 0), (1, 1)])
line2 = LineString([(1, 0), (0, 1)])

if are_lines_intersecting(line1, line2):
    print("Lines are intersecting")
else:
    print("Lines are not intersecting")
