def fib(n):
  golden_ratio = (1+(5 ** 0.5)) /2
  return int(round((golden_ratio ** n) / (5 ** 0.5)))

print(fib(6))