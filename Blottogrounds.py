# Blottogrounds
# INPUT:
# - a .csv file where each row is an 11-tuple where the first is the
# player's name as a string, and the remaining 10 entries are integers
# - a list of size 10 that encodes the distribution of points among the towers
# - a 'battle' function that determines the victory condition at the towers
# OUTPUT: a .csv file with a ranking of the players based on the number of
# games they've won, disqualifications, and a matrix that shows who beat who.

import csv
import copy
import importlib

# Importing a .py file that contains the point distribution and battle:
r_name = input("Name of rules file: ")
r = importlib.import_module('Rules.' + r_name)

subs_name = input("Name of submission file: ")
subs = []

# Input routine:
with open('Submissions/' + subs_name + '.csv') as csvfile:
    raw = csv.reader(csvfile, delimiter = ',')
    for row in raw:
        if not row[2].isnumeric():
            continue
        newsub = [row[1]]
        for i in range(2,12):
            newsub.append(int(row[i]))
        subs.append(newsub)

# Checking for infeasible submissions:
disquals = []
newsubs = []
for i in range(len(subs)):
    valid = True
    if sum(subs[i][1:]) != 100:
        valid = False
    else:
        for n in subs[i][1:]:
            if n < 0 or n > 100:
                valid = False
                break
    if valid:
        newsubs.append(subs[i])
    else:
        disquals.append(subs[i])

subs = newsubs
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
subs_unsorted = copy.deepcopy(subs)
subs.sort(key = lambda sub : sub[11], reverse = True)

ranks = []
for i in range(len(subs)):
    rank_count = 1
    if i == 0:
        ranks.append([rank_count,subs[i][0],subs[i][11]])
    elif subs[i][11] != subs[i-1][11]:
        rank_count = i+1
        ranks.append([rank_count,subs[i][0],subs[i][11]])
    elif subs[i][11] == subs[i-1][11]:
        ranks.append([rank_count,subs[i][0],subs[i][11]])

# Output routine:
with open('Results/results.csv', 'w', newline = '') as newcsv:
    mywriter = csv.writer(newcsv)
    mywriter.writerow(["Rules file:",r_name,"Submissions file:",subs_name])
    mywriter.writerow([])
    mywriter.writerow(["Ranking","Name","Wins"])
    for rank in ranks:
        mywriter.writerow(rank)
    if len(disquals) > 0:
        mywriter.writerow([])
        mywriter.writerow(["Disqualifications:"])
        for disqual in disquals:
            mywriter.writerow(disqual)
    mywriter.writerow([])
    mywriter.writerow(["Win matrix:"])
    names = []
    for rank in ranks:
        names.append(rank[1])
    names.sort()
    mywriter.writerow([""] + names)
    for i in range(len(names)):
        mywriter.writerow([names[i]] + win_matrix[i])

# Optional graph rendering:
render = input("Done! Would you like a graph? (YES?) ")
render = render.lower()
render = render.strip()
if render != 'yes':
    print("No graph produced.")
if render == 'yes':
    import networkx as nx
    import matplotlib.pyplot as plt
    G = nx.DiGraph()
    G.add_nodes_from(names)
    for i in range(len(subs)):
        for j in range(len(subs)):
            if win_matrix[i][j] > 0:
                G.add_edge(names[i],names[j])
    plt.figure(figsize=(8,8))
    nodesizes = [sub[11]*100 for sub in subs_unsorted]
    nx.draw(G, with_labels=True, connectionstyle='arc3, rad = 0.1',
            node_color='#73E4E8',
            node_size=nodesizes)
    plt.savefig('Results/results_graph.pdf')
    print("Graph produced and saved.")
