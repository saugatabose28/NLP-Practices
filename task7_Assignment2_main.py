"""
Complete system
In this question, you will put all the components together with a training and evaluation loop. Your code should do the following:

Read the data

Create a model

Train the model by iterating over the training data. In each iteration, go through each example and run the learning function for it. At the end of each iteration, evaluate the model on the dev set.

Evaluate the model on the test set.

Return the dev scores and the final test score

Program name - q6_combined.py

Function name - main

Arguments:

filename , a string, the location of a file to read. It's contents are as described in the Data question

iterations, an integer, the number of iterations of training to do

read_data, a function, as defined in the Data question

model_maker, a class, as defined in the Model question (you can use this as follows: my_model = model_maker(labels, training_data)

learn, a function, as defined in the Learning question

find_best_code, a function, as defined in the Inference question

get_confusion_matrix, a function, as defined in the Confusion Matrix question

calculate_accuracy, a function, as defined in the Evaluation Metrics question

calculate_macro_f1, a function, as defined in the Evaluation Metrics question

Return value - a tuple, containing:

A list, each element is a dictionary with the keys accuracy and macro-f1, whose values are the respective scores. These are the scores on the dev set from each iteration of training.

A dictionary, with the keys accuracy and macro-f1, whose values are the respective scores on the test set.

Example
See data data.q6_combined.sample.json for a sample input. The output in this case should be:

(
    [{'accuracy': 1.0, 'macro-f1': 1.0}],
    {'accuracy': 0.5, 'macro-f1': 0.3333333333333333}
)
"""

#!/usr/bin/env python3

import json
import sys

## Data

def read_data(filename: str):
    labels = set()
    split_data = {
            'train': [],
            'dev': [],
            'test': []
    }
    with open(filename) as src:
        data = json.load(src)
        for example in data:
            question = example['question']
            sql = example['sql']
            labels.add(sql)
            split_data[example['data']].append((question, sql))
    return split_data, labels

## Model

class CodeModel:
    def __init__(self, labels, training_data):
        self.weights = {}
        self.labels = labels

        for question, _ in training_data:
            for label in labels:
                features = self.get_features(question, label)
                for feature in features:
                    if feature not in self.weights:
                        self.weights[feature] = 0

    def get_features(self, question, label):
        features = []
        for token in question.split():
            features.append((token, label))
        return features

    def get_score(self, question, label):
        score = 0
        for feature in self.get_features(question, label):
            score += self.weights.get(feature, 0)
        return score

    def update(self, question, label, change):
        for feature in self.get_features(question, label):
            self.weights[feature] += change

## Inference

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

## Learning

def learn(question, answer, model, find_best_code):
    # Get the model's guess for this question
    guess = find_best_code(question, model)
    
    if guess == answer:
        # We got it right, do nothing
        pass
    else:
        # Add 1 to features for the true answer
        model.update(question, answer, 1)
        # Subtract 1 from features for the guess
        model.update(question, guess, -1)

## Evaluation

def get_confusion_matrix(eval_data, model, find_best_code):
    confusion_matrix = {}
    for label in model.labels:
        for olabel in model.labels:
            confusion_matrix[label, olabel] = 0
    for question, answer in eval_data:
        guess = find_best_code(question, model)
        confusion_matrix[answer, guess] = 1 + confusion_matrix.get((answer, guess), 0)
    return confusion_matrix

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

def evaluate(eval_data, model, labels):
    confusion_matrix = get_confusion_matrix(eval_data, model, find_best_code)
    metrics = {
            'accuracy': calculate_accuracy(confusion_matrix, labels),
            'macro-f1': calculate_macro_f1(confusion_matrix, labels)
    }
    return metrics

## Combined

def print_scores(context, scores):
    parts = [context]
    for metric, score in scores.items():
        parts.append(metric)
        parts.append(str(score))
    print("\t".join(parts))

def main(filename, iterations, read_data, model_maker, learn, find_best_code, get_confusion_matrix, calculate_accuracy, calculate_macro_f1):
    data, labels = read_data(filename)
    model = CodeModel(labels, data['train'])

    dev_scores = []
    for iteration in range(iterations):
        for example in data['train']:
            learn(example[0], example[1], model, find_best_code)
        confusion_matrix = get_confusion_matrix(data['dev'], model, find_best_code)
        dev_score = {
                'accuracy': calculate_accuracy(confusion_matrix, labels),
                'macro-f1': calculate_macro_f1(confusion_matrix, labels)
        }
        dev_scores.append(dev_score)

    confusion_matrix = get_confusion_matrix(data['test'], model, find_best_code)
    test_score = {
            'accuracy': calculate_accuracy(confusion_matrix, labels),
            'macro-f1': calculate_macro_f1(confusion_matrix, labels)
    }
    return dev_scores, test_score