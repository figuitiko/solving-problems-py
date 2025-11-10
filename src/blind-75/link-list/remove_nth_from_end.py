from class_list_node import List_Node

def remove_nth_from_end(head, n):
  dummy = List_Node(0)
  left = dummy
  right = head
  
  while n > 0 and right:
    right = right.next
    n -= 1
  
  while right:
    left = left.next
    right = right.next
    
  left.next = left.next.next
  return dummy.next
  