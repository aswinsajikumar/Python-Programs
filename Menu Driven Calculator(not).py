print  ("MENU")
print  ("1.Add")
print  ("2.Subtract")
print  ("3.Multiply")
print  ("4.Divide")
ch=input('Choice:')

a=input("Enter 1st number:")
b=input("Enter 2nd number:")

if ch =='1':
	print (a+b)
elif ch =='2':
	print (a-b)
elif ch =='3':
	print (a*b)
elif ch =='4':
	print (a/b)
else:
	print ("Invalid Input")
