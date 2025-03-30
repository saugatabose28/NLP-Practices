"""
Trigram Language Model
Write code that calculates the probability of a sequence using a trigram Markov approximation.

For now, we will assume that the probability of START and START START are 1 (ie., P(START) = P(START START) = 1), so you can use just trigrams for all of the calculation. You may assume that all ngrams start with START START . All queries will start with START and end with END.

Program name - q3_trigram.py

Function name - process_input

Arguments:

input_filename, a string, the name of a file with ngram counts. Each line in the file will have a number, a space, and an ngram.

ngram , a list of strings, an ngram that the probability should be calculated for.

Return value - The probability of the ngram.

Example 1
Input arguments:

data.tiny-sample.trigram.txt

["START", "I", "eat", "chocolate", "END"]

Return: 0.75

Note that data.tiny-sample.trigram.txt can be viewed in your workspace for this slide. It contains:

4 START START
4 START I
1 I END
4 END END
4 START START I
1 START I END
1 I END END
3 I eat
3 eat chocolate
3 chocolate END
3 START I eat
3 I eat chocolate
3 eat chocolate END
3 chocolate END END

Example 2
Input arguments:

data.tiny-sample.trigram.txt

["START", "chocolate", "eat", "I", "END"]

Return: 0.0

If your answer does not match those above, please ensure you have the latest version of the data file by resetting this part to scaffold (see instructions in the first question). Note, when you do so, it will clear your code, so make sure to save it somewhere else before resetting.

"""
import math

def trigram_lm(ngram: list[str], counts: int):
    # Get probs
    logprob = 0
    for i in range(len(ngram) - 2):
        trigram_context = tuple(ngram[i:i+2])
        trigram_full = tuple(ngram[i:i+3])

        full_count = counts.get(trigram_full, 0)
        context_count = counts.get(trigram_context, 0)
        if context_count == 0:
            return 0
        logprob += math.log(full_count / context_count)

    return math.exp(logprob)

def process_input(input_filename: str, ngram: list[str]):
    # Get counts
    counts = {}
    unigram_total = 0
    with open(input_filename) as src:
        for line in src:
            parts = line.strip().split()
            count = int(parts[0])
            tgram = tuple(parts[1:])
            counts[tgram] = count

    return trigram_lm(ngram, counts)