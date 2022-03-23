import graphviz as gv

#g1 = gv.Graph(format="svg")
g1 = gv.Graph(format="pdf")
g1.node('A')
g1.node('B')
g1.node('C')
g1.edge('A', 'B')
g1.edge('A', 'C')
g1.render('graph/demo59-grh')
#print(g1.source)

g2 = gv.Digraph(format="pdf")
g2.node('A')
g2.node('B')
g2.node('C')
g2.edge('A', 'B')
g2.edge('A', 'C')
g2.render('graph/demo59-dgrh')