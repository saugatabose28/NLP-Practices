"""
Evaluation - Perplexity
Write code that calculates the perplexity from a probability.

If the probability given is 0, return -1.

Program name - q9_perplexity.py

Function name - process_input

Arguments:

probability , a float, the probability to use

length , an int, the length of the token sequence that this is the probability for

Return value - The perplexity.

Example
Input arguments:

0.01

2

Return: 10
"""

import math

def process_input(probability: float, length: int):
    if probability == 0:
        return -1
    else:
        return math.pow(probability, -1/length)
