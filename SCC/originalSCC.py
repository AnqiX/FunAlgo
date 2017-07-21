###### reading the data #####
with open('smallArray.txt') as req_file:
        ori_data = []
        for line in req_file:
            line = line.split()
            if line:
                line = [int(i) for i in line]
                ori_data.append(line)

###### forming the Grev ####
revscc_dic = {}
for temp in ori_data:
    if temp[1] not in revscc_dic:
        revscc_dic[temp[1]] = [temp[0]]
    else:
        revscc_dic[temp[1]].append(temp[0])        

######## finding the G#####
scc_dic = {}
for temp in ori_data:
    if temp[0] not in scc_dic:
        scc_dic[temp[0]] = [temp[1]]
    else:
        scc_dic[temp[0]].append(temp[1])

##### iterative dfs (with finish times) ####
path = []
time = 0
finish_time_dic = {}
for i in range(max(max(ori_data)),0,-1):
    start = i
    q = [start]
    while q:
        v = q.pop(0)
        if v not in path and v in revscc_dic:
            path.append(v)
            q = [v] + q
            for w in revscc_dic[v]:
                if w not in path: q = [w] + q
        else:
            if v not in finish_time_dic:
                finish_time_dic[v] = time
                time += 1
print(path)  
print(finish_time_dic)
