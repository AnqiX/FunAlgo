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
            scc_dic[temp[0]].append(temp[1])

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
    #print('new order', newOrder)
    secondResult = DFS(scc_dic, newOrder)
    leaderArray = secondResult[1]

    rootDic = {}
    for node in leaderArray:
        root = leaderArray[node]
        if root in rootDic:
            rootDic[root].append(node)
        else:
            rootDic[root] = [node]
    #print(rootDic)

    lengthArray = []
    for component in rootDic:
        lengthArray.append(len(rootDic[component]))
        
    rawLength = sorted(lengthArray, key=int, reverse=True)[:5]
    for i in range (0, 5-len(rawLength)):
        rawLength.append(0)
    return rawLength       

def DFS(scc_dic, order):
    ###### forming the Grev ####
    revscc_dic = {}
    maxKey = 0
    for key in scc_dic:
        temps = scc_dic[key]
        if key > maxKey:
            maxKey = key
        for temp in temps:
            if temp not in revscc_dic:
                revscc_dic[temp] = [key]
            else:
                revscc_dic[temp].append(key)
    #print(order)
    #print('revscc_dic: ', revscc_dic)
    ##### iterative dfs (with finish times) ####
    path = []
    time = 0
    finish_time_dic = {}
    leader = {}
    for i in order:
        start = i
        q = [start]
        while q:
            v = q.pop(0)
            #print(v)
            if v not in path and v in revscc_dic:
                path.append(v)
                q = [v] + q
                #print(v, revscc_dic[v])
                for w in revscc_dic[v]:
                    if w not in path: q = [w] + q
            else:
                if v not in revscc_dic:
                    #print(v)
                    path.append(v)
                if v not in finish_time_dic:
                    #print('finish: ', v, 'root: ', path[len(path)-1])
                    leader[v] = path[len(path)-1]
                    finish_time_dic[v] = time
                    time += 1
                    
    return [finish_time_dic, leader]


print(kosaraju())
