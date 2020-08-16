no_stu  = int(input())
list1 = [[input(), float(input())] for i in range(no_stu)] 
#print(list1)

y = []
for i in list1:
    y.append(i[1])

#print(y)
y.sort(reverse=False)


a = y[1]
faulters = []
for i in list1:
    if i[1] == a:
       faulters.append(i[0])

done1 = sorted(faulters)
for i in done1:
    print(i)

