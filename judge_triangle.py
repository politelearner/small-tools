def distance(point1, point2):
    # 计算两点之间的距离
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

def is_triangle(line1, line2, line3):
    # 检查是否可以形成一个三角形
    # 如果任意两条线段之间的长度之和大于第三条线段的长度，则可以形成一个三角形
    lengths = [line1, line2, line3]
    lengths.sort()  # 将长度按升序排列
    return lengths[0] + lengths[1] > lengths[2]

def count_triangles(lines):
    count = 0
    n = len(lines)
    # 遍历所有可能的三条线段组合
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # 检查这三条线段是否首尾相连，并且可以形成一个三角形
                if (lines[i][0] == lines[k][1] and lines[i][1] == lines[j][0] and
                    lines[j][1] == lines[k][0] and is_triangle(distance(lines[i][0], lines[i][1]), distance(lines[j][0], lines[j][1]), distance(lines[k][0], lines[k][1]))):
                    count += 1
    return count
