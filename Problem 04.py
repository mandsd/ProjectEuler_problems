for x in range(100,1000):
  for y in range(100,1000):
      z = str(x*y)
      if list(reversed(z)) == list(z):
            print(z)
