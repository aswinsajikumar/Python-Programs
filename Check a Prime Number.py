n=int(input('Enter the number:'))
for i in range(2,n,1):
    if n%i==0:
        print(n,'is not a Prime Number')
        break
else:
    print(n,'is a Prime Number')
