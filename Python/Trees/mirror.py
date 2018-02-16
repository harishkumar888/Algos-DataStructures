import tree


def mirror(node):
    if not node: return
    mirror(node.left)
    mirror(node.right)
    node.left, node.right = node.right, node.left

tree_obj = tree.tree()
root = tree_obj.get_tree()
print("Org: ", tree.get_tree_list(root, "bfs"))
mirror(root)
print("Mirror", tree.get_tree_list(root, "bfs"))



