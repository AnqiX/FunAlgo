import operator

 
def kosaraju():
    print('function begin')
    
    ###### reading the data #####
    with open('testCase.txt') as req_file:
            ori_data = []
            for line in req_file:
                line = line.split()
                if line:
                    line = [int(i) for i in line]
                    ori_data.append(line)      
    print('read complete')
    
    ######## finding the G#####
    print('scc_dic calculation begin')
    scc_dic = {}
    for temp in ori_data:
        if temp[0] not in scc_dic:
            scc_dic[temp[0]] = [temp[1]]
        else:
            scc_dic[temp[0]] = [temp[1]] + scc_dic[temp[0]]
            
    print('order calculation begin')
    keyList = list(scc_dic.keys())
    
    print('reversing order 1 begin')
    backwardOrder = sorted(keyList, key=int, reverse=True)

    print('first DFS begin')
    firstResult = DFS(scc_dic, backwardOrder)
    print('first DFS finish')

    print('new order calculation begin')
    finish_time_dic = firstResult[0]
    sortedFinishTimeDic = sorted(finish_time_dic.items(), key=operator.itemgetter(1))
    newOrder = []
    for row in sortedFinishTimeDic:
        newOrder.append(row[0])

    print('second DFS begin')
    secondResult = DFS(scc_dic, newOrder)
    print('second DFS finish')

    print('calculate leader array begin')
    leaderArray = secondResult[1]
    rootDic = {}
    for node in leaderArray:
        root = leaderArray[node]
        if root in rootDic:
            rootDic[root].append(node)
        else:
            rootDic[root] = [node]

    print('length array calculation begin')
    lengthArray = []
    for component in rootDic:
        lengthArray.append(len(rootDic[component]))

    print('five largest root calculation begin')
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
    path = {}
    time = 0
    finish_time_dic = {}
    leader = {}
    levelDic = {}
    levelDic[0] = 0
    root = order[0]
    pushRoot = False
    immediateParent = {}
    immediateParent[order[0]] = 0
    print('for loop starts')
    for i in order:
        start = i
        q = [start]
        print(i)
        while q:

            v = q.pop(0)
            if v not in path and v in scc_dic:
                path[v] = True
                if pushRoot:
                    print('root: ', v)
                    root = v
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
                    path[v] = True
                if v not in finish_time_dic:
                    #print(v, 'root: ', root[len(root)-1])
                    leader[v] = root
                    finish_time_dic[v] = time
                    time += 1
                    
                    if v in immediateParent:
                        #print('v: ', v, 'parent: ', immediateParent[v], ", compare: ", time, levelDic[immediateParent[v]], '####')
                        if time == levelDic[immediateParent[v]] or order[0] == v:
                            pushRoot = True
                    else:
                        pushRoot = True

    #print('levelDic: ', levelDic)
    return [finish_time_dic, leader]


print(kosaraju())
