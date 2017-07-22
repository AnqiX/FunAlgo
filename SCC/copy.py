import operator
    
def kosaraju():
    ###### reading the data #####
    with open('testCase.txt') as req_file:
            ori_data = []
            for line in req_file:
                line = line.split()
                if line:
                    line = [int(i) for i in line]
                    ori_data.append(line)      

    ######## finding the G#####
    scc_dic = {}
    for temp in ori_data:
        if temp[0] not in scc_dic:
            scc_dic[temp[0]] = [temp[1]]
        else:
            scc_dic[temp[0]] = [temp[1]] + scc_dic[temp[0]] 

    keyList = list(scc_dic.keys())
    for row in ori_data:
        if row[1] not in keyList:
            keyList.append(row[1])
    backwardOrder = sorted(keyList, key=int, reverse=True)

    firstResult = DFS(scc_dic, backwardOrder)
    finish_time_dic = firstResult[0]
    
    sortedFinishTimeDic = sorted(finish_time_dic.items(), key=operator.itemgetter(1))
    newOrder = []
    for row in sortedFinishTimeDic:
        newOrder.append(row[0])
    #print("new order: ", newOrder)
    secondResult = DFS(scc_dic, newOrder)
    leaderArray = secondResult[1]

    rootDic = {}
    for node in leaderArray:
        root = leaderArray[node]
        if root in rootDic:
            rootDic[root].append(node)
        else:
            rootDic[root] = [node]

    lengthArray = []
    for component in rootDic:
        lengthArray.append(len(rootDic[component]))
        
    rawLength = sorted(lengthArray, key=int, reverse=True)[:5]
    for i in range (0, 5-len(rawLength)):
        rawLength.append(0)
    #print(rootDic)
    return rawLength       

def DFS(scc_dic, order):
    ###### forming the Grev ####
    #print(scc_dic)
    revscc_dic = {}
    maxKey = 0

    ##### iterative dfs (with finish times) ####
    path = []
    time = 0
    finish_time_dic = {}
    leader = {}
    filledLevelCount = 0
    levelDic = {}
    levelDic[0] = 0
    root = [order[0]]
    pushRoot = False
    immediateParent = {}
    immediateParent[order[0]] = 0
    for i in order:
        start = i
        q = [start]
        while q:
            v = q.pop(0)
            if v not in path and v in scc_dic:
                path.append(v)
                if pushRoot:
                    root.append(v)
                    pushRoot = False
                levelDic[v] = len(scc_dic[v])
                q = [v] + q
                #print(v, scc_dic[v], root)
                for w in scc_dic[v]:
                    if w not in path:
                        q = [w] + q
                        immediateParent[w] = v
            else:
                if v not in scc_dic:
                    path.append(v)
                if v not in finish_time_dic:
                    #print(v, 'root: ', root[len(root)-1])
                    leader[v] = root[len(root)-1]
                    finish_time_dic[v] = time
                    time += 1
                    
                    if v in immediateParent:
                        #print('v: ', v, 'parent: ', immediateParent[v], ", compare: ", time, levelDic[immediateParent[v]], '####')
                        if time == levelDic[immediateParent[v]] or order.index(v) == 0:
                            pushRoot = True
                    else:
                        pushRoot = True

    #print('levelDic: ', levelDic)
    return [finish_time_dic, leader]


print(kosaraju())
