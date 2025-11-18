def can_attend(intervals):
  intervals.sort(key = lambda i : i[0])

  for i in range(1, len(intervals)):
    i1 = intervals[i-1]
    i2 = intervals[i]

    if i1[0] > i2[1]:
      return False
  return True

print(can_attend([(0,30), (5,10), (15,20)]))