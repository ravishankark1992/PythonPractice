class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        from collections import defaultdict
        lookup = defaultdict(list)

        for u,v in prerequisites:
            lookup[u].append(v)
        
        visited = []
        children=[]
        print(lookup)
        def DFS(n, children):
            for i, j in lookup.items():
                print(visited)
                if i in visited:
                    return False
                else:
                    visited.append(i)
                    children.append(lookup[i])
                    out = DFS(n, children)

                    if not out:
                        return False
                print(lookup[i])
                visited.pop()
            return True
        return DFS(numCourses, [])

x=Solution()
y=x.canFinish(4, [[1,0],[2,3]])
print(y)