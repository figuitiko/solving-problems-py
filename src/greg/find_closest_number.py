def find_closest_number(nums):
  closest = nums[0]
  for x in nums:
    if abs(x) < abs(closest):
      closest = x
      
  if closest < 0 and abs(closest) in nums:
    return abs(closest)
    
  return closest
  
print(find_closest_number([2, -1, 1]))