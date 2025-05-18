graph = {
    'A' : {'B' : 1, 'C' : 3, 'D' : 5},
    'B' : {'E' : 8, 'F' : 6},
    'C' : {'G' : 4},
    'D' : {'H' : 2, 'I' : 4, 'J' : 6},
    'E' : {'K' : 1},
    'F' : {},
    'G' : {'L' : 3, 'M' : 5},
    'H' : {},
    'I' : {'N' :7, 'O' : 2},
    'J' : {'P' : 4},
    'K' : {}, 'L' : {}, 'M' : {}, 'N' : {}, 'O' : {}, 'P' : {}
}

h = {
    'A': 3,
    'B': 5,
    'C': 2,
    'D': 6,
    'E': 1,
    'F': 10,
    'G': 6,
    'H': 4,
    'I': 8,
    'J': 12,
    'K': 9,
    'L': 3,
    'M': 2,
    'N': 1,
    'O': 6,
    'P': 5
}

# def print_path_and_cost(start, goals, parent, g):

#     path = []
#     current = goals

#     while current != start:
#         path.append(current)
#         current = parent[current]

#     path.append(start)
#     path.reverse()

#     print ('Đường đi: ', '->'.join(path))
#     print ('Chi phí: ', g[goals])



# def AT(start, goals, graph):
#     OPEN = [start]
#     CLOSED = []
#     parent = {}
#     g = {start:0}

#     while OPEN:
#         min_cost = float('inf')
#         n = None
#         for vertex in OPEN:
#             cost = g[vertex] if vertex in g else float('inf')
#             if  cost < min_cost:
#                 min_cost = cost
#                 n = vertex


#         if n in goals:
#             print ('Đã tìm thấy đích: ', n)
#             print_path_and_cost(start, n, parent, g)
#             return

#         OPEN.remove(n)
#         CLOSED.append(n)

#         for m in graph.get(n, {}):
#             cost = graph[n][m]
#             new_cost = cost + g[n]
#             if m not in g or  new_code < g[m]:
#                 g[m] = new_cost
#                 parent[m] = n

#             if m not in OPEN and m not in CLOSED:
#                 OPEN.append(m)

#     print('Không tìm được')
#     return False



def print_path_and_cost(start, goals, parent, f):
    path = []
    current = goals

    while current != start:
        path.append(current)
        current = parent[current]
    
    path.append(start)
    path.reverse()

    print ('Đường đi: ', '->'.join(path))
    print ('Chi phí', f[goals])


def Asao(start, goals, graph, h):
    OPEN = [start]
    g = {start:0}
    f = {start: h[start]}
    CLOSED = []
    parent = {}

    while OPEN:
        min_f = float('inf')
        n = None
        for node in OPEN:
            if f[node] < min_f:
                min_f = f[node]
                n = node
        

        if n in goals:
            print ('Đã tìm được!')
            print_path_and_cost(start, n, parent, f)
            return

        OPEN.remove(n)
        CLOSED.append(n)

        for m in graph.get(n, {}):
            cost = graph[n][m]
            new_cost = g[n] + cost

            if m not in g or new_cost < g[m]:
                g[m] = new_cost
                f[m] = g[m] + h[m]
                parent[m] = n

            if m not in OPEN and m not in CLOSED:
                OPEN.append(m)
            
    print('Không tìm được!')
    return False


start = 'A'
goals = 'K'
# AT(start, goals, graph)
Asao(start, goals, graph, h)



