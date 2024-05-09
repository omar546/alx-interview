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
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n /= divisor
        divisor += 1

    return operations
