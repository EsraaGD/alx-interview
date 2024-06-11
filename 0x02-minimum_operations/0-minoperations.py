#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to obtain
    exactly `n` characters 'H' in the file starting from a single 'H'.

    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required.
    Returns 0 if `n` is impossible to achieve."""

    if n <= 1:
        return 0

    operations = 0
    divisor = 2  # Start checking with the smallest prime number

    while n > 1:
        # Divide `n` by the current divisor as long as it's divisible
        while n % divisor == 0:
            operations += divisor  # Add the divisor to the operation count
            n //= divisor  # Update `n` by dividing it by the divisor
        divisor += 1  # Move to the next potential divisor

    return operations
