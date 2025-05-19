graph = {
    "A": {"B": 2, "C": 4, "F": 6},
    "B": {},
    "C": {"D": 8, "E": 2},
    "D": {},
    "E": {},
    "F": {"G": 5, "H": 1},
    "G": {},
    "H": {}
}

def print_path_and_cost(start, goal, parent, g):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    print("Đường đi:", ' -> '.join(path))
    print("C(p) = ", g[goal])

def AT(graph, start, goals):
    MO = [start]  # Danh sách các đỉnh đã được duyệt
    g = {start: 0}  # Chi phí tới từng đỉnh
    DONG = []  # Danh sách các đỉnh đã xét xong
    parent = {}  # Lưu trữ cha của mỗi đỉnh

    while MO:
        # Lấy đỉnh n có chi phí g(n) nhỏ nhất từ tập MO
        min_cost = float('inf')
        n = None
        for vertex in MO:
            cost = g[vertex] if vertex in g else float('inf')
            if cost < min_cost:
                min_cost = cost
                n = vertex

        if n in goals:
            print_path_and_cost(start, n, parent, g)
            return True

        MO.remove(n)  # Xóa đỉnh n khỏi tập MO
        DONG.append(n)  # Thêm đỉnh n vào tập đỉnh đã xét

        for m in graph.get(n, {}):  # Duyệt qua các đỉnh kề của n
            cost = graph[n][m]
            new_cost = g[n] + cost
            if m not in g or new_cost < g[m]:  # Nếu là đỉnh mới hoặc đường đi tốt hơn
                g[m] = new_cost
                parent[m] = n

            if m not in DONG and m not in MO:
                MO.append(m)

    return False  # Không tìm thấy đường đi đến đỉnh đích

# Chạy ví dụ
start = "A"
goals = ["D", "H"]
AT(graph, start, goals)