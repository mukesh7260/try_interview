intervals = [[2,4],[4,7],[8,10]]
result = []
for i in intervals:
    if not result or result[-1][1] < i[0]:
        result.append(i) 
    else:
        result[-1][1] = max(result[-1][1],i[1])

print(result)


#  o/p : - [[2, 7], [8, 10]]