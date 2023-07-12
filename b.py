x,y = list(map(int, input().split()))
z=(x*(x+1))/2
n=x
while(y!=z):
    z=z-1-(1+(n-1))
    n-=1
print(x-n)