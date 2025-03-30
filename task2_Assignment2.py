"""
Model
In this question, you will implement a linear model.

Features - The model should use a bag of words representation. To convert a question into words run .split() on it. Do not make other changes (e.g., do not change to lowercase).

For example, given the question: "Tell me the names of all the classes" and the SQL "SELECT name FROM course", you would generate the following features:

("Tell", "SELECT name FROM course")
("me", "SELECT name FROM course")
("the", "SELECT name FROM course")
("names", "SELECT name FROM course")
("of", "SELECT name FROM course")
("all", "SELECT name FROM course")
("the", "SELECT name FROM course")
("classes", "SELECT name FROM course")

Note, the word the appears twice in the sentence, so it appears twice in our list of features.

Weights - Since this is a multi-class labelling task, you should have a weight for each (feature, label) pair. Initialise weights for every feature for every training example to 0 (note that this setting to zero is not standard practise, but it means we can avoid randomness, which makes marking clearer). Only create weights for the training data.

Program name - q1_model.py

Class name - CodeModel

Function __init__ , this should prepare the class. It should save the labels in self.labels and initialise all the weights to 0.

labels , a set of strings, each string is one SQL query

training_data, a list, each item is a tuple containing a question and an SQL query

Function get_features, this should return a list of features for a given (question, SQL query) pair.

question, a string, an English question

label, a string, an SQL query

Function get_score, this should return the model's score for a (question, SQL query) pair. If the (question, label) pair produces features that were unseen in training then ignore them (or add zero, which is equivalent).

question, a string, an English question

label, a string, an SQL query

Function update, this should modify the model, changing all weights for features for the (question, SQL query) pair by the amount indicated.

question, a string, an English question

label, a string, an SQL query

change, an integer, how much to change the weights

Example
It is hard to provide an example input / output pair in this case. We have provided some sample data that you can use to test yourself. The structure of the sample file is:

 (
    {train, dev, and test data},
    {the set of all labels},
    An input question,
    The correct answer for the question,
    The number of training iterations the model will go through before running on the input question
)
"""

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
        answer = []
        for token in question.split():
            answer.append((token, label))
        return answer

    def get_score(self, question, label):
        score = 0
        for feature in self.get_features(question, label):
            score += self.weights.get(feature, 0)
        return score

    def update(self, question, label, change):
        for feature in self.get_features(question, label):
            self.weights[feature] += change