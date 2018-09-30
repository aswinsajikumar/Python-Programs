n=int(input("Enter the number:"))
num=n
ans=0
for c in range(1,n+1,1):
    r=n%10
    ans=ans+r
    n=n//10
print ('The sum of the digits of',num,'is',ans)
    
