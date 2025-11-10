from class_list_node import List_Node

def reverse_list_iterative(head):
  prev, curr = None, head

  while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
  return prev

# Create a linked list: 1 -> 2 -> 3 -> 4
node4 = List_Node(4)
node3 = List_Node(3, node4)
node2 = List_Node(2, node3)
node1 = List_Node(1, node2)

# Use your function
reversed_head = reverse_list_iterative(node1)

print(node1)

def reverse_list_recursive(head):
  if not head:
    return None
  
  new_head = head
  if head.next:
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
  head.next = None
  return new_head
