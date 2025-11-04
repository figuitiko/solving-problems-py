def quick_sort(arr):
  if (len(arr) <= 1):
    return arr
  
  p = arr[-1]

  L = [x for x in arr[:-1] if x <= p]
  R = [x for x in arr[:-1] if x > p]

  L = quick_sort(L)
  R = quick_sort(R)

  return L + [p] + R
B = [-5, 3 , 2 , 1, -3, -3, 7, 2, 2]
quick_sort(B)

print(B)