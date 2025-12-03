def two_sum(nums, target):
  h = {}
  for i in range(len(nums)):
    h[nums[i]] = i
  for i in range(len(nums)):
    y = target - nums[i]
    
    if y in h and h[y] != i:
      return [i, h[y]]
    
print(two_sum([2,7,4,3], 9))
    