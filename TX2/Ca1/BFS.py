from collections import deque

def bfs(graph, start, goal):
    dq = deque([start])
    visited = set()
    parent = {start: None}  # Khởi tạo cha của đỉnh đầu tiên

    while dq:
        node = dq.popleft()
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent.get(node)
            return path[::-1]

        for neigh in graph.get(node, []):
            if neigh not in visited and neigh not in dq:
                parent[neigh] = node
                dq.append(neigh)

    return None

if __name__ == "__main__":  # ✅ Sửa lỗi __name__
    # Định nghĩa đồ thị
    graph = {
        "A": ["B", "C", "D"],
        "B": ["M", "N"],
        "M": ["X", "Y"],
        "X": [],
        "Y": ["R", "S"],
        "C": ["N", "L"],
        "N": ["U", "V"],
        "V": ["G", "H"],
        "D": ["O", "P"],
        "O": ["I", "J"],
        # các đỉnh lá còn lại: U, V, G, H, S, R, L, P, I, J...
    }

    path = bfs(graph, start="A", goal="R")
    if path:
        print("Đường đi tìm được:", " → ".join(path))
    else:
        print("Không tìm thấy đường đi tới đích.")
