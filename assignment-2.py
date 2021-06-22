
# --------------------------------------
#  Assignment 2 : Brenda Cobena
# --------------------------------------
import networkx as nx
import matplotlib.pyplot as plt


# Importing graphs from a file
G = nx.read_graphml('graph.graphml')

# --------------------------------------
# Draw with custom node labels
# --------------------------------------
node_labels=nx.get_node_attributes(G,'label')


#Custom position
positions = {'1':[-1,0.5],'2':[0,1],'6':[1,1],'5':[2,1],'22':[0,-1],'3':[1,-1],'4':[2,-1]}  
colors = ['r','#1f78b4','orange','#1f78b4','#1f78b4','#1f78b4','#1f78b4']
nsize = [500, 1000, 400, 800, 200, 1000, 1000]
ecolor=['darkviolet','k','k','k','k','k']


nx.draw_networkx(G,        
                 positions,
                 node_size= nsize,
                 node_color= colors,
                 edge_color=ecolor,
                 labels=node_labels,
                 font_size=8
                )


plt.savefig('matplot_graph.png')

