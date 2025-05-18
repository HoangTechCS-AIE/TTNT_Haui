from collections import deque

# Kiểm tra trạng thái có hợp lệ không
def is_valid(state):
    soi, de, cai, nguoi = state
    # Kiểm tra nếu sói và dê ở cùng mà không có người
    if soi == de != nguoi:
        return False
    # Kiểm tra nếu dê và cải ở cùng mà không có người
    if de == cai != nguoi:
        return False
    return True

# Sinh các trạng thái tiếp theo từ một trạng thái hiện tại
def get_next_states(state):
    soi, de, cai, nguoi = state
    next_states = []
    # Các khả năng người có thể chở ai hoặc đi một mình
    for a, b, c in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0)]:
        # Người đi sang bờ bên kia và có thể mang theo 1 thứ
        new_soi = soi ^ (a & 1) if a else soi
        new_de = de ^ (b & 1) if b else de
        new_cai = cai ^ (c & 1) if c else cai
        new_nguoi = nguoi ^ 1  # Người chuyển bờ
        # Chỉ thực hiện nếu người đang cùng bờ với thứ mang theo
        if (a == 0 or soi == nguoi) and (b == 0 or de == nguoi) and (c == 0 or cai == nguoi):
            new_state = (new_soi, new_de, new_cai, new_nguoi)
            if is_valid(new_state):
                next_states.append(new_state)
    return next_states

# Tìm đường đi từ trạng thái đầu đến trạng thái đích
def bfs(start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        current_state, path = queue.popleft()
        if current_state == goal:
            return path
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    return None

# Khởi chạy
start = (0, 0, 0, 0)
goal = (1, 1, 1, 1)

result = bfs(start, goal)
if result:
    for i, state in enumerate(result):
        print(f"Bước {i}: {state}")
else:
    print("Không tìm được đường đi.")
