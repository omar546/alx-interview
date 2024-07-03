#!/usr/bin/python3
"""Prime Game Module"""

def get_prime_numbers(limit):
    """
    Returns a list of prime numbers between 1 and the specified limit (inclusive).
    
    Args:
        limit (int): Upper boundary of range. The lower boundary is always 1.
    
    Returns:
        list: List of prime numbers within the specified range.
    """
    primes = []
    is_prime = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num, limit + 1, num):
                is_prime[multiple] = False
    return primes

def determine_winner(rounds, limits):
    """
    Determines the winner of the Prime Game.
    
    Args:
        rounds (int): Number of rounds of the game.
        limits (list of int): Upper limits of the range for each round.
    
    Returns:
        str: Name of the winner (Maria or Ben) or None if no winner can be determined.
    """
    if not rounds or not limits:
        return None
    
    maria_score = 0
    ben_score = 0
    
    for i in range(rounds):
        primes = get_prime_numbers(limits[i])
        if len(primes) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    
    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    return None
