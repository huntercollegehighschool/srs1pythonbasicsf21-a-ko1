"""
Define a function twodigitodd that take a single integer argument (number). The function should return True if the number is a two digit odd number, and False if it is not.
"""

def twodigitodd(number):
  if number/10 >= 1 and number % 2 == 1:
    return True
  return False
