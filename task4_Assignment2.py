"""
Learning
In this question, you will implement a function that makes an update to a model based on its performance on a sample.

Implement perceptron update, ie., if the answer is right, do nothing, if it is wrong, (a) add one to weights for the features with the correct query label, and (b) subtract one from the weights for the features with the incorrect query label.

Program name - q3_learning.py

Function name - learn

Arguments:

question, a string, an English question

answer, a string, the correct SQL query for this question

model, a CodeModel, with the functions defined in the Model question, and the class member variable labels

find_best_code, a function, the one defined the Inference question. Note that you can call this the same way you would if it was defined in your code (e.g., find_best_code(question, model)

Return value - No return value. We will check your work by inspecting the model.

Example
It is hard to provide an example input / output pair in this case. We have provided some sample data that you can use to test yourself.

Note: This example was updated at 4pm on March 7th to fix a bug.
"""
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