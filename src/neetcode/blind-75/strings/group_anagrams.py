from collections import defaultdict


def group_anagrams(strs):
  res = defaultdict(list)
  
  for s in strs:
    count = [0] * 26
    
    for c in s:
      count[ord(c) - ord("a")] += 1
    key = tuple(count)
    res[tuple(key)].append(s)
  return res.values()

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))