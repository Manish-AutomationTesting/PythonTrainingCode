x=int(input("Please enter the value of x: "))

if x<0:
    print("x is negative number")
elif x>0:
    print("x is positive number")
elif x==0:
    print("x is equal to zero")
else:
    print("not defined")

if True:
    print("PASS")
else: #Dead code
    print("FAIL")

if 10>5:
    print("Hii")
else:
    print("how are you")

a=100
b=200
c=300
if a>b & a>c:
    print("a is highest number")
elif b>c:
    print("b is the highest number")
else:
    print("c is the highest")

total=int(input("enter the total value: "))
if total<100:
    total=total+20
elif 100 <= total < 500:
    total= total+50
else:
    total=total+100

print(total)#no concat
print("Total: "+str(total))#str method
print(f'{"total value="}{total}')#f string
