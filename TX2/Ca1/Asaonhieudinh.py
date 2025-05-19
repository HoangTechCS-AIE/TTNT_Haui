graph = {
    'A': [('B', 4), ('C', 3)],
    'B': [('F', 5), ('E', 12)],
    'C': [('D', 7), ('E', 10)],
    'D': [('E', 2)],
    'E': [('Z', 5)],
    'F': [('Z', 16)],
    'Z': []
}

heuristic = {
    'A': 11,
    'B': 11,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 0,
    'Z': 0
}
def a_star(graph, heuristic, start, goal):
    open_list = [start]
    closed = set()
    g = {start: 0}
    f = {start: heuristic[start]}
    parent = {start: None}
    order = []  # Lưu thứ tự duyệt

    while open_list:
        # Chọn đỉnh có f(n) nhỏ nhất
        current = min(open_list, key=lambda node: f.get(node, float('inf')))
        open_list.remove(current)
        order.append(current)

        if current == goal:
            # Truy vết đường đi
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Thứ tự duyệt:", " → ".join(order))
            print("Đường đi A*:", " → ".join(path))
            print("Chi phí (g):", g[goal])
            return path

        closed.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor in closed:
                continue

            tentative_g = g[current] + cost

            if neighbor not in open_list:
                open_list.append(neighbor)
            elif tentative_g >= g.get(neighbor, float('inf')):
                continue

            parent[neighbor] = current
            g[neighbor] = tentative_g
            f[neighbor] = g[neighbor] + heuristic[neighbor]

    print("Không tìm thấy đường đi.")
    return None
if __name__ == "__main__":
    a_star(graph, heuristic, 'A', 'Z')
