from collections import defaultdict, deque

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  def __repr__(self):
    return repr(self.data)
  def children(self):
    return [self.left, self.right]


class tree:
  '''
          9
        /  \ 
      6      11
     / \    / 
    4   8  10 
   / \ 
  2   5

  '''
  def __init__(self):
    self.root = Node(9)
    self.root.left = Node(6)
    self.root.right = Node(11)
    self.root.left.left = Node(4)
    self.root.left.right = Node(8)
    self.root.right.left = Node(10)
    # self.root.right.right = Node(14)
    self.root.left.left.left = Node(2)
    self.root.left.left.right = Node(5)
  def get_tree(self):
    return self.root


def populate_treelist_preorder(root, treelist):
  if root:
    treelist.append(root.data)
    populate_treelist_preorder(root.left, treelist)
    populate_treelist_preorder(root.right, treelist)


def populate_treelist_inorder(root, treelist):
  if root:
    populate_treelist_inorder(root.left, treelist)
    treelist.append(root.data)
    populate_treelist_inorder(root.right, treelist)


def populate_treelist_postorder(root, treelist):
  if root:
    populate_treelist_postorder(root.left, treelist)
    populate_treelist_postorder(root.right, treelist)
    treelist.append(root.data)


def populate_treelist_bfs(root, treelist):
  if root is None: return
  new_queue = deque()
  new_queue.append(root)

  while new_queue:
    r = new_queue.popleft()
    treelist.append(r)
    for child in r.children():
      if child: new_queue.append(child)
  return treelist


def get_tree_list(root, traversal="preorder"):
  treelist = []
  if traversal == "preorder":
    populate_treelist_preorder(root, treelist)
  elif traversal == "inorder":
    populate_treelist_inorder(root, treelist)
  elif traversal == "postorder":
    populate_treelist_postorder(root, treelist)
  elif traversal == "bfs":
    populate_treelist_bfs(root, treelist)
  return treelist


def min_height(node):
  if node is None:
    return 0
  else:
    return min(min_height(node.left), min_height(node.right)) + 1


def max_height(node):
  if node is None:
    return -1
  else:
    return max(max_height(node.left), max_height(node.right)) + 1


def depth(node, level=0, lists=None):
  if not lists: lists = defaultdict(list)
  if node is None:
    return 0
  elif lists.get(node):
    return lists[node]
  else:
    lists[node] = level
    depth(node.left, level+1, lists)
    depth(node.right, level+1, lists)
  
  print(node, lists[node])


# Creates a linked list connecting all nodes at the same level.defaultdict
def populate_linked_list(root, level, lists):
    if not root: return
    lists[level].append(root)
    populate_linked_list(root.left, level+1, lists)
    populate_linked_list(root.right, level+1, lists)


def create_linked_list(root):
    lists = defaultdict(list)
    populate_linked_list(root, 0, lists)
    return dict(lists)


if __name__ == "__main__":
  print("The file defines all the functions.")