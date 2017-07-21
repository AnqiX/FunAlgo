import sys
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
    
sys.setrecursionlimit(4000000)
print('started')


with open("testCase.txt") as textFile:
    lines = [line.split() for line in textFile]

#lines = [line.split() for line in data]

def formatRaw(raw):
    #print(raw)
    result = {}
    for row in raw:
        if row != []:
            tail = int(row[0])
            head = int(row[1])
            if tail not in result:
                result[tail] = []
            result[tail].append(head)

    return result

def kosaraju(lines):
    graph = formatRaw(lines)
    global t, s, explored, leader, fArray
    t = 0
    s = None
    explored = {}
    leader = {}
    fArray = {}
    nodes = list(graph.keys())

    for i in range(len(nodes), 0, -1):
        if i not in explored:
            s = i
            DFS(graph, i)

    explored = {}
    newOrder = []
    for key in fArray:
        newOrder.append(fArray[key])

    #print(newOrder)
    
    for i in newOrder:
        if i not in explored:
            #print('start node: ', i)
            s = i
            DFS(graph, i)

    #print(leader)
    
    formattedLeader = {}
    for node in leader:
        root = leader[node]
        if root not in formattedLeader:
            formattedLeader[root] = [node]
        else:
            formattedLeader[root].append(node)
    #print(formattedLeader)
    lengthArray = []
    for component in formattedLeader:
        lengthArray.append(len(formattedLeader[component]))

    rawLength = sorted(lengthArray, key=int, reverse=True)[:5]
    for i in range (0, 5-len(rawLength)):
        rawLength.append(0)
    return rawLength

def DFS(graph, i):
    global explored, leader, t, s, fArray

    explored[i] = True 
    leader[i] = s
    #print('DFS input: ', i)
    if i in graph:
        
        neighbors = graph[i]

        #print(i, 'neigbors: ', neighbors)
        
        for j in neighbors:
            if j not in explored:
                DFS(graph, j)
    t += 1
    fArray[t] = i

print(kosaraju(lines))
