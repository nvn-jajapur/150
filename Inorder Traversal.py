# Definition for a binary tree node.
from typing import List, Optional
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st1 =[]
        ans =[]
        value = root
        while(True):
            if value:
                st1.append(value)
                value = value.left
            else:
                if not value:
                    break
                value = st1.pop()
                ans.append(value)
                value = value.right
        return ans
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        pre =[]
        ino=[]
        post=[]
        stack.append((root,1))
        while stack:
            node, value = stack.pop()
            if value ==1:
                pre.append(node.val)
                value +=1
                stack.append((node,value))
                if node.left:
                    stack.append((node.left,1))
            elif value==2: 
                ino.append(node.val)
                value+=1
                stack.append((node, value))
                if node.right:
                    stack.append((node, 1))
            else:
                post.append(node.val)
        return post
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = collections.deque()
        ans = []
        dq.append(root)
        while dq:
            dqLen = len(dq)
            level =[]
            for i in range(dqLen):
                value = dq.popleft()
                if value:
                    level.append(value.val)
                    dq.append(value.left)
                    dq.append(value.right)
            if level:
                ans.append(level)
        return ans
    def topView(self, root : Optional[TreeNode])->[]:
        stack =[]
        ans =[]
        stack.append(root)
        ans.append(root.val)
        while stack:
            node = root.left
            while node:
                stack.append(node.left)
                ans.append(node.val)
                node = node.left
        return ans
    
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


if __name__ =="__main__":
    arr = [1,2,3,4,None,6,7,5]
    sol = Solution()
    tree = TreeNode(sol)
    # print(sol.inorderTraversal(tree))
    # print(sol.postorderTraversal(tree))
    arr2 = [1,None,2]
    tree2 = build_tree(arr2)
    sol = Solution()
    # print(sol.levelOrder(tree2))
    arr3 = [1,2,3,4,None,6,7,5]
    tree3 = build_tree(arr3)
    print(sol.topView(tree3))