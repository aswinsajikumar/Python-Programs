n=int(input('Enter the number:'))
num=n
arm=0
length=len(str(n))
while(n>0):
    r=n%10
    arm=arm+(r**length)
    n=n//10
if arm==num:
    print ('Armstrong number')
else:
    print ('Not an Armstrong number')
