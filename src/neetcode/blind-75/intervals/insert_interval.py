def insert(intervals, new_interval):
  res = []
  
  for i in range(len(intervals)):
    if new_interval[i] < intervals[i][0]:
      res.append(new_interval)
      return res + intervals[i:]
    elif new_interval[0] > intervals[i][1]:
      res.append(intervals[i])
    else:
      new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[i], intervals[i][1])]

  res.append(new_interval)
  
  return res

print(insert([[1,3], [6,9]], [2,5]))