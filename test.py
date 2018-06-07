import sys
import re
import time

graphRE=re.compile("(\\d+)\\s(\\d+)")
edgeRE=re.compile("(\\d+)\\s(\\d+)\\s(-?\\d+)")

vertices=[]
edges=[]

def BellmanFord(G):
    pathPairs=[]
    # Fill in your Bellman-Ford algorithm here
    # The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]

#   // This implementation takes in a graph, represented as
#   // lists of vertices and edges, and fills two arrays
#   // (distance and predecessor) with shortest-path
#   // (less cost/distance/metric) information
#__________________________________________________________________________________


#   for each vertex v in vertices:
#       distance[v] := inf             // At the beginning , all vertices have a weight of infinity
#       predecessor[v] := null         // And a null predecessor
   
#   distance[source] := 0              // Except for the Source, where the Weight is zero 
   
#  #  // Step 2: relax edges repeatedly
#   for i from 1 to size(vertices)-1:
#       for each edge (u, v) with weight w in edges:
#           if distance[u] + w < distance[v]:
#               distance[v] := distance[u] + w
#               predecessor[v] := u

#   # // Step 3: check for negative-weight cycles
#   for each edge (u, v) with weight w in edges:
#       if distance[u] + w < distance[v]:
#           return false
#   return distance[], predecessor[]
#________________________________________________________________________________________
    
    #for each i and j we have outside for loop(edges)
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            distance = []
            for v in range(len(vertices)):
                distance.append(float("inf"))
            distance[i] = 0
            #step2
            for x in range(len(vertices)):
                for u in range(len(vertices)):
                    for v in range(len(vertices)):
                        if float(distance[u]) + float(edges[u][v]) < float(distance[v]):
                            distance[v] = float(distance[u]) + float(edges[u][v])
                        
    
            pathPairs.append(( (i,j), float(distance[j])))
    print (pathPairs)
    return pathPairs

def FloydWarshall(G):
    pathPairs=[]
    # Fill in your Floyd-Warshall algorithm here
    # # The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]
    # let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
    # distance 
    #dist = []
    for v in range(len(vertices)):
        edges[v][v] = 0
    for k in range(len(vertices)):
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if float(edges[i][k]) == float("inf") or float(edges[j][k]) == float("inf"):
                    continue
                if float(edges[i][j]) > float(edges[i][k]) + float(edges[k][j]): 
                    edges[i][j] = float(edges[i][k]) + float(edges[k][j])
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            pathPairs.append(((i,j), edges[i][j]))     
            
    print(pathPairs)
    return pathPairs

def readFile(filename):
    global vertices
    global edges
    # File format:
    # <# vertices> <# edges>
    # <s> <t> <weight>
    # ...
    inFile=open(filename,'r')
    line1=inFile.readline()
    graphMatch=graphRE.match(line1)
    if not graphMatch:
        print(line1+" not properly formatted")
        quit(1)
    vertices=list(range(int(graphMatch.group(1))))
    edges=[]
    for i in range(len(vertices)):
        row=[]
        for j in range(len(vertices)):
            row.append(float("inf"))
        edges.append(row)
    for line in inFile.readlines():
        line = line.strip()
        edgeMatch=edgeRE.match(line)
        if edgeMatch:
            source=edgeMatch.group(1)
            sink=edgeMatch.group(2)
            if int(source) > len(vertices) or int(sink) > len(vertices):
                print("Attempting to insert an edge between "+source+" and "+sink+" in a graph with "+vertices+" vertices")
                quit(1)
            weight=edgeMatch.group(3)
            edges[int(source)][int(sink)]=weight
    #Debugging
    #for i in G:
        #print(i)
    return (vertices,edges)

def main(filename,algorithm):
    algorithm=algorithm[1:]
    G=readFile(filename)
    # G is a tuple containing a list of the vertices, and a list of the edges
    # in the format ((source,sink),weight)
    if algorithm == 'b' or algorithm == 'B':
        BellmanFord(G)
    if algorithm == 'f' or algorithm == 'F':
        FloydWarshall(G)
    if algorithm == "both":
        start=time.clock()
        BellmanFord(G)
        end=time.clock()
        BFTime=end-start
        start=time.clock()
        FloydWarshall(G)
        end=time.clock()
        FWTime=end-start
        print("Bellman-Ford timing: "+str(BFTime))
        print("Floyd-Warshall timing: "+str(FWTime))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    main(sys.argv[2],sys.argv[1])
