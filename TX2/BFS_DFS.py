graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'F': ['K', 'L', 'M'],
    'H': ['N', 'O'],
    'E': [], 'G': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}


# Chiều rộng

def print_path(start, goal, parent):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()

    print('Đường đi: ', '->'.join(path))


def Bfs(start, goal, graph):
    Open = [start]
    Closed = []
    parent = {}

    while Open:
        current = Open.pop(0)
        print('Đang duyệt: ', current)

        if current == goal:
            print('Đã tìm thấy đích: ', current)
            print_path(start, current, parent)
            return

        Closed.append(current)
        # Duyệt các nút kề
        for neighbor in graph.get(current, []):
            if neighbor not in Open and neighbor not in Closed:
                parent[neighbor] = current
                Open.append(neighbor)  # Thêm vào cuối danh sách

    print('Không tìm thấy!')


start = 'A'
goal = 'N'
Bfs(start, goal, graph)

# Chiều sâu

# def print_path(start, goal, parent):
#     path = []
#     current = goal
#     while current != start:
#         path.append(current)
#         current = parent[current]

#     path.append(start)
#     path.reverse()

#     print('Đường đi: ', '->'.join(path))

# def Dfs(start, goal, graph):
#     Open = [start]
#     Closed = []
#     parent = {}

#     while Open:
#         current = Open.pop(0)
#         print ('Đang duyệt: ', current)
#         if current == goal:
#             print ('Đã tìm thấy đích: ', current)
#             print_path(start, current, parent)
#             return

#         Closed.append(current)

#         for neighbor in graph.get(current, []):
#             if neighbor not in Open and neighbor not in Closed:
#                 parent[neighbor] = current
#                 Open.insert(0, neighbor)

#     print ('Không tìm thấy đường đi!')

# start = 'A'
# goal = 'N'
# Dfs(start, goal, graph)



