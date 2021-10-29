"""
The function below is supposed to return True if the integer entered as the argument is prime, and False if it's not. Fix the code so that it runs the way it's supposed to.
"""

factors = []
def isprime(number):
  for i in range(1, number+1):
    if number % i == 0:
      factors.append(i)
  if len(factors) == 2:
    return True
  return False