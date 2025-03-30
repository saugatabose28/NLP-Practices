"""
Counting N-Grams
Write code to count the frequency of all n-grams in the input data. Before counting, add a special token, START at the start of each input line and a special token END at the end of each input line.

Note, every word/token in your ngrams should have a size of 1 or larger. If you split the text up in a way that creates empty strings, do not include them in the ngram.

For all parts of this assignment, your code should have a particular program name and a particular function name with certain arguments. We provide initial starter code in the right format.

For this task:

Program name - q0_count.py

Function name - process_input

Arguments:

input_filename, a string, the name of the text file to read

n, an integer, the size of ngrams to count

Return value - A dictionary, where the keys are tuples of the ngrams and the values are counts of those ngrams in the text file.

Example
Input arguments:

data.tiny-sample.txt

2

Return:

{('START', 'This'): 1, ('This', 'file'): 1, ('file', 'is'): 1, ('is', 'a'): 1, ('a', 'sample'): 1, ('sample', 'file'): 1, ('file', 'END'): 1, ('START', 'It'): 1, ('It', 'has'): 1, ('has', 'two'): 1, ('two', 'lines'): 1, ('lines', 'END'): 1}
Note that data.tiny-sample.txt can be viewed in your workspace for this slide. It contains:

This file is a sample file
It has two lines
If you cannot see that file or it contains different text, please reset to scaffold as shown below:


"""
def process_input(input_filename: str, n: int):
    # Count ngrams
    counts = {}
    with open(input_filename) as src:
        for line in src:
            # Add special start and end symbols
            words = ['START'] + line.strip().split() + ['END']
            for i in range(len(words) - n + 1):
                ngram = tuple(words[i:i+n])
                counts[ngram] = counts.get(ngram, 0) + 1
    return counts