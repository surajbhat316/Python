l = list()
n = int(input('Enter the  total # of values : '))
for i in range(n):
    a = int(input())
    l.append(a)
d = dict()
for items in l:
    d[items] = d.get(items,0)+1
print(d)
l1 = list()
for k,v in d.items():
    l1.append((v,k))
sorted(l1, reverse = True)
m= int(input('Enter the value of m'))
for i in range(m):
    print(l1[i][1])
    
