#print(1)
#print(2)
#print(3)
#print(4)
#print(5)

#while loop:
print("************While loop************")
count =0
while(count<10):
    print(count)
    count =count+1

num=0
while(num<3):
    print("Hello Python")
    num=num+1
else:
    print("Bye Python")

#for loop:
name=["Java", "Python", "dot net", "C Sharp"]
for i in name:
    print(i)

str="I Love Python"
for i in str:
    print(i)

print("**************")
list=[1,45,56,78,89]
for i in list:
    print(i)

print("*****************")

list=["Naveen", "Automation", "Labs"]
for index in range(len(list)):
    print(list[index])

#for loop with else:
print("*************")
countyList=["India", "UK", "Japan", "USA"]
for index in range(len(countyList)):
    print(countyList[index])
else:
    print("Country List is over")

print("******Print city List**********")

cityList=["Patna", "Bhopal", "Banglore"]
for index in range(3):
    print(cityList[index])
else:
    print("city List is over")

#nested for loop:
for i in range(1,5):
    for j in range(i):
        print(i, end='')
    print()






