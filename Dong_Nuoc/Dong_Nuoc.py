from collections import deque


# Dung dịch tối đa của bình
max_x = 4
max_y = 3

#Kiểm tra trạng thái đích
def isGoat(state):
    x, y = state
    return x == 2


#Hàm sinh trạng thái con
def sinh_son(state):
    x, y = state
    neighbors = []

    # luật 1:
    if x < max_x:
        neighbors.append((max_x, y))

    #luật 2:
    if y < max_y:
        neighbors.append((x, max_y ))

    #luật 3:
    if x > 0:
        neighbors.append((0, y))

    #luật 4:
    if y > 0:
        neighbors.append((x, 0))

    #luật 5:
    if x + y >= max_x and y > 0:
        neighbors.append((max_x, y - (max_x - x)))

    #luật 6:
    if x + y >= max_x and x > 0:
        neighbors.append((x - (max_y - y), max_y))

    #Luật 7:
    if x + y < max_x and y > 0:
        neighbors.append((x + y, 0))


    #Luật 8:
    if x + y < max_y and x > 0:
        neighbors.append((0, x + y))

    return neighbors


#BFS
def bfs(start):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()
        if isGoat(current):
            return path
        for next_state in sinh_son(current):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    return None

state = (0, 0)
solve = bfs(state)
if solve:
    for i,state in enumerate(solve):
        print(f"Bước {i}: {state}")
else:
    print("Không giải đuược bài")

