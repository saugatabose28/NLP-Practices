"""
Exhaustive Search
In this question, you should explicitly consider every possible sequence labelling.

For example, in the two word sequence from the overview, Australia ! you should calculate the scores for:

LOC LOC

LOC O

O LOC

O O

Then return the highest probability sequence and its probability.

Note that, as discussed in lectures, this method does not scale well to long sequences or large sets of labels. All the test cases in this question will be small, so that isn't an issue.

We encourage you to use the itertools.product function (https://docs.python.org/3/library/itertools.html#itertools.product) in your implementation.
"""
import itertools

def exhaustive(tokens, distributions, transitions, labels):
    best = []
    for option in itertools.product(labels, repeat=len(tokens)):
        score = 1.0
        previous_label = "START"
        for label, distribution in zip(option, distributions):
            score *= distribution[label]
            score *= transitions[previous_label, label]
            previous_label = label
        score *= transitions[previous_label, "END"]
        if len(best) == 0:
            best = [(score, option)]
        elif score > best[0][0]:
            best = [(score, option)]
        elif score == best[0][0]:
            best.append((score, option))
    best.sort(reverse=True)
    return best[0]