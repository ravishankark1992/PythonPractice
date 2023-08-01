

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["G"],
    "D": [],
    "E": ["F"],
    "F": [],
    "G": [],
}


class Search:
    def dfs(self, value, root_node):

        visited = []
        children = []
        if value == root_node:
            return "Found"
        visited.append(root_node)
        children.extend(graph[root_node])
        while len(children):
            print(children)
            current_node = children.pop()
            if current_node in children:
                continue
            if value == current_node:
                return "Found"
            visited.append(current_node)
            children.extend(graph[current_node])
        return -1


value = "F"
o = Search()
root_node = "A"
out = o.dfs(value, root_node)
print(out)