class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def create_tree(self):
        tree = TreeNode(4)

        tree.left = TreeNode(2)
        tree.right = TreeNode(7)

        tree.left.left = TreeNode(1)
        tree.left.right = TreeNode(3)
        tree.right.left = TreeNode(6)
        tree.right.right = TreeNode(9)

        tree.left.left.left = TreeNode(10)
        tree.left.left.right = TreeNode(11)
        tree.left.right.left = TreeNode(12)
        tree.left.right.right = TreeNode(13)
        tree.right.left.left = TreeNode(20)
        tree.right.left.right = TreeNode(21)
        tree.right.right.left = TreeNode(22)
        tree.right.right.right = TreeNode(23)
        return tree

    def print_tree(self, tree: TreeNode):
        print(f"""
        {tree.val}
        {tree.left.val} {tree.right.val}
        {tree.left.left.val} {tree.left.right.val} {tree.right.left.val} {tree.right.right.val}
        {tree.left.left.left.val} {tree.left.left.right.val} {tree.left.right.left.val} {tree.left.right.right.val} {tree.right.left.left.val} {tree.right.left.right.val} {tree.right.right.left.val} {tree.right.right.right.val}
            """)

    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)

        root.left = right
        root.right = left
        return root

s = Solution()
tree = s.create_tree()

s.print_tree(tree)
s.print_tree(s.invertTree(tree))
