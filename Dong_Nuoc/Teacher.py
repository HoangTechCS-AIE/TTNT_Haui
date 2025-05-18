from collections import deque

# Hàm kiểm tra xem trạng thái đã là trạng thái mục tiêu chưa
def is_goal_state(state):# là 1 tuple
    return state[0] == 2  # Bình 4 lít phải có 2 lít nước

# Hàm sinh ra các trạng thái con từ trạng thái hiện tại
def get_neighbors(state, capacity_4l, capacity_3l):
    neighbors = []
    jug_4l, jug_3l = state

    # Các hành động có thể thực hiện:

    # 1. Đổ đầy bình 4 lít
    if jug_4l < capacity_4l:
        neighbors.append((capacity_4l, jug_3l))

    # 2. Đổ đầy bình 3 lít
    if jug_3l < capacity_3l:
        neighbors.append((jug_4l, capacity_3l))

    # 3. Đổ nước từ bình 4 lít sang bình 3 lít
    if jug_4l > 0 and jug_3l < capacity_3l:
        transfer = min(jug_4l, capacity_3l - jug_3l)
        neighbors.append((jug_4l - transfer, jug_3l + transfer))

    # 4. Đổ nước từ bình 3 lít sang bình 4 lít
    if jug_3l > 0 and jug_4l < capacity_4l:
        transfer = min(jug_3l, capacity_4l - jug_4l)
        neighbors.append((jug_4l + transfer, jug_3l - transfer))

    # 5. Đổ bỏ nước trong bình 4 lít
    if jug_4l > 0:
        neighbors.append((0, jug_3l))

    # 6. Đổ bỏ nước trong bình 3 lít
    if jug_3l > 0:
        neighbors.append((jug_4l, 0))

    return neighbors

# Hàm giải bài toán bằng BFS
def bfs(capacity_4l, capacity_3l):
    # Trạng thái ban đầu (cả hai bình đều rỗng)
    initial_state = (0, 0)

    # Sử dụng deque để lưu trữ các trạng thái cần duyệt và đường đi tương ứng
    queue = deque([(initial_state, [])])
    visited = set()  # Set để lưu các trạng thá
# Duyệt qua các trạng thái bằng BFS
    while queue:
        current_state, path = queue.popleft()

        # Nếu đã gặp trạng thái mục tiêu, trả về đường đi
        if is_goal_state(current_state):
            return path + [current_state]

        # Thêm trạng thái vào set đã duyệt
        if current_state not in visited:
            visited.add(current_state)

            # Tạo các trạng thái con và đưa vào hàng đợi
            for neighbor in get_neighbors(current_state, capacity_4l, capacity_3l):
                if neighbor not in visited:
                    queue.append((neighbor, path + [current_state]))

    return None  # Nếu không tìm thấy đường đi

# Hàm in ra các bước thực hiện
def print_solution(solution):
    if solution:
        print("Các bước thực hiện:")
        for step in solution:
            print(f"Bình 4 lít: {step[0]} lít, Bình 3 lít: {step[1]} lít")
    else:
        print("Không tìm thấy giải pháp!")

# Dung tích của các bình
capacity_4l = 4
capacity_3l = 3

# Giải bài toán
solution = bfs(capacity_4l, capacity_3l)

# In kết quả
print_solution(solution)