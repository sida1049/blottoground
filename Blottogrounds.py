# Blottogrounds
# INPUT:
# - a .csv file where each row is an 11-tuple where the first is the
# player's name as a string, and the remaining 10 entries are integers
# - a list of size 10 that encodes the distribution of points among the towers
# - a 'battle' function that determines the victory condition at the towers
# OUTPUT: a .csv file with a ranking of the players based on the number of
# games they've won, disqualifications, and a matrix that shows who beat who.

import csv
import importlib

# Importing a .py file that contains the point distribution and battle:
r_name = input("Name of rules file: ")
r = importlib.import_module(r_name)

subs_name = input("Name of submission file: ")
subs = []

# TO-DO: read .csv file and make subs into a list where each entry is a list of
# length 11, where the first entry is name and the rest are allocations.
# IMPORTANT: pass all allocations through the int() function so the numbers in
# subs are integers only.

# Checking for infeasible submissions:
disquals = []
for i in range(len(subs)):
    invalid = False
    if sum(subs[i][1:]) != 100:
        invalid = True
    else:
        for n in subs[i][1:]:
            if n < 0 or n > 100:
                invalid = True
                break
    if invalid:
        disquals.append(subs.pop(i))

subs.sort() # lexicographical sorting

# In the following win matrix, encode 0 for loss OR tie and 1 for win.
# E.g. win_matrix[i][j] == 1 means "i beats j"
win_matrix = [[0 for i in subs] for j in subs]

for i in range(len(subs)):
    for j in range(i+1,len(subs)):
        i_score = 0
        j_score = 0
        for k in range(10):
            outcome = r.battle(subs[i][k],subs[j][k])
            if outcome == 1: # i wins
                i_score = i_score + r.points[k]
            elif outcome == 2: # j wins
                j_score = j_score + r.points[k]
        if i_score > j_score:
            win_matrix[i][j] = 1
        elif i_score < j_score:
            win_matrix[j][i] = 1

# Counting wins:

for i in range(len(subs)):
    subs[i].append(sum(win_matrix[i]))

# Sort subs according to descending win count (12th entry):
subs.sort(key = lambda sub : sub[11], reverse = True)

ranks = []
for i in len(subs):
    ranks.append([subs[i][0],subs[i][11]])

#TO-DO: output ranks, disquals and win_matrix a .csv file that is human-readable
