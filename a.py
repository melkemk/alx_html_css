total, acc = map(int, input().split())
arr = list(map(int, input().split()))
i=0
num=0
while(i<acc and arr[i]!=0  ):
    num+=1
    i+=1
while(num<total and  arr[num]==arr[num-1] and arr[i]!=0 ):
    num+=1
print(num)