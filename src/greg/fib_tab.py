def fib_tab(n):
  if n == 0:
    return 0
  if n == 1:
     return 1
   
  dp =[0] * (n+1)
  dp[0] = 0
  dp[1] = 1
  for i in range(2, n+1):
    dp[i] = dp[i - 2] + dp[i - 1]
    
  return dp[n]

print(fib_tab(6))

def fib_tab_1(n):
  if n == 0:
    return 0
  if n == 1:
     return 1
   
  prev = 0
  curr = 1
  
  for i in range(2, n+1):
    prev, curr = curr, prev + curr
    
  return curr

print(fib_tab_1(6))