def jewels_stone(jewels, stones):
  s = set(jewels)
  count = 0
  
  for stone in stones:
    if stone in s:
      count += 1
  
  return count

jewels = "aA"
stones = "aAAbbb"

print(jewels_stone(jewels, stones))