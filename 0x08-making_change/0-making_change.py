#!/usr/bin/python3
"""
Main file for testing the makeChange function.
"""

def makeChange(coins, amount):
    """
    Determine the minimum number of coins needed to make the given amount.
    
    The function uses a greedy algorithm to select the largest coins first.
    It iterates through the sorted list of coins and subtracts as many of
    each coin's value from the amount as possible, keeping a count of the coins used.
    
    Args:
        coins (list): A list of coin denominations.
        amount (int): The total amount of money to make change for.

    Returns:
        int: The minimum number of coins needed to make the amount, or -1 if it is not possible.
    """

    if amount < 1:
        return 0
    
    # Sort coins in descending order
    coins.sort(reverse=True)
    c = 0
    
    for pound in coins:
        if amount == 0:
            break
        
        # Determine how many of the current coin can be used
        n = amount // pound
        amount -= n * pound
        c += n
    
    # Check if we were able to make the exact amount
    return c if amount == 0 else -1
