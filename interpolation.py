"""
Interpolation
Write code that calculates the probability of a sequence using a unigram, bigram, and trigram model, with interpolation.

We will assume that the probability of START is 1 (ie., P(START) = 1), All queries will start with START and end with END.

Program name - q8_interpolation.py

Function name - process_input

Arguments:

input_filename, a string, the name of a file with ngram counts. Each line in the file will have a number, a space, and an ngram.

ngram , a list of strings, an ngram that the probability should be calculated for.

weights , a list of floats, with the interpolation weights (for unigram, bigram, and trigram models in that order).

Return value - The probability of the ngram.

Example
Input arguments:

data.tiny-sample.interpolation.txt 

["START", "I", "eat", "NLP", "END"] 

[0.2, 0.4, 0.4]

Return: 0.00180625

If your answer does not match, please ensure you have the latest version of the data file by resetting this part to scaffold (see instructions in the first question). Note, when you do so, it will clear your code, so make sure to save it somewhere else before resetting.
"""
import math

def get_prob(full, context, counts):
    full_count = counts.get(full, 0)
    context_count = counts.get(context, 0)
    if context_count == 0:
        return 0
    else:
        return full_count / context_count

def process_input(input_filename: str, ngram: list[str], weights: list[float]):
    # Get counts
    counts = {}
    unigram_total = 0
    with open(input_filename) as src:
        for line in src:
            parts = line.strip().split()
            count = int(parts[0])
            tgram = tuple(parts[1:])
            counts[tgram] = count
            if len(tgram) == 1 and tgram != 'START':
                unigram_total += count

    ngram = ["START"] + ngram
    # Get probs
    logprob = 0
    for i in range(len(ngram) - 2):
        trigram_context = tuple(ngram[i:i+2])
        trigram_full = tuple(ngram[i:i+3])
        bigram_context = tuple(ngram[i+1:i+2])
        bigram_full = tuple(ngram[i+1:i+3])
        unigram = (ngram[i+2], )

        trigram_prob = get_prob(trigram_full, trigram_context, counts)
        bigram_prob = get_prob(bigram_full, bigram_context, counts)
        unigram_prob = counts[unigram] / unigram_total

        prob = unigram_prob * weights[0] + bigram_prob * weights[1] + trigram_prob * weights[2]
        if prob == 0:
            return 0

        logprob += math.log(prob)

    return math.exp(logprob)