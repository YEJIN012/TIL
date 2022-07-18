n = int(input())
number = list(range(1,n+1))
for i in number : 
    print(i)

n = int(input())
number = list(range(1,n+1))
for i in number : 
    print(i, end = ' ')

n = int(input())
number = list(range(n,-1,-1))
for i in number : 
    print(i)

n = int(input())
number = list(range(n,-1,-1))
for i in number : 
    print(i, end= ' ')

n = int(input())
number = list(range(1,n+1))
ans = 0
for i in number :
    ans = ans + i 
print(ans)