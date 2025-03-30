"""
Calculating Probabilities
Write code that uses counts to estimate a probability.

Program name - q1_prob.py

Function name - process_input

Arguments:

input_filename, a string, the name of a file with ngram counts. Each line in the file will have a number, a space, and an ngram.

ngram , a list of strings, an ngram that the probability should be calculated for.

Return value - The probability of the last word in the ngram given the sequence of words before it. Do not use any form of smoothing. If an ngram does not occur in the provided data, return a value of 0.

Example 1
Input arguments:

data.tiny-sample.prob.txt

["I", "love", "NLP"]

Return: 0.5

Note that data.tiny-sample.prob.txt can be viewed in your workspace for this slide. It contains:

10 I
2 love
1 NLP
2 I love
1 love NLP
1 I love NLP
9 chocolate
1 love chocolate
1 I love chocolate
8 eat
8 I eat
8 eat chocolate
8 I eat chocolate

Example 2
Input arguments:

data.tiny-sample.prob.txt

["I", "eat"]

Return: 0.8

Example 3
Input arguments:

data.tiny-sample.prob.txt

["I", "eat", "NLP"] 

Return: 0.0

If your answer does not match those above, please ensure you have the latest version of the data file by resetting this part to scaffold (see instructions in the first question). Note, when you do so, it will clear your code, so make sure to save it somewhere else before resetting.
"""

import math

def process_input(input_filename: str, ngram: list[str]):
    # Get counts
    counts = {}
    with open(input_filename) as src:
        for line in src:
            parts = line.strip().split()
            count = int(parts[0])
            tgram = tuple(parts[1:])
            counts[tgram] = count

    # Get probs
    context = tuple(ngram[:-1])
    full = tuple(ngram)

    full_count = counts.get(full, 0)
    context_count = counts.get(context, 0)
    if context_count == 0:
        return 0
    else:
        return full_count / context_count