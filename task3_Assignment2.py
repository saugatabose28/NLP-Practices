"""
Inference
In this question, you will implement a function to find the best label for a question given a model.

In other words, this is the function that makes a prediction / guesses the answer.

You should consider every possible label and identify the one with the highest score. If more than one have the same score then sort the labels using python's sort function (e.g., best_options.sort()) and take the first.

Program name - q2_inference.py

Function name - find_best_code

Arguments:

question, a string, the English question

model, a CodeModel, with the functions defined in the Model question, and the class member variable labels

Return value - A string, the highest scoring SQL query.

Example
See data.q2_inference.sample.txt for a sample input. The structure of the input is:

(
    {data for training},
    {the set of labels},
    An input question,
    The correct answer for the question,
    The number of training iterations our model will go through before running on the input question
)

The output in this case should be:

SELECT name FROM course ;
"""

def find_best_code(question, model):
    scores = []
    # Go through every possible label
    for label in model.labels:
        # Calculate the score the model gives for this label on this instance
        score = model.get_score(question, label)
        # Add it to the list of scores
        scores.append((score, label))
    # Sort the scores so that the best one is first
    scores.sort(reverse=True)
    # Break ties by sorting the labels
    top = [v[1] for v in scores if v[0] == scores[0][0]]
    top.sort()
    return top[0]