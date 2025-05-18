from collections import deque

# Dung tích tối đa của các bình
MAX_4 = 4
MAX_3 = 3

# Kiểm tra trạng thái đích
def is_goal(state):
    x, y = state
    return x == 2  # Chỉ cần 2 lít trong bình 4 lít

# Sinh các trạng thái tiếp theo từ một trạng thái hiện tại
def get_next_states(state):
    x, y = state
    states = []

    # Luật 1: Đổ đầy bình 4
    if x < MAX_4:
        states.append((MAX_4, y))
    # Luật 2: Đổ đầy bình 3
    if y < MAX_3:
        states.append((x, MAX_3))
    # Luật 3: Đổ hết bình 4
    if x > 0:
        states.append((0, y))
    # Luật 4: Đổ hết bình 3
    if y > 0:
        states.append((x, 0))
    # Luật 5: Rót từ 3 → 4 (cho đến khi đầy 4 hoặc hết 3)
    if x + y >= MAX_4 and y > 0:
        states.append((MAX_4, y - (MAX_4 - x)))
    # Luật 6: Rót từ 4 → 3 (cho đến khi đầy 3 hoặc hết 4)
    if x + y >= MAX_3 and x > 0:
        states.append((x - (MAX_3 - y), MAX_3))
    # Luật 7: Rót từ 3 → 4 (bình 4 chưa đầy và còn nước trong bình 3)
    if x + y < MAX_4 and y > 0:
        states.append((x + y, 0))
    # Luật 8: Rót từ 4 → 3 (bình 3 chưa đầy và còn nước trong bình 4)
    if x + y < MAX_3 and x > 0:
        states.append((0, x + y))

    return states

# BFS để tìm lời giải
def bfs(start):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()
        if is_goal(current):
            return path
        for next_state in get_next_states(current):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    return None

# Chạy thử
start_state = (0, 0)
solution = bfs(start_state)

# In kết quả
if solution:
    for i, state in enumerate(solution):
        print(f"Bước {i}: {state}")
else:
    print("Không tìm được lời giải.")
