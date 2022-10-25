#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.score import Score

"""
 Objects creations
"""
score_1 = Score(name="Cincuenta")
print("New score: {}".format(score_1))
score_1.save()
score_2 = Score(name="diesciseis")
print("New score: {}".format(score_2))
score_2.save()
