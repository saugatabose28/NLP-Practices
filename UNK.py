"""
Using UNK for Rare Words
In this section, we will use the special symbol UNK to account for rare words. Write code that:

Reads a file of text

Replaces every word that only appears once with UNK

Creates a bigram language model

Calculates the probability of a piece of given text

 We will assume that the probability of START is 1 (ie., P(START) = 1), All queries will start with START and end with END.

Program name - q5_unk.py

Function name - process_input

Arguments:

input_filename, a string, the name of a file with test.

ngram , a list of strings, an ngram that the probability should be calculated for.

Return value - The probability of the ngram.

Example
Input arguments:

data.tiny-sample.unk.txt

["START", "I", "love", "books", "END"]

Return: 0.5

Note that data.tiny-sample.unk.txt can be viewed in your workspace for this slide. It contains:

I love NLP
I love learning
I love chocolate
I love chocolate most
If your answer does not match the one above, please ensure you have the latest version of the data file by resetting this part to scaffold (see instructions in the first question). Note, when you do so, it will clear your code, so make sure to save it somewhere else before resetting.
"""
import math

def process_input(input_filename: str, ngram: list[str]):
    # Count tokens
    token_counts = {}
    with open(input_filename) as src:
        for line in src:
            for word in line.strip().split():
                token_counts[word] = token_counts.get(word, 0) + 1

    # Count ngrams
    counts = {}
    with open(input_filename) as src:
        for line in src:
            # Add special start and end symbols
            words = ['START'] + line.strip().split() + ['END']

            # Insert UNKs
            for i, word in enumerate(words):
                if word in ['START', 'END']:
                    continue
                if token_counts[word] == 1:
                    words[i] = "UNK"

            # Count ngrams
            for n in [1, 2]:
                for i in range(len(words) - n + 1):
                    tgram = tuple(words[i:i+n])
                    counts[tgram] = counts.get(tgram, 0) + 1

    # Insert UNKs for ngram
    for i, word in enumerate(ngram):
        if word in ['START', 'END']:
            continue
        if token_counts.get(word, 0) <= 1:
            ngram[i] = "UNK"

    # Calculate probability
    logprob = 0
    for i in range(len(ngram) - 2 + 1):
        context = ngram[i:i+1]
        full = ngram[i:i+2]
        context_count = counts.get(tuple(context), 0)
        full_count = counts.get(tuple(full), 0)

        if full_count > 0 and context_count > 0:
            logprob += math.log(full_count / context_count)
        else:
            return 0

    return math.exp(logprob)