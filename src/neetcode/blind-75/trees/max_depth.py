from collections import deque


# recursively DFS
def max_depth(root): 
  if not root:
    return 0
  
  return 1 + max(max_depth(root.left), max_depth(root.right))

#  iterative BFS
def max_depth1(root):
  if not root:
    return 0  
  level = 0
  q = deque()
  while q:
    for i in range(len(q)):
      node = q.popleft()
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    level += 1
    
  return level

# iterative DFS

def max_depth2(root):
  if not root:
    return 0
  
  stack = [[root, 1]]
  res = 1
  
  while stack:
    node , depth = stack.pop()
    if node:
      res = max(res, depth)
      stack.append([node.left, depth +1])
      stack.append([node.right, depth +1])
  return res
