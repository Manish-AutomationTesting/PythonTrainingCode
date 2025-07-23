def test():
    print("Hello Python")


test()


def abc(a):
    print(a + 10)


abc(120)


# optional paramter
def getCountryName(name="India"):
    print(name)


getCountryName()
getCountryName("UK")
getCountryName(100)


# pass a list to a function
def getNames(list):
    for x in list:
        print(x)


name = ["Naveen", "Peter", "Brian", "Mitchel"]
getNames(name)  # calling a function


# function with return
def sum(a, b):
    c = a + b
    return c


s1 = sum(10, 20)
print(s1)


def getCapitalName(countryName):
    if countryName == "India":
        return "New Delhi"
    elif countryName == "USA":
        return "Washington DC"
    else:
        print("Not defined")


print(getCapitalName("India"))
print(getCapitalName("USA"))
getCapitalName("China")


# Launch Browser

def launchBrowser(browserName):
    if browserName == "Chrome":
        print("Launch Google Chrome")
    elif browserName == "Firefox":
        print("Launch firefox")
    elif browserName == "IE":
        print("Launch Internet Explorer")
    else:
        print("Browser not defined")


launchBrowser("Opera")

#recursion in Python:
#A function is calling itself
#WAP to get factorial of a given number
#fact(4)=4*3*2*1=24
#fact(5)=5*4*3*2*1=120

def fact(num):
    if num==0:
       return 1

    elif num>=1:
        num =num*fact(num-1)
        return num

print(fact(0))
print(fact(4))
print(fact(9))

def login(userName, Password):
    print("login with %s and %s" %(userName, Password))

login("Maneesh@gmail", "Password@1")





