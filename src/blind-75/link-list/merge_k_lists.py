from class_list_node import List_Node

def merge_k_lists(lists):
  
  def merge_two_lists(l1, l2):
    dummy = List_Node(0)
    tail = dummy

    while l1 and l2:
      if l1.val < l2.val:
        tail.next = l1
        l1 = l1.next
      else:
        tail.next = l2
        l2 = l2.next
      tail = tail.next

    if l1:
      tail.next = l1
    if l2:
      tail.next = l2
    return dummy.next
  
  if not lists or len(lists) == 0:
    return None
  
  while len(lists) > 1:
    
    merged = []

    for i in range(0, len(lists), 2):
      l1 = lists[i]
      l2 = lists[i + 1] if (i + 1) < len(lists) else None
      merged.append(merge_two_lists(l1 , l2))
    lists = merged

  return lists[0]
