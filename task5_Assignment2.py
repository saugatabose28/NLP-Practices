"""
Confusion Matrix
In this question, you will implement a function to construct a confusion matrix summarising the output of the model on a list of examples.

You should run the model on each sample to get its prediction, then use that to record counts in the confusion matrix.

Program name - q4_confusion.py

Function name - get_confusion_matrix

Arguments:

eval_data, a list, each element is a tuple, containing two strings: the English question and the true SQL query

model, a CodeModel, with the functions defined in the Model question, and the class member variable labels

find_best_code, a function, the one defined the Inference question. Note that you can call this the same way you would if it was defined in your code (e.g., find_best_code(question, model)

Return value - A dictionary, where the keys are tuples (true answer, system guess) and the values are the count of cases for that pair. Note that you should include all possible pairs of labels, even those that have a value of zero.

Example
See data.q4_confusion.sample.txt for a sample input. The output in this case should be:

{
    ('SELECT name FROM course ;', 'SELECT name FROM course ;'): 3,
    ('SELECT name FROM course ;', 'SELECT code FROM course ;'): 0,
    ('SELECT code FROM course ;', 'SELECT name FROM course ;'): 0,
    ('SELECT code FROM course ;', 'SELECT code FROM course ;'): 1
}
"""

def get_confusion_matrix(eval_data, model, find_best_code):
    confusion_matrix = {}
    for label in model.labels:
        for olabel in model.labels:
            confusion_matrix[label, olabel] = 0
    for question, answer in eval_data:
        guess = find_best_code(question, model)
        confusion_matrix[answer, guess] = 1 + confusion_matrix.get((answer, guess), 0)
    return confusion_matrix