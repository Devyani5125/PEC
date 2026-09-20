graph = {}
h = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node: ")
    neighbours = input("Enter neighbours: ").split()
    graph[node] = neighbours
    h[node] = int(input("Enter heuristic value: "))

start = input("Enter starting node: ")
goal = input("Enter goal node: ")

open_list = [(h[start], 0, start)]
visited = []

while open_list:
    open_list.sort()
    f, g, current = open_list.pop(0)

    if current in visited:
        continue

    visited.append(current)
    print(current, end=" ")

    if current == goal:
        print("\nGoal found!")
        break

    for neighbour in graph.get(current, []):
        new_g = g + 1
        new_f = new_g + h[neighbour]
        open_list.append((new_f, new_g, neighbour))

print("\nA* Search:", visited)
