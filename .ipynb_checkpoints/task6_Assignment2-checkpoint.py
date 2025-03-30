"""
Evaluation Metrics
In this question, you will implement several metrics that can be calculated from a confusion matrix.

Program name - q5_metrics.py

Functions:

calculate_accuracy , this should calculate the accuracy, as a number between 0 and 1

calculate_precision , this should calculate the per-SQL query precision, as numbers between 0 and 1

calculate_recall , this should calculate the per-SQL query recall, as numbers between 0 and 1

calculate_macro_f1 , this should calculate macro F-scores, as a number between 0 and 1. Remember, to get macro F1 you calculate the F-score for each label separately, then take the mean of those F-scores.

For all metrics, if the equation gives 0/0, assign a score of 1.0.

Arguments (all functions have the same arguments):

confusion_matrix, a dictionary, the structure and contents are as defined in the Confusion Matrix question.

labels, a set of strings, all the possible labels

Return value:

calculate_accuracy and calculate_macro_f1 should return a single number, the score

calculate_precision and calculate_recall should return dictionaries, whether the key is an SQL query and the value is the precision and recall, respectively, for that SQL query.

Note, for this question we use this function to check values, allowing for slightly different results due to floating point error:

def compare_vals(ans, ref):
    if abs(ans - ref) < 1e-5:
        return True
    return False
Example
See data.q5_metrics.sample.txt for a sample input. The outputs in this case should be:

Accuracy: 0.5

Precision dict: {'SELECT name FROM course ;': 0.25, 'SELECT code FROM course ;': 0.6666666666666666}

Recall dict:  {'SELECT name FROM course ;': 0.3333333333333333, 'SELECT code FROM course ;': 0.5714285714285714}

F-score: 0.4505494505494505
"""

def calculate_accuracy(confusion_matrix, labels):
    total = 0
    match = 0
    for pair, count in confusion_matrix.items():
        total += count
        if pair[0] == pair[1]:
            match += count
    return match / total

def calculate_precision(confusion_matrix, labels):
    p_vals = {}
    for label in labels:
        tp, fp = 0, 0
        for other in labels:
            if other == label:
                tp += confusion_matrix.get((label, label), 0)
            else:
                fp += confusion_matrix.get((other, label), 0)
        if tp + fp == 0:
            p_vals[label] = 1.0
        else:
            p_vals[label] = tp / (tp+fp)
    return p_vals

def calculate_recall(confusion_matrix, labels):
    r_vals = {}
    for label in labels:
        tp, fn = 0, 0
        for other in labels:
            if other == label:
                tp += confusion_matrix.get((label, label), 0)
            else:
                fn += confusion_matrix.get((label, other), 0)
        if tp + fn == 0:
            r_vals[label] = 1.0
        else:
            r_vals[label] = tp / (tp+fn)
    return r_vals

def calculate_macro_f1(confusion_matrix, labels):
    p_vals = calculate_precision(confusion_matrix, labels)
    r_vals = calculate_recall(confusion_matrix, labels)
    f_vals = {}
    for label in labels:
        p = p_vals[label]
        r = r_vals[label]
        if p + r == 0:
            f_vals[label] = 1.0
        else:
            f_vals[label] = 2 * p * r / (p + r)
    total = sum(f for _, f in f_vals.items())
    return total / len(f_vals)