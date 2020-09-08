a = [[1,2,3], [4,5,6], [7,8,9]]
print(a)
getFirstColumn = [sum(x) for x in zip(*a)]
getRowSums = [sum(x) for x in a]
print(getFirstColumn)
