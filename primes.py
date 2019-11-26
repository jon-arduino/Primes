import sys

max_prime = 100
prime_count=0
if len(sys.argv) >1:
    max_prime = int(sys.argv[1])

print("Count all primes less than", max_prime)
prime_list=[]

for number in range(2,max_prime):
  its_a_prime=1
  for prime in prime_list:
      if (number % prime == 0):     # if number is not a prime
          its_a_prime=0
          break
  if (its_a_prime):
      prime_list = prime_list + [number]
      prime_count += 1
      # print(number)

print("total primes found less than",max_prime,"=",prime_count)
#print("size of list = ",len(prime_list) )
