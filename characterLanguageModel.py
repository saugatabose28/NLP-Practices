"""
Character Language Model
An alternative to using UNK is to build a language model with pieces of language that are smaller than words, e.g., characters. If we have a model that includes every character then we can generate any output, and so the unknown word problem is resolved.

Write code that uses counts to estimate the probability of a character sequence. For this part of the assignment, you will calculate a Markov approximation. We will use the special character ^ to indicate the start of a character sequence and $ for the end of a character sequence (that is the only place they will ever occur). The probability of ^ is 1 (ie., P(^) = 1),

You may assume that all ngrams start with ^ and end with $ . Note that a space is a valid character in the data and query ngram.

Program name - q6_char.py

Function name - process_input

Arguments:

input_filename, a string, the name of a file. The file will contain a series of lines. Each line will contain a count, a space, and a character ngram.

N , an integer, the order of the ngram to use.

ngram , a list of strings, an ngram that the probability should be calculated for.

Return value - The probability of the ngram.

Example 1
Input arguments:

data.tiny-sample.char.txt

1

["^", "A", " ", "p", "a", "?", "$"]

Return: 5.358367626886151e-06

Example 2
Input arguments:

data.tiny-sample.char.txt

2

["^", "A", " ", "p", "a", "?", "$"]

Return: 0.25

Example 3
Input arguments:

data.tiny-sample.char.txt

3

["^", "A", " ", "p", "a", "?", "$"]

Return: 0.0 

If your answer does not match those above, please ensure you have the latest version of the data file by resetting this part to scaffold (see instructions in the first question). Note, when you do so, it will clear your code, so make sure to save it somewhere else before resetting.
"""
import math

def get_count(ngram, counts, counts_all_unigrams):
    if len(ngram) == 0:
        return counts_all_unigrams
    elif ngram in counts:
        return counts[ngram]
    else:
        return 0

def process_input(input_filename: str, N: int, ngram: list[str]):
    counts = {}
    counts_all_unigrams = 0
    with open(input_filename) as src:
        for line in src:
            # Remove the trailing newline
            line = line[:-1]

            # Split the line up
            split_point = line.index(" ")
            num = int(line[:split_point])
            tgram = line[split_point+1:]

            # Record the count
            counts[tgram] = num
            if len(tgram) == 1 and tgram not in ["^"]:
                counts_all_unigrams += num

    
    logprob = 0
    for i in range(len(ngram) - N + 1):
        if N == 1 and ngram[i] == '^':
            continue
        context = "".join(ngram[i:i+N-1])
        full = "".join(ngram[i:i+N])
        context_count = get_count(context, counts, counts_all_unigrams)
        full_count = get_count(full, counts, counts_all_unigrams)

        if full_count > 0 and context_count > 0:
            logprob += math.log(full_count / context_count)
        else:
            return 0

    return math.exp(logprob)
