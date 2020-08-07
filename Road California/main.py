import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
#data = pd.read_csv("corona.csv") 
# Preview the first 5 lines of the loaded data 
#data.head()
import networkx as nx
import matplotlib.pyplot as plt


g=nx.read_edgelist('roadNet-CA.txt',create_using=nx.Graph(),nodetype=int)

print(nx.info(g))

sp=nx.spring_layout(g)

plt.axes('off')

nx.draw_networkx(g,pos=sp,with_labels=False,node_size=35)

plt.show()