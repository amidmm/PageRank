This is a simple implementation of the PageRank algorithm and it is ought to
be used for educational purposes not in commercial softwares.

Usage Example :

    Graph.v = [1,2,3]
    Graph.e = {1:[2,3],2:[1],3:[]}
    PageRank(Graph, None)  #landa is given a random number and initial value is 1
    #or
    PageRank(Graph,0.15,100)