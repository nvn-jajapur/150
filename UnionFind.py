class UnionFind:
    def __init__(self):
        self.parent={}
        self.weights={}
    def add(self, x):
        if x not in self.parent:
            self.parent[x]=x
            self.weights[x] =1
    def findP(self, x):
        if x!=self.parent[x]:
            self.parent[x] = self.findP(self.parent[x])
        return self.parent[x]
    def findUnionBySize(self, x, y):
        self.add(x)
        self.add(y)
        parentX = self.findP(x)
        parentY = self.findP(y)
        if parentX == parentY: return
        elif self.weights[parentX] < self.weights[parentY]:
            self.parent[parentX] = parentY
            self.weights[parentY]+=self.weights[parentX]
        else:
            self.parent[parentY] = parentX
            self.weights[parentX]+=self.weights[parentY]
class Solution:
    union = UnionFind()
    union.findUnionBySize(1,2)
    union.findUnionBySize(2,3)
    union.findUnionBySize(4,5)
    union.findUnionBySize(6,7)
    union.findUnionBySize(5,6)
    if (union.findP(3) == union.findP(7)):
        print("same")
    else: print("Not Same")
    union.findUnionBySize(3,7)
    if (union.findP(3) == union.findP(7)):
        print("same")
    else: print("Not Same")