graph, heu = {}, {}
nodes = [input("Enter node: ") for _ in range(int(input("Number of nodes: ")))]
for _ in range(int(input("Number of edges: "))):
    s, e, cost = input("Enter start, end, cost: ").split()
    graph.setdefault(s, []).append((e, int(cost)))
    graph.setdefault(e, []).append((s, int(cost)))
for node in nodes:
    heu[node] = int(input(f"Enter heuristic for {node}: "))
startn, goaln = input("Enter start and goal: ").split()

open_set, closed_set = [(startn, 0)], set()
g_scores, came_from = {startn: 0}, {}
while open_set:
    current_node = min(open_set, key=lambda x: g_scores.get(x[0], float('inf')) + heu.get(x[0], float('inf')))
    open_set.remove(current_node)
    if current_node[0] == goaln: break
    closed_set.add(current_node[0])
    for neighbor, cost in graph.get(current_node[0], []):
        if neighbor in closed_set: continue
        tentative_g_score = g_scores[current_node[0]] + cost
        if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
            came_from[neighbor] = current_node[0]
            g_scores[neighbor] = tentative_g_score
            if neighbor not in [n[0] for n in open_set]:
                open_set.append((neighbor, tentative_g_score))

path = [goeln]
while current := came_from.get(current): path.append(current)
path.reverse()
print("Path from start to goal:", path)