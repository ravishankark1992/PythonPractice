
from collections import defaultdict
class TreeNode:
    def __init__(self, val="", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

C=TreeNode(val="s3")
D=TreeNode(val="s4")
F=TreeNode(val="s2*")
E=TreeNode(val="s1*", right=F)
B=TreeNode(val="s2", left=C, right=D)
A=TreeNode(val="s1", left=B)
DC = TreeNode(val="DC", left=A, right=E)

class test:
    res = defaultdict(list)
    def build_datacenter(self, dataset):
        out = self.dfs(dataset)
        return self.res

    def dfs(self, node) -> int:
        if node == None:
            return 0
        depth = max(self.dfs(node.left),self.dfs(node.right))
        self.res[depth].append(node.val)
        #self.res[ld].append(node.val)
        #self.res[rd].append(node.val)

        #print(self.res)
    
        return 1 + depth
    

out = test().build_datacenter(DC)
result=[]
# for k,v in out.items():
for i in range(len(out)-1):
    print(out[i])
    result.append(out[i])
#print(result)