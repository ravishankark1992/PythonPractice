class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return False
        lookup={}
        tree = {}
        for p in prerequisites:
            tree[p[1]]=p[0]

        b = [x[1] for x in prerequisites]
        print(tree)
        print(b)
        for i in range(numCourses):
            if i in tree:
                if i in lookup:
                    lookup[i].append(tree[i])
                else:
                    lookup[i]=[tree[i]]

        # for val in prerequisites:

        # def bfs():
        print(lookup)
        return False

