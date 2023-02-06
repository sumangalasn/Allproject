def fibonacci(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a+b
  return a

for i in range(10):
  print(fibonacci(i))