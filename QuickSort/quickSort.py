import math
import statistics

with open('quickSortData.txt') as f:
    #h = [int(x) for x in next(f).split()]
    A = [int(x) for x in f]

callCount = 0
    
def quickSort(A):
    global callCount
    
    n = len(A)
    if n <= 1:
        return A

    (p1, p2, p) = partition(A)
    callCount += len(p1)
    callCount += len(p2)
    (p1Sorted) = quickSort(p1)
    (p2Sorted) = quickSort(p2)
    return p1Sorted + p + p2Sorted

def partition(A):

    """ last element as pivot
    A0 = A[0]
    Ar = A[len(A)-1]
    A[len(A)-1] = A0
    A[0] = Ar
    """


    A0 = A[0]
    Ar = A[len(A) - 1]
    midIndex = findMiddle(A)
    Am = A[midIndex]
    #print('output: ', midIndex, Am)
    dic = {A0: 0, Ar: len(A) - 1, Am: midIndex}
    medianA = statistics.median([A0, Ar, Am])
    A[dic[medianA]] = A0
    A[0] = medianA


    p = A[0]
    #print('input: ', A)
    #print('pivot: ', p)

    
    r = len(A)
    l = 0
    i = l + 1
    for j in range(l+1, r):
        if A[j] < p:
            Ai = A[i]
            Aj = A[j]
            A[i] = Aj
            A[j] = Ai           
            i += 1
    Al = A[l]
    A[l] = A[i-1]
    A[i-1] = Al

    #print('output: ', A[:(i-1)], A[(i):], p)
    return A[:(i-1)], A[(i):], [p]

def findMiddle(input_list):
    #print('input: ', input_list)
    middle = len(input_list)/2
    #print('middle: ', repr(middle))
    if middle % 1 != 0:
        return int(middle - .5)
    else:
        return int(middle -1)

B = [2, 4, 6, 3, 9, 7, 1, 0, 11, 14, 99]
C = [7, 2, 5, 4]

quickSort(A)
print(callCount)
