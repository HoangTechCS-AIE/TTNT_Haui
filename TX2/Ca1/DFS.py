def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    parent = {start: None}

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent.get(node)
            return path[::-1]

        for neigh in reversed(graph.get(node, [])):
            if neigh not in visited and neigh not in stack:
                parent[neigh] = node
                stack.append(neigh)

    return None
if __name__ == "__main__":
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
    }

    path = dfs(graph, start="A", goal="R")
    if path:
        print("Đường đi tìm được (DFS):", " → ".join(path))
    else:
        print("Không tìm thấy đường đi tới đích.")
