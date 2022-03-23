import itertools

import graphviz as gv
from itertools import combinations,permutations

# g1 = gv.Graph(format="svg")
teams = ['US', 'UK', 'DE', 'FR', 'TW', 'CH']
# g1 = gv.Graph(format="png")
# g1 = gv.Graph(format="pdf")
g1 = gv.Digraph(format="png")
for t in teams:
    g1.node(t)

#for t1, t2 in combinations(teams, 2):
for t1, t2 in permutations(teams, 2):
    g1.edge(t1, t2)

g1.edge('TW','TW')
g1.render('graph/demo60')

g2 = gv.Graph(format="png")
for tt in teams:
    g2.node(tt)
for tt1, tt2 in combinations(teams, 2):
    g2.edge(tt1, tt2)

g2.edge('TW','TW')
g2.render('graph/demo60-1')