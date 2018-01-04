import numpy as np
import matplotlib.pyplot as plt
import OpticsClusterArea as OP
from itertools import *
import AutomaticClustering as AutoC
import loadDataSet as ld


X = ld.loadDataSet('julei2.txt')
# Y = []
# for i in range(len(X)/2):
#    Y.append(X[2*i])
X = np.array(X)



#plot scatterplot of points

# fig = plt.figure()
# ax = fig.add_subplot(111)

# ax.plot(X[:,0], X[:,1], 'b.', ms=2)

# plt.savefig('Graph.png', dpi=None, facecolor='w', edgecolor='w',
#     orientation='portrait', papertype=None, format=None,
#     transparent=False, bbox_inches=None, pad_inches=0.1)
# plt.show()

RD = ld.loadDataSet2('RD60.txt')
order = ld.loadDataSet2('order60.txt')
RD = np.array(RD)
#run the OPTICS algorithm on the points, using a smoothing value (0 = no smoothing)
# [RD, CD, order] = OP.optics(X,20)
# RD = RD - min(RD[1:len(RD)])
RPlot = []
RPoints = []
        
for item in order:
    RPlot.append(RD[item-1]) #Reachability Plot
    RPoints.append([X[item-1][0],X[item-1][1]]) #points in their order determined by OPTICS

#hierarchically cluster the data
rootNode = AutoC.automaticCluster(RPlot, RPoints)

#print Tree (DFS)
AutoC.printTree(rootNode, 0)

#graph reachability plot and tree
#AutoC.graphTree(rootNode, RPlot)

#array of the TreeNode objects, position in the array is the TreeNode's level in the tree
array = AutoC.getArray(rootNode, 0, [0])

#get only the leaves of the tree
leaves = AutoC.getLeaves(rootNode, [])

#graph the points and the leaf clusters that have been found by OPTICS
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(X[:,0], X[:,1], 'y.')
colors = cycle('gmkrcbgrcmk')
for item, c in zip(leaves, colors):
    node = []
    for v in range(item.start,item.end):
        node.append(RPoints[v])
    node = np.array(node)
    ax.plot(node[:,0],node[:,1], c+'x', ms=5)

plt.savefig('Graph2.png', dpi=None, facecolor='w', edgecolor='w',
    orientation='portrait', papertype=None, format=None,
    transparent=False, bbox_inches=None, pad_inches=0.1)
plt.show()
