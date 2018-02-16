import tree

tree_obj = tree.tree()
root = tree_obj.get_tree()

node_obj = tree.Node(5)

assert tree.get_tree_list(root, "preorder") == [9, 6, 4, 2, 5, 8, 11, 10]
assert tree.get_tree_list(root, "inorder") == [2, 4, 5, 6, 8, 9, 10, 11]
assert tree.get_tree_list(root, "postorder") == [2, 5, 4, 8, 6, 10, 11, 9]

assert tree.min_height(root) == 2
assert tree.max_height(root) == 3

assert node_obj.data == 5

print(tree.create_linked_list(root))
# assert tree.create_linked_list(root) == {0: [9], 1: [6, 11], 2: [4, 8, 10], 3: [2, 5]}



