import math

EPS = 1e-8
MAXV = 10000

class Point:
    def __init__(self, a=0, b=0, c=-1):
        self.x = a
        self.y = b
        self.id = c

    def __lt__(self, a):
        return self.x < a.x or (math.isclose(self.x, a.x, abs_tol=EPS) and self.y < a.y)

    def __eq__(self, a):
        return math.isclose(self.x, a.x, abs_tol=EPS) and math.isclose(self.y, a.y, abs_tol=EPS)

    def dist2(self, b):
        return (self.x - b.x) ** 2 + (self.y - b.y) ** 2

class Point3D:
    def __init__(self, a=0, b=0, c=0):
        self.x = a
        self.y = b
        self.z = c

    def __sub__(self, a):
        return Point3D(self.x - a.x, self.y - a.y, self.z - a.z)

    def dot(self, a):
        return self.x * a.x + self.y * a.y + self.z * a.z

class Edge:
    def __init__(self, id=0):
        self.id = id
        self.c = None

def cmp(v):
    return 1 if abs(v) > EPS else (0 if abs(v) < EPS else -1)

def cross(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)

def cross_3d(a, b):
    return Point3D(a.y * b.z - a.z * b.y, -a.x * b.z + a.z * b.x, a.x * b.y - a.y * b.x)

def inCircle(a, b, c, p):
    if cross(a, b, c) < 0:
        b, c = c, b
    a3, b3, c3, p3 = Point3D(a), Point3D(b), Point3D(c), Point3D(p)
    b3, c3, p3 = b3 - a3, c3 - a3, p3 - a3
    f = cross_3d(b3, c3)
    return cmp(p3.dot(f))

def intersection(a, b, c, d):
    return cmp(cross(a, c, b)) * cmp(cross(a, b, d)) > 0 and cmp(cross(c, a, d)) * cmp(cross(c, d, b)) > 0

class Delaunay:
    def __init__(self):
        self.head = [[] for _ in range(MAXV)]
        self.p = [None] * MAXV
        self.rename = [0] * MAXV
        self.n = 0

    def init(self, n, points):
        self.p = sorted(points)
        for i in range(n):
            self.rename[self.p[i].id] = i
        self.n = n
        self.divide(0, n - 1)

    def addEdge(self, u, v):
        edge_uv = Edge(v)
        edge_vu = Edge(u)
        self.head[u].append(edge_uv)
        self.head[v].append(edge_vu)
        edge_uv.c = edge_vu
        edge_vu.c = edge_uv

    def divide(self, l, r):
        if r - l <= 2:
            for i in range(l, r + 1):
                for j in range(i + 1, r + 1):
                    self.addEdge(i, j)
            return
        mid = (l + r) // 2
        self.divide(l, mid)
        self.divide(mid + 1, r)

        nowl, nowr = l, r
        update = 1
        while update:
            update = 0
            ptL, ptR = self.p[nowl], self.p[nowr]
            for edge in self.head[nowl]:
                t = self.p[edge.id]
                v = cross(ptR, ptL, t)
                if cmp(v) > 0 or (cmp(v) == 0 and ptR.dist2(t) < ptR.dist2(ptL)):
                    nowl, update = edge.id, 1
                    break
            if update:
                continue
            for edge in self.head[nowr]:
                t = self.p[edge.id]
                v = cross(ptL, ptR, t)
                if cmp(v) < 0 or (cmp(v) == 0 and ptL.dist2(t) < ptL.dist2(ptR)):
                    nowr, update = edge.id, 1
                    break

        self.addEdge(nowl, nowr)

        while True:
            update = 0
            ptL, ptR = self.p[nowl], self.p[nowr]
            ch, side = -1, 0
            for edge in self.head[nowl]:
                if cmp(cross(ptL, ptR, self.p[edge.id])) > 0 and (ch == -1 or inCircle(ptL, ptR, self.p[ch], self.p[edge.id]) < 0):
                    ch, side = edge.id, -1
            for edge in self.head[nowr]:
                if cmp(cross(ptR, self.p[edge.id], ptL)) > 0 and (ch == -1 or inCircle(ptL, ptR, self.p[ch], self.p[edge.id]) < 0):
                    ch, side = edge.id, 1
            if ch == -1:
                break
            if side == -1:
                for edge in self.head[nowl][:]:
                    if intersection(ptL, self.p[edge.id], ptR, self.p[ch]):
                        self.head[edge.id].remove(edge.c)
                        self.head[nowl].remove(edge)
                    else:
                        continue
                nowl = ch
                self.addEdge(nowl, nowr)
            else:
                for edge in self.head[nowr][:]:
                    if intersection(ptR, self.p[edge.id], ptL, self.p[ch]):
                        self.head[edge.id].remove(edge.c)
                        self.head[nowr].remove(edge)
                    else:
                        continue
                nowr = ch
                self.addEdge(nowl, nowr)

    def getEdge(self):
        ret = []
        for i in range(self.n):
            for edge in self.head[i]:
                if edge.id < i:
                    continue
                ret.append((self.p[i].id, self.p[edge.id].id))
        return ret

# Example usage:
points = [Point(0, 0, 0), Point(1, 0, 1), Point(0, 1, 2), Point(1, 1, 3)]
delaunay = Delaunay()
delaunay.init(len(points), points)
edges = delaunay.getEdge()
print(edges)
