"""
Data
In this question, you will implement a function that reads and prepares the data.

The input is a json file containing a list. Each element in the list is one example. Each example has the fields:

data, a string, either train, dev, or test, to indicate how this example should be used

question, a string, an English question

sql, a string, the corresponding SQL query

Your function must produce a tuple containing two things:

A dictionary, with the keys train, dev, and test. Each key maps to a list containing tuples. Each tuple is one example, containing the question followed by the SQL query.

A set, containing all the observed SQL queries, including cases from train, dev, and test.

Note:

You do not need to tokenise the question or sql in this task. They can be kept as strings.

Program name - q0_data.py

Function name - read_data

Arguments:

filename , a string, the name of a file

Return value - a tuple, as described above.

Example
See data.q0_data.sample.json for a sample input. The output in this case should be:

(
    {
    'train': [
        ('What are all the courses ?', 'SELECT name FROM course ;'),
        ('What are all the course codes ?', 'SELECT code FROM course ;')],
    'dev': [
        ('What are all the courses ?', 'SELECT name FROM course ;')],
    'test': [
        ('Please give me the names of courses .', 'SELECT name FROM course ;')]
    },
    {'SELECT name FROM course ;', 'SELECT code FROM course ;'}
)
"""

import json

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