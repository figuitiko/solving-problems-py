from class_tree_node import Tree_Node

def same_tree(p, q):
  if not p and not q:
    return True
  if not p or not q or p.val != q.val:
     return False
  return same_tree(p.left, q.left) and same_tree(p.right, q.right)

three = Tree_Node(3)
two = Tree_Node(2)
one = Tree_Node(1,two, three)

three1 = Tree_Node(3)
two1 = Tree_Node(2)
one1 = Tree_Node(1, two1, three1)

print(same_tree(one, one1))