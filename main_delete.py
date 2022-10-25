#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.score import Score

fs = FileStorage()

# All States
all_scores = fs.all(Score)
print("All Score: {}".format(len(all_scores.keys())))
for score_key in all_scores.keys():
    print(all_scores[score_key])

# Delete the new State
fs.delete(Score)

# All States
all_scores = fs.all(Score)
print("All Score: {}".format(len(all_scores.keys())))
for score_key in all_scores.keys():
    print(all_scores[score_key])