def contain_duplicate(nums):
  h = set()
  for num in nums:
    if num in h:
      return True
    else:
      h.add(num)
  return False