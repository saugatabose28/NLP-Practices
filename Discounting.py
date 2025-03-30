"""
Discounting
Write code that calculates the probability of a sequence using a trigram model with discounting.

Do discounting with a uniform distribution over the unseen words (ie., don't weight by the unigram distribution). We will assume that the probability of START is 1 (ie., P(START) = 1) and that START is not generated later in the ngram (ie., it is not part of the vocab when redistributing the discount). All queries will start with START and end with END. If you need to calculate a probability in which the context is unseen, use a uniform probability across the vocabulary.

Program name - q7_discount.py

Function name - process_input

Arguments:

input_filename, a string, the name of a file with ngram counts. Each line in the file will have a number, a space, and an ngram.

ngram , a list of strings, an ngram that the probability should be calculated for.

discount , a float, the discount to apply in the calculation.

Return value - The probability of the ngram.

Example
Input arguments:

data.tiny-sample.discount.txt

["START", "I", "eat", "NLP", "END"]

0.1

Return: 0.00097

If your answer does not match, please ensure you have the latest version of the data file by resetting this part to scaffold (see instructions in the first question). Note, when you do so, it will clear your code, so make sure to save it somewhere else before resetting.
"""
import math

def process_input(input_filename: str, ngram: list[str], discount: float):
    # Get counts
    counts = {}
    seen = {}
    vocab = set()
    with open(input_filename) as src:
        for line in src:
            parts = line.strip().split()
            count = int(parts[0])
            tgram = tuple(parts[1:])
            counts[tgram] = count
            if len(tgram) == 3:
                seen.setdefault(tgram[:2], set()).add(ngram[2])
            for token in tgram:
                if token not in ['START']:
                    vocab.add(token)

    if ngram[1] != 'START':
        ngram = ["START"] + ngram

    # Get probs
    logprob = 0
    for i in range(len(ngram) - 2):
        context = tuple(ngram[i:i+2])
        full = tuple(ngram[i:i+3])
        context_count = counts.get(context, 0)
        full_count = counts.get(full, 0)

        if full_count != 0:
            prob = (full_count - discount) / context_count
            if prob == 0:
                return 0
            logprob += math.log(prob)
        elif context not in seen:
            prob = 1 / len(vocab)
            logprob += math.log(prob)
        else:
            # count seen words
            seen_vocab = seen[context]
            available_prob = len(seen_vocab) * (discount / context_count)
            prob = available_prob / (len(vocab) - len(seen_vocab))
            if prob == 0:
                return 0
            logprob += math.log(prob)
    return math.exp(logprob)