"""
Ngram LM, Exact
Write code that calculates the probability of a sequence without using a Markov approximation.

For this part of the assignment, you will calculate the exact probability (not a Markov approximation). Use the chain rule to decompose the probability into a series of pieces. We will assume that the probability of START is 1 (ie., P(START) = 1), All queries will start with START and end with END.

Program name - q4_exact.py

Function name - process_input

Arguments:

input_filename, a string, the name of a file with ngram counts. Each line in the file will have a number, a space, and an ngram.

ngram , a list of strings, an ngram that the probability should be calculated for.

Return value - The probability of the ngram.

Example
Input arguments:

data.tiny-sample.exact.txt

["START", "I", "eat", "chocolate", "END"]

Return: 0.75

Note that data.tiny-sample.exact.txt can be viewed in your workspace for this slide. It contains:

4 START
4 I
4 END
4 START I
1 I END
1 START I END
3 eat
3 chocolate
3 I eat
3 eat chocolate
3 chocolate END
3 START I eat
3 I eat chocolate
3 eat chocolate END
3 START I eat chocolate
3 I eat chocolate END
3 START I eat chocolate END

Example 2
Input arguments:

data.tiny-sample.exact.txt

["START", "chocolate", "eat", "I", "END"]

Return: 0.0

If your answer does not match those above, please ensure you have the latest version of the data file by resetting this part to scaffold (see instructions in the first question). Note, when you do so, it will clear your code, so make sure to save it somewhere else before resetting.
"""
import math

def process_input(input_filename: str, ngram: list[str]):
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
                if token not in ['START', 'END']:
                    vocab.add(token)

    full_count = counts.get(tuple(ngram), 0)
    start_count = counts.get(("START", ))
    return full_count / start_count