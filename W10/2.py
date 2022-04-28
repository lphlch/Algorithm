def findTree(treeSetList,vertex):
    for i in range(len(treeSetList)):
        if vertex in treeSetList[i]:
            return i
    return -1

def kruskal(edges):
    # let every vertex be a single tree
    vertexSet=set()
    for edge in edges:
        vertexSet.add(edge[0])
        vertexSet.add(edge[1])
    treeSetList=[]
    for vertex in vertexSet:
        treeSetList.append(set([vertex]))
    # sort edges by weight
    edges.sort(key=lambda x:int(x[2]))
    w=0
    for edge in edges:
        tree1Index=findTree(treeSetList,edge[0])
        tree2Index=findTree(treeSetList,edge[1])
        if tree1Index!=tree2Index:          # check if both vertices are in the tree
            w+=int(edge[2])                 # add weight
            treeSetList[tree1Index].update(treeSetList[tree2Index]) # merge two trees
            treeSetList.pop(tree2Index)     # remove tree2
            
    return w
            
n=int(input())
edges=[]
for i in range(n):
    edge=tuple(input().split(','))
    edges.append(edge)

print(kruskal(edges))