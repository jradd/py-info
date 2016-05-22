""" Boolean function to return whether a given value is prime """


def is_prime(n):
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
