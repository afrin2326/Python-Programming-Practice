def graph_color(graph, color_no, result, nodes, node_index):
    if node_index == len(nodes):
        return True

    node = nodes[node_index]
    for color in range(1, color_no + 1):
        isColorValid = True
        for neighbor in graph[node]:
            if result[neighbor] == color:
                isColorValid = False
                break

        if isColorValid:
            result[node] = color
            if graph_color(graph, color_no, result, nodes, node_index + 1):
                return True
            result[node] = 0  # backtrack

    return False


if __name__ == '__main__':
    color_no = 3  # Try with 3 colors
    nodes = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

    graph = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'NSW', 'T'],
        'T': ['V']
    }

    result = {node: 0 for node in nodes}

    isColoringPossible = graph_color(graph, color_no, result, nodes, 0)

    if isColoringPossible:
        print("Coloring solution:")
        for region in result:
            print(f"{region} => Color {result[region]}")
    else:
        print("No solution exists...")
