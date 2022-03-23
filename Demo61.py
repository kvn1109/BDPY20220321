import graphviz as gv
import functools
import itertools

graph = functools.partial(gv.Graph, format='png')
digraph = functools.partial(gv.Digraph, format='png')
g1 = graph()
g2 = digraph()


def add_nodes(g, nodes):
    for n in nodes:
        if isinstance(n, tuple):
            g.node(n[0], **n[1])
        else:
            g.node(n)
    return g


def add_edges(g, edges):
    for e in edges:
        if isinstance(e[0], tuple):
            g.edge(*e[0], **e[1])
        else:
            g.edge(*e)
    return g


teams = ['US', 'UK', 'DE', 'FR']
races = tuple(itertools.combinations(teams, 2))
g1 = add_nodes(g1, teams)
g1 = add_edges(g1, races)
print(type(g1), type(g2))
g1.render("graph/demo61_g")

node1 = ('A', {'label': "United State"})
node2 = ('B', {'label': "United Kindom"})
node3 = ("C", {'label': "German"})
node4 = ('D', {'label': "France"})
g2_nodes = [node1, node2, node3, node4]
e1 = (('A', 'B'), {'label': 'comes from'})
e2 = (('A', 'C'), {'label': 'vehicle maker'})
e3 = (('B', 'C'), {'label': 'TGV'})
e4 = (('B', 'D'), {})
g2_edges = [e1, e2, e3, e4]
g2 = add_nodes(g2, g2_nodes)
g2 = add_edges(g2, g2_edges)

g2.render("graph/demo61_dg")

def apply_style(g, styles):
    g.graph_attr.update(('graph' in styles and styles['graph']) or {})
    g.node_attr.update(('nodes' in styles and styles['nodes']) or {})
    g.edge_attr.update(('edges' in styles and styles['edges']) or {})
    return g


styles = {'graph': {'label': 'some countries',
                    'fontsize': '24',
                    'fontcolor': '#448800',
                    'bgcolor': '#C0FFEE',
                    'rankdir': 'RL',  # TB, BT, LR, RL
                    'fontname': 'Courier'},
          'nodes': {'fontname': 'Courier',
                    'shape': 'rectangle',
                    'fontcolor': 'green',
                    'style': 'filled',
                    'fillcolor': '#004499'},
          'edges': {'style': 'dotted',
                    'color': '#882200',
                    'arrowhead':'open',
                    'fontname':'Consolas',
                    'fontsize':'24',
                    'fontcolor':'#FF0000'}}

g3 = apply_style(g2, styles)
g3.render('graph/demo61_dg_style')