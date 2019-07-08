def isSymmetric(self, root):
    if root is None:
        return True
    return self.isSymmetricHelp(root.left, root.right)

def isSymmetricHelp(self, left, right):
    if left is None or right is None:
        return left == right
    if left.val != right.val:
        return False
    return self.isSymmetricHelp(left.left, right.right) and self.isSymmetricHelp(left.right, right.left)
