import math

def get_triangle_number():
  current_number = 0
  i = 1
  while True:
    current_number += i
    i += 1
    yield current_number

def test_triangle_number(num, n):
    global amount_of_divisors
    x = int(math.sqrt(num))
    if x*x == num:
      amount_of_divisors-=1
    for i in range(1,x+1):
      if num % i ==0:
        amount_of_divisors+=2
    if amount_of_divisors > n:
        print (f"the first Triangle number with more than {n} divisors is {num}")

            
amount_of_divisors = 0
triangle_number = get_triangle_number()
n = 500 #Find the first triangle number with more than N divisors

while amount_of_divisors <= n:
    amount_of_divisors = 0
    num = next(triangle_number)
    test_triangle_number(num, n)