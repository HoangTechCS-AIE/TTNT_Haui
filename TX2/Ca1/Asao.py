# Định nghĩa graph: mỗi cạnh là (đỉnh kề, chi phí, heuristic)
graph = {
    'A': [('B', 4, 11), ('C', 3, 11)],
    'B': [('F', 5, 11), ('E', 12, 4)],
    'C': [('D', 7, 6), ('E', 10, 4)],
    'D': [('E', 2, 4)],
    'E': [('Z', 5, 0)],
    'F': [('Z', 16, 0)]
}

# Hàm heuristic h(n)
def h(node):
    h = {
        'A': 11,
        'B': 11,
        'C': 11,
        'D': 6,
        'E': 4,
        'F': 0,
        'Z': 0
    }
    return h[node]

# Hàm in đường đi và chi phí
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

# Thuật toán A*
def A_star(graph, start, goals):
    MO = [start]  # Tập đỉnh mở
    DONG = []     # Tập đỉnh đóng
    f = {start: h(start)}  # Chi phí f(n)
    g = {start: 0}         # Chi phí g(n)
    parent = {}            # Cha của mỗi đỉnh

    while MO:
        # Chọn đỉnh có f(n) nhỏ nhất trong MO
        min_f = float('inf')
        min_node = None
        for node in MO:
            if f[node] < min_f:
                min_f = f[node]
                min_node = node
        n = min_node

        if n in goals:
            print_path_and_cost(start, n, parent, g)
            print(parent)
            return True

        MO.remove(n)
        DONG.append(n)

        for m, cost, _ in graph.get(n, []):
            cost_new = g[n] + cost
            if m not in g or cost_new < g[m]:
                g[m] = cost_new
                f[m] = g[m] + h(m)
                parent[m] = n

            if m not in DONG and m not in MO:
                MO.append(m)

    return False

# Chạy thử
print("A*")
A_star(graph, 'A', ['Z', 'F'])
