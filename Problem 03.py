""" The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? """

x = 2
number = 600851475143
while (x*x) <= number:
   if number%x == 0:
      number = number/x
   else:
      x = x + 1
print()
print(number)
