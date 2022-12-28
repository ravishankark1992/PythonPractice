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


# needed:
# Visited, loop, check condition for search node
#
# a
# a
# and


def bfs(search_key: str, root_node: str, graph_map: Dict) -> bool:
    visited = []
    new_queue = []
    new_queue.append(root_node)
    i = 0
    while len(new_queue) > 0 and i < 10:
        print("queue", new_queue)
        current_node = new_queue.pop(-1)
        if current_node == search_key:
            print("found key:", current_node)
            return True
        else:
            visited.append(current_node)
            print("visited:", visited)
        children = graph_map[current_node]
        print("children:", children)
        for child in children:
            if child not in visited and child not in new_queue:
                new_queue.append(child)
        i += 1
    return False


root_node = "A"
search_key = "D"
print(bfs(search_key, root_node, graph))
