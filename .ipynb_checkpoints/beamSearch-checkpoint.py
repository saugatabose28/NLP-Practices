"""
Beam Search
In this question, use beam search to identify a label sequence. Since beam search is approximate, it may not be the highest probability sequence.

As a reminder, beam search works by labelling the sequence word by word, keeping track of a small number (K) of complete label sequences. At each step, we consider all possible ways to extend the current sequences one step. Then we keep the top K of those options.

This is an efficient method, but is not guaranteed to get the optimal solution.

For example, in the three word sequence Sydney is cool and labels LOC and O if the beam size is two, then you would:

Calculate probabilities for the two options on the first token (Sydney), taking into consideration the initial transition from START to a label.

Consider all possible ways of extending those initial sequences to also cover is.

Keep the top two sequences.

Consider all possible ways of extending to cover cool.

Keep the top two sequences.

Update the probabilities to consider the transition to END.

Return the highest probability option and it's probability.
"""

def beam(tokens, distributions, transitions, labels, k):
    beam = [(1.0, ["START"])]
    # Calculate all following tokens
    for distribution in distributions:
        nbeam = []
        for option in beam:
            for label, score in distribution.items():
                score *= option[0]
                score *= transitions[option[1][-1], label]
                nbeam.append((score, option[1][:] + [label]))
        nbeam.sort(reverse=True)
        beam = nbeam[:k]

    # Calculate final
    nbeam = []
    for option in beam:
        score = option[0]
        score *= transitions[option[1][-1], "END"]
        nbeam.append((score, option[1][1:]))
    nbeam.sort(reverse=True)
    beam = nbeam[:k]

    return beam[0]