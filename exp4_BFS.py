graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

h = {'A': 5, 'B': 2, 'C': 3, 'D': 0, 'E': 1}

open = ['A']

while open:
    node = open.pop(0)
    print(node, end=" ")

    if node == 'D':
        print("\nGoal found!")
        break

    for x in graph[node]:
        open.append(x)

    open.sort(key=lambda x: h[x])
