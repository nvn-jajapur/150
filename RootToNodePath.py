from typing import List, Optional
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rootToNode(self, root : Optional[TreeNode], k:int)-> bool:
        if not root: return False
        if root.val == k: return True
        stack =[]
        stack.append(root.val)
        print(len(stack))
        if ( self.rootToNode(root.left, k) or self.rootToNode(root.right, k)): 
            return True
        stack.pop()
        return False

def build_tree(vals: List[Optional[int]]) -> Optional[TreeNode]:
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if node:
            # left child
            left_val = vals[i] if i < len(vals) else None
            node.left = TreeNode(left_val) if left_val is not None else None
            queue.append(node.left)
            i += 1
            # right child
            if i < len(vals):
                right_val = vals[i]
                node.right = TreeNode(right_val) if right_val is not None else None
                queue.append(node.right)
                i += 1
    return root
if __name__ =='__main__':
    arr = [1,2,2,3,4,4,3]
    tree = build_tree(arr)
    sol = Solution()
    print(sol.rootToNode(tree,7))