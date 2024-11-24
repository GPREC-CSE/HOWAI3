def create_graph():
    n = int(input("Enter number of nodes: "))
    G = []
    print("Enter adjacency matrix:")
    for i in range(n):
        row = list(map(int, input().split()))
        G.append(row)
    return G

def color_graph(G):
    n = len(G)
    colors = ["Blue", "Red", "Yellow", "Green"]
    result = [-1] * n
    result[0] = 0

    available = [False] * len(colors)

    for u in range(1, n):
        for i in range(n):
            if G[u][i] == 1 and result[i] != -1:
                available[result[i]] = True

        color = 0
        while color < len(colors):
            if not available[color]:
                break
            color += 1

        result[u] = color
        available = [False] * len(colors)

    return {chr(97 + i): colors[result[i]] for i in range(n)}

G = create_graph()
theSolution = color_graph(G)
print(theSolution)
for node, color in sorted(theSolution.items()):
    print(f"Node {node} = {color}")
