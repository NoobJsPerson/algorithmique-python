# Question 1:
nb=int(input("Donner une valeur entiere :"))
if nb%2 == 0:
	print(f"{nb} est pair")
if nb%2 == 1:
	print(f"{nb} est impair")

# le program lit un entier et verifie si cet entier est pair ou impair

nb=int(input("Donner une valeur entiere :"))
if nb%2 == 0:
	print(f"{nb} est pair")
else:
	print(f"{nb} est impair")


# Question 2:
x=float(input("Donner un reel :"))
y=float(input("Donner un second reel :"))
op=input("Donner un operateur :")
if op=="+":
	res=x+y
else:
	res=x-y
print(x,op,y,"=",res)


x=float(input("Donner un reel :"))
y=float(input("Donner un second reel :"))
op=input("Donner un operateur :")
if op=="+":
	res=x+y
elif op=="-":
	res=x-y
elif op=="*":
	res=x*y
elif op=="/":
	res=x/y
print(x,op,y,"=",res)
