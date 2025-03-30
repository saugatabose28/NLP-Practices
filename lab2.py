"""
Lab 2 Instructions
If you haven't already, please install scikit-learn: https://scikit-learn.org/stable/install.html

scikit-learn Working With Text Data Tutorial [1 pt]
To start, work through this tutorial from the widely used package scikit-learn, stopping at the exercises:

https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html

Note - do all the steps including the grid search at the end.

To show the teaching staff you are done, show them the output of running the code, which should include the metrics from the SVM and the performance after the grid search:

                        precision    recall  f1-score   support

           alt.atheism       0.95      0.80      0.87       319
         comp.graphics       0.87      0.98      0.92       389
               sci.med       0.94      0.89      0.91       396
soc.religion.christian       0.90      0.95      0.93       398

              accuracy                           0.91      1502
             macro avg       0.91      0.91      0.91      1502
          weighted avg       0.91      0.91      0.91      1502

0.917500000000000

Identifying Deception in Diplomacy [1 pt]
In this section, you will use scikit-learn to identify deception in the board game Diplomacy.

First, download the dataset:

https://github.com/DenisPeskoff/2020_acl_diplomacy

If you are curious about where this comes from, see the research paper: https://aclanthology.org/2020.acl-main.353/

The data contains JSON lines like this:

{
    "messages": [
        "Germany!\n\nJust the person I want to speak with. I have a somewhat crazy idea that I\u2019ve always wanted to try with I/G, but I\u2019ve never actually convinced the other guy to try it. And, what\u2019s worse, it might make you suspicious of me. \n\nSo...do I suggest it?\n\nI\u2019m thinking that this is a low stakes game, not a tournament or anything, and an interesting and unusual move set might make it more fun? That\u2019s my hope anyway.\n\nWhat is your appetite like for unusual and crazy?",
        "You've whet my appetite, Italy. What's the suggestion?",
        "\ud83d\udc4d",
        "It seems like there are a lot of ways that could go wrong...I don't see why France would see you approaching/taking Munich--while I do nothing about it--and not immediately feel skittish",
        "Yeah, I can\u2019t say I\u2019ve tried it and it works, cause I\u2019ve never tried it or seen it. But how I think it would work is (a) my Spring move looks like an attack on Austria, so it would not be surprising if you did not cover Munich. Then (b) you build two armies, which looks like we\u2019re really at war and you\u2019re going to eject me. Then we launch the attack in Spring. So there is really no part of this that would raise alarm bells with France.\n\nAll that said, I\u2019ve literally never done it before, and it does involve risk for you, so I\u2019m not offended or concerned if it\u2019s just not for you. I\u2019m happy to play more conventionally too. Up to you.",
        "I am just sensing that you don\u2019t like this idea, so shall we talk about something else? That was just a crazy idea I\u2019ve always wanted to try. I\u2019m happy to play more conservatively.",
        "Any thoughts?",
        "Sorry Italy I've been away doing, um, German things. Brewing Lagers?",
        "I don't think I'm ready to go for that idea, however I'd be down for some good ol'-fashioned Austria-kicking?",
        "I am pretty conflicted about whether to guess that you were telling the truth or lying about the \u201cbrewing lagers\u201d thing. I am going to take it literally and say \ud83d\udc4e even though I don\u2019t think you meant it deceptively. \ud83d\ude09"
    ],
    "sender_labels": [ true, true, true, true, true, true, true, true, true, true ],
    
    # The rest of these fields are not needed in this task, they are included here so you are aware of them    
    "receiver_labels": [ true, true, true, true, "NOANNOTATION", "NOANNOTATION", "NOANNOTATION", true, false, true ],
    "speakers": [ "italy", "germany", "italy", "germany", "italy", "italy", "italy", "germany", "germany", "italy" ],
    "receivers": [ "germany", "italy", "germany", "italy", "germany", "germany", "germany", "italy", "italy", "germany" ],
    "absolute_message_index": [ 74, 76, 86, 87, 89, 92, 97, 117, 119, 121, ],
    "relative_message_index": [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ],
    "seasons": [ "Spring", "Spring", "Spring", "Spring", "Spring", "Spring", "Spring", "Spring", "Spring", "Spring", ],
    "years": [ "1901", "1901", "1901", "1901", "1901", "1901", "1901", "1901", "1901", "1901" ],
    "game_score": [ "3", "3", "3", "3", "3", "3", "3", "3", "3", "3" ],
    "game_score_delta": [ "0", "0", "0", "0", "0", "0", "0", "0", "0", "0" ],
    "players": [ "italy", "germany" ],
    "game_id": 1
}

For us, the crucial thing to know about is:

messages , the text being sent back and forth between players

sender_labels , this indicates whether the message is truthful (true) or not (false)

Implement a Logistic Regression classifier that predicts if a message is truthful. The reason we are using logistic regression is that it is widely used and a great baseline for many NLP classification tasks. You should use the following configuration:

Solver: saga

Penalty: None

All other parameters as defaults

The steps you will need to implement are:

Data Loading: Start by loading your training, development, and test datasets to prepare the features (messages) and labels (sender_labels).

Data Preprocessing: Convert the text messages into a suitable format for modelling, using the same approach as in the tutorial above.

Model Definition: Use scikit-learn's LogisticRegression class to create the model, with the solver set to 'saga' and penalty set to 'None'.

Model Training: Train your model using the training data.

Model Evaluation: Assess the model's performance on the development dataset.

A few notes that may be helpful:

In the tutorial above, twenty_train.data is a list of strings. You can create something comparable yourself for the diplomacy data

In the tutorial above, twenty_train.target is a Numpy array. You can create a regular Python list and then convert it into an array with numpy.array(my_list)

You should get results that look something like this (where 0 indicates a lie and 1 indicates the truth):

              precision    recall  f1-score   support

           0       0.15      0.07      0.10       240
           1       0.92      0.96      0.94      2501

    accuracy                           0.88      2741
   macro avg       0.53      0.52      0.52      2741
weighted avg       0.85      0.88      0.86      2741

The number we care about here is the f1-score for 0, ie., how well are we doing at identifying lies? This simple model scores 0.10, which is not very good - it's hard!

Extension: Can you do better? [0 pt]
We only used the text above. Can you add other properties of the data to try to improve performance?

To avoid over-fitting, experiment on the development / validation data, then when you think you have a good approach, evaluate on the test data.
"""
import json
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn import metrics

def readfile(filename):
    examples_msg = []
    examples_label = []
    for line in open(filename):
        data = json.loads(line.strip())
        for msg, tlabel in zip(data['messages'], data['sender_labels']):
            if tlabel:
                examples_msg.append(msg)
                examples_label.append(1)
            else:
                examples_msg.append(msg)
                examples_label.append(0)
    return examples_msg, np.array(examples_label)

train = readfile("train.jsonl")
test = readfile("test.jsonl")
valid = readfile("validation.jsonl")


text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', LogisticRegression(penalty=None, solver='saga', max_iter=1000)),
])
text_clf.fit(train[0], train[1])

predicted = text_clf.predict(test[0])
np.mean(predicted == test[1])

print(metrics.classification_report(test[1], predicted))
metrics.confusion_matrix(test[1], predicted)
