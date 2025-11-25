def character_replacement(s, k):
  count = {}
  res = 0  
  l = 0
  max_f = 0
  
  for r in range(len(s)):
    right_char = s[r]
    count[right_char] = 1 + count.get(right_char, 0)
    max_f = max(max_f, count[right_char])
    
    while (r - l + 1) - max_f > k:
      left_char = s[l]
      count[left_char] -= 1
      l += 1
    res = max(res, r - l  + 1)
  
  return res

print(character_replacement("ABAB", 2))
    