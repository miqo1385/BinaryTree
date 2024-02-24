import unittest
from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Pre order
def preorder(node):
    result = []
    if node:
        # print(node.value, end= ' ')
        result.append(node.value)
        result += preorder(node.left)
        result += preorder(node.right)
    return result


# In order
def inorder(node):
    result = []
    if node:
        result += inorder(node.left)
        result.append(node.value)
        # print(node.value, end = ' ')
        result += inorder(node.right)
    return result


# Post order
def postorder(node):
    result = []
    if node:
        result += postorder(node.left)
        result += postorder(node.right)
        # print(node.value, end = ' ')
        result.append(node.value)
    return result


# Level order
def levelorder(node):
    result = []
    queue = deque([node])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result


# Creating a simple binary tree
root = TreeNode('10')
root.left = TreeNode('5')
root.left.left = TreeNode('3')
root.left.right = TreeNode('9')
root.right = TreeNode('20')
root.right.left = TreeNode('15')
root.right.right = TreeNode('25')


# Create another example

class ourFunctionTests(unittest.TestCase):
    def test_01(self):
        self.assertEqual(preorder(root), ['10', '5', '3', '9', '20', '15', '25'])

    def test_02(self):
        self.assertEqual(inorder(root), ['3', '5', '9', '10', '15', '20', '25'])

    def test_03(self):
        self.assertEqual(postorder(root), ['3', '9', '5', '15', '25', '20', '10'])

    def test_04(self):
        self.assertEqual(levelorder(root), ['10', '5', '20', '3', '9', '15', '25'])


if __name__ == '__main__':
    unittest.main()

# Test
# print('Pre order')
# print(preorder(root))
# print('\nIn order')
# print(inorder(root))
# print('\nPost order')
# print(postorder(root))
