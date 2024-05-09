#!/usr/bin/python3
'''minimum operations challenge.'''

def minOperations(n):
  """
  Calculates the fewest operations needed to have n 'H' characters.

  Args:
      n: Target number of 'H' characters.

  Returns:
      Minimum number of operations needed to achieve n 'H' characters.
      Returns 0 if n is impossible to achieve.
  """
  if n == 0:
    return 0

  current_chars = 1
  operations = 0

  while current_chars * 2 <= n:
    current_chars *= 2
    operations += 1  

  operations += (n - current_chars) // current_chars

  return operations
