from collections import deque, defaultdict
from tree import Node, tree, max_height, min_height, depth

def create_list(root):
  ll = defaultdict(list)
  if root is None: return
  new_queue = deque()
  new_queue.append(root)

  while new_queue:
    r = new_queue.popleft()
    h_r = min_height(r)
    # print(r, h_r)
    print(depth(r))
    # ll[h_r].append(r)
    for child in r.children():
      if child: new_queue.append(child)  
  return ll

root = tree().get_tree()
print(depth(root))
# print(dict(create_list(root)))

