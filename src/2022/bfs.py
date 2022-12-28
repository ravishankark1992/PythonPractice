from typing import Dict

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["G"],
    "D": [],
    "E": ["F"],
    "F": [],
    "G": [],
}


def bfs(search_key: str, root_node: str, graph_map: Dict) -> bool:
    visited = []
    node_queue = [root_node]
    while len(node_queue) > 0:
        print(visited)
        current_node = node_queue.pop(0)
        if current_node == search_key:
            print("found key")
            return True
        visited.append(current_node)
        children = graph_map[current_node]
        for child in children:
            if child not in visited and child not in node_queue:
                node_queue.extend(child)
    return False


root = "A"
search_num = "D"
print(bfs(search_num, root, graph))
