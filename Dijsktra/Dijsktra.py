import re

def formatRawData(fname):
	result = {}
	with open(fname) as f:
		content = f.readlines()
	for x in content:
		row = re.split(r'\t+', x.strip())
		if row != ['']:
			#print(row)
			key = int(row[0])
			result[key] = []
			for i in range(1, len(row)):
				connection = row[i].split(',')
				desired_array = [int(numeric_string) for numeric_string in connection]
				result[key].append(desired_array)
	
	return result


def Dijsktra():
	graph = formatRawData('testCases.txt')
	print(graph)
	resultList = {}
	infinity = 1000000
	chekcedList = []
	uncheckedList = {}

	for key in graph:
		resultList[key] = infinity
		uncheckedList[key] = infinity

	resultList[1] = 0
	
	while len(chekcedList) != len(resultList):
		u = min(uncheckedList)
		uncheckedList.pop(u, None)
		chekcedList.append(u)

		u_distance_value = resultList[u]
		print(u_distance_value)
		for row in graph[u]:
			#print('row: ',row)
			v = row[0]
			uv_weight = row[1]
			v_distance_value = resultList[v]
			uv_sum = u_distance_value + uv_weight
			#print(uv_sum, "compare with ", v_distance_value)
			if uv_sum < v_distance_value and u_distance_value != infinity:
				resultList[v] = uv_sum
				if v in uncheckedList:
					uncheckedList[v] = uv_sum
				#print('result list v: ', resultList[v])

	return resultList

	



result = Dijsktra()
print(result)
#print(result[7], result[37], result[59], result[82], result[99], result[115], result[133], result[165], result[188], result[197])