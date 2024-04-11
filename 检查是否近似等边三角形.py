import matplotlib.pyplot as plt

def is_equilateral_triangle(points,error = 0.05):
    # 计算三边的长度
    side_lengths = [
        ((points[0][0] - points[1][0])**2 + (points[0][1] - points[1][1])**2)**0.5,
        ((points[1][0] - points[2][0])**2 + (points[1][1] - points[2][1])**2)**0.5,
        ((points[2][0] - points[0][0])**2 + (points[2][1] - points[0][1])**2)**0.5
    ]
    
    # 计算误差范围
    error_margin = max(side_lengths) * error
    
    # 检查三边的长度是否在误差范围内相等
    if abs(side_lengths[0] - side_lengths[1]) <= error_margin and \
       abs(side_lengths[1] - side_lengths[2]) <= error_margin and \
       abs(side_lengths[2] - side_lengths[0]) <= error_margin:
        return True
    else:
        return False

def plot_triangle(points):
    # 绘制三角形
    plt.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], 'b-')
    plt.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]], 'b-')
    plt.plot([points[2][0], points[0][0]], [points[2][1], points[0][1]], 'b-')
    
    # 标记顶点
    plt.plot(points[0][0], points[0][1], 'ro')
    plt.plot(points[1][0], points[1][1], 'ro')
    plt.plot(points[2][0], points[2][1], 'ro')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Triangle')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# 示例用法
triangle_points = [[0, 0], [1, 0], [0.5, 0.8]]
print("是否为等边三角形：", is_equilateral_triangle(triangle_points))
plot_triangle(triangle_points)
