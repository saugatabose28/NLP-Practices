"""
Viterbi Search
In this question, use Viterbi search to identify the highest probability label sequence.

For the Viterbi algorithm, we think about label sequences as paths through a lattice / grid. For example, here is a blue path through the red lattice of LOC and O labels for "Sydney is in Australia".


If you think of this like a graph, where each label is a node, then we are trying to find the path with the highest value. The Viterbi algorithm finds the highest probability path to every node in the lattice. The key idea is that the highest probability path to a particular spot (e.g., O above "in") is:

The highest probability path to some label, x, of the previous word
+
The probability of the edge from x to the label for this word

Reusing the example above, here are the two possibilities for this label. It could either come from LOC or O followed by an edge / transition:


Given this observation, we can identify the best possible label sequence in two passes:

Move left-to-right through the sentence, working out for each word what the probability of reaching each possible label is, and noting what the previous label was

For the last word, work out the highest probability label and the previous label

Go backwards through the sentence, step-by-step, by going to the previous label written down at each step.

If we visualise what the algorithm would compute for the example above, it would look something like this (where the blue arrows indicate for each label what the previous label was, and the blue box indicates the best label of the last word):


In more detail, the steps of the algorithm are:

Calculate probabilities for the possible labels for the first word, taking into account the transition from START.

For every other word:

Consider each possible label, L

Consider each possible previous label, M

Calculate the probability of L, if we had come from M

Record the best way to get to L (ie., which label M was the best) and what the probability of it is

Determine the highest probability label for the final word by taking into consideration the END transition.

Starting from the final word and its label, go back through the lattice one step at a time to get the best sequence

For another explanation, see 8.4.5 and 8.4.6 of Speech and Language Processing (Dan Jurafsky and James H. Martin)
"""

def viterbi(tokens, distributions, transitions, labels):
    scores = [{}]
    # Calculate initial
    for label, score in distributions[0].items():
        combined_score = score * transitions["START", label]
        source = "START"
        scores[0][label] = (combined_score, source)

    # Calculate all following tokens
    for distribution in distributions[1:]:
        scores.append({})
        for label, score in distribution.items():
            options = []
            for previous_label, (previous_score, _) in scores[-2].items():
                combined_score = previous_score * score * transitions[previous_label, label]
                options.append((combined_score, previous_label))
            options.sort(reverse=True)
            scores[-1][label] = options[0]

    # Calculate final
    end_options = []
    for previous_label, (previous_score, _) in scores[-1].items():
        combined_score = previous_score * transitions[previous_label, "END"]
        end_options.append((combined_score, previous_label))
    end_options.sort(reverse=True)

    # Extract sequence
    sequence = [end_options[0][1]]
    for i in range(len(scores) - 1, 0, -1):
        _, previous_label = scores[i][sequence[0]]
        sequence.insert(0, previous_label)

    return end_options[0][0], sequence
