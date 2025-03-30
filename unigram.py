"""
Unigram Language Model
Write code that calculates the probability of a sequence using a unigram Markov approximation.

Program name - q2_unigram.py

Function name - process_input

Arguments:

input_filename, a string, the name of a file with unigram counts. Each line in the file will have a number, a space, and an unigram.

ngram , a list of strings, an ngram that the probability should be calculated for.

Return value - The probability of the ngram.

Example 1
Input arguments:

data.tiny-sample.unigram.txt

["I"] 

Return: 0.4

Note that data.tiny-sample.unigram.txt can be viewed in your workspace for this slide. It contains:

3 chocolate
3 eat
4 I
Example 2
Input arguments:

data.tiny-sample.unigram.txt

 ["I", "eat", "chocolate"]

Return: 0.036

Example 3
Input arguments:

data.tiny-sample.unigram.txt

["chocolate", "eat", "I"]

Return: 0.036

If your answer does not match those above, please ensure you have the latest version of the data file by resetting this part to scaffold (see instructions in the first question). Note, when you do so, it will clear your code, so make sure to save it somewhere else before resetting.
"""

import math

def get_prob(full, context, counts):
    full_count = counts.get(full, 0)
    context_count = counts.get(context, 0)
    if context_count == 0:
        return 0
    else:
        return full_count / context_count

def process_input(input_filename: str, ngram: list[str]):
    # Get counts
    counts = {}
    unigram_total = 0
    with open(input_filename) as src:
        for line in src:
            parts = line.strip().split()
            count = int(parts[0])
            tgram = parts[1]
            counts[tgram] = count
            unigram_total += count

    # Get probs
    logprob = 0
    for word in ngram:
        if word not in counts:
            return 0
        prob = counts[word] / unigram_total
        if prob == 0:
            return 0
        logprob += math.log(prob)
    return math.exp(logprob)
