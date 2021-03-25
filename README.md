# blottoground
A repository for developing and organising Blottoground - a script for playing submitted strategies to Blotto games via a .csv file.

All rules (.py), submissions (.csv) and results (.csv) files go into their respective folders.

Blottoground should function as follows:

Execute Blottoground.py from console.

Prompt: "Name of rules file: "
User enters: "rules_classic"

This should lead to the importing of rules_classic.py in Blottoground.py from the folder called "Rules", since the former script contains the point distribution as well as the rule for determining the victory condition at the towers.

Prompt: "Name of submissions file: "
User enters: "submissions_week1"

This should lead to Blottoground reading in submissions_week1.csv from folder called "Submissions".

Blottoground will then proceed to play all participants in the .csv file against one another.

Blottoground will output results.csv into the folder called "Results". The .csv file will contain, in order, a ranking of the players along with their number of wins, a list of disqualified players and their strategies, and a matrix that represents who won between the players corresponding to the rows and columns. Rows and columns should have names of the players.
