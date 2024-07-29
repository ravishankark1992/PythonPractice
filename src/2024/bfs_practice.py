from typing import Dict
from queue import Queue
from collections import deque

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
    children = deque()

    children.append(root_node)
    while children:
        child = children.popleft()
        print(child)
        if child == search_key:
            print("Found key:", child)
            return True
        if child not in visited:
            visited.append(child)
            new_node = graph_map[child]
        for node in new_node:
            if node not in visited and node not in children:
                children.append(node)

    return False

root_node = "A"
search_key = "F"
print(bfs(search_key, root_node, graph))
