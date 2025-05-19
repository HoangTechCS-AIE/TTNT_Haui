def dfs(graph, start, goals):
    stack = [start]
    visited = set()
    parent = {start: None}
    order = []  # Danh sách bước duyệt

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)  # Lưu bước duyệt

        if node in goals:
            # Truy vết đường đi
            path = []
            while node is not None:
                path.append(node)
                node = parent.get(node)
            print("Thứ tự duyệt:", " → ".join(order))
            print("Đường đi tìm được (DFS):", " → ".join(path[::-1]))
            return path[::-1]

        # Đảo ngược danh sách con để duyệt theo thứ tự từ trái sang phải
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                parent[neighbor] = node
                stack.append(neighbor)

    print("Thứ tự duyệt:", " → ".join(order))
    print("Không tìm thấy đường đi đến goal.")
    return None
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['H', 'I'],
        'C': ['E', 'F'],
        'D': ['G'],
        'E': [],
        'F': ['J', 'K'],
        'G': [],
        'H': [],
        'I': [],
        'J': [],
        'K': []
    }

    start = 'A'
    goals = {'I', 'G', 'K'}
    dfs(graph, start, goals)
