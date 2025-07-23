def login(userName, password):
    print(userName, password)

login("Naveen", "test123")

login(userName="Naveen", password="test123")

#*arg
def getMarks(*arg):
    for x in arg:
        print(x)

getMarks(10,20,30,40,50)
getMarks("A","A+", "B", "B-")

#keywords args:
#**arg
def getStudentsMarks(**args):
    for key, value in args.items():
        print("%s==%s" %(key, value))

getStudentsMarks(naveen=10, tom=20, peter=30)
getStudentsMarks(key="apple", sellerName="Xeon")

#Lambda functions: Annonymous function;
#A function without any name:

cube = lambda x:x*x*x

print(cube(4))

total = lambda marks: marks +30

print(total(100))





