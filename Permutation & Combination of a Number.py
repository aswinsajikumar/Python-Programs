def fact(x):
    f=1
    for i in range(x,1,-1):
        f=f*i
    return f
n=int(input('Enter n:'))
r=int(input('Enter r:'))
d=n-r
nf=fact(n)
rf=fact(r)
df=fact(d)
ans=nf/(rf*df)
print ('Combination(nCr)=',ans)
ans1=ans*rf
print ('Permutation(nPr)=',ans1)
