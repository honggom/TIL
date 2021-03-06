# Easy
# 94. Binary Tree Inorder Traversal

class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        return result