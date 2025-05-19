from collections import deque

def bfs(graph, start, goals):
    queue = deque([start])
    visited = set()
    parent = {start: None}
    order = []  # Danh sách các bước duyệt

    while queue:
        node = queue.popleft()
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
            print("Đường đi tìm được (BFS):", " → ".join(path[::-1]))
            return path[::-1]

        for neighbor in graph.get(node, []):
            if neighbor not in visited and neighbor not in queue:
                parent[neighbor] = node
                queue.append(neighbor)

    print("Thứ tự duyệt:", " → ".join(order))
    print("Không tìm thấy đường đi đến goal.")
    return None

# Chạy thử
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
    bfs(graph, start, goals)
