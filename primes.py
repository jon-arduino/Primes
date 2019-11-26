max_primes = 100
print("Compute all primes less than", max_primes)
prime_list=[]

for number in range(2,max_primes):
  its_a_prime=1
  for prime in prime_list:
      if (number % prime == 0):     # if number is not a prime
          its_a_prime=0
          break
  if (its_a_prime):
      prime_list = prime_list + [number]
      print(number)


