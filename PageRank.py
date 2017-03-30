from random import random


def evaluate(Graph, landa):
    if landa is None:
        landa = random()
    assert len(Graph.v) >= 1, "Graph should be None Empty"
    for e in Graph.e.keys():
        assert e in Graph.v, "Edge points to a none existing vertex"
    return landa


def FindInVertex(Graph, target, loop1Rank):
    result = 0
    for i in range(len(Graph.v)):
        if Graph.v[target] in Graph.e[Graph.v[i]] and target != i:
            result += loop1Rank[i] / (len(Graph.e[Graph.v[i]]) + 1)
    return result + loop1Rank[target] / (len(Graph.e[Graph.v[target]]) + 1)


def PageRank(Graph, landa, initValue=1):
    """
    PageRank calculates the PageRank of a given Graph
    :param Graph: Object of Graph class with two member v and e. The v is the list of vertices and
    The e is dictionary of edges in this format: 'v1
    :[v2,...,]'
    :param landa: A number between 0 to 1 indicating the chance of choosing a vertex
    :param initValue: Initial value given to all the vertices
    :return: List of ranks for each edge
    """
    landa = evaluate(Graph, landa)
    loop1Ranks = []
    loop2Ranks = []
    nodeCount = len(Graph.v)
    tail = (1 - landa) / nodeCount
    for i in range(nodeCount):
        loop1Ranks.append(initValue / nodeCount)
    for i in range(nodeCount):
        loop2Ranks.append(tail + landa * FindInVertex(Graph, i, loop1Ranks))
    print(loop2Ranks)
