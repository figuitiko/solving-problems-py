def can_construct(ransom_notes, magazine):
  counter = {}
  for c in magazine:
    if c in counter:
      counter[c] += 1
    else:
      counter[c] = 1
  
  for c in ransom_notes:
    if c not in counter:
      return False
    elif c == 1:
      del counter[c]
    else:
      counter[c] -= 1
  return True

print(can_construct("aa", "aab"))
