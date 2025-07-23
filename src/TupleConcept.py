# Tuple: is a collection of elements of any Python data type
# Tuple vs List:
# 1. syntax: you have to store the values in the tuple with (), but in List: []
# 2. Tuple is immutable but List is mutable
# 3. Can not change the value of tuple elements


names = ("Java", "Python", "Dot Net", "C Sharp")
marks = (10, 45, 67, 89)
employeeData = ("Tom", 25, 'M', 23.45, True)
print(employeeData)
print(employeeData[0])
print(employeeData[3])

#print print(employeeData[5]) #tuple index out of range

print(employeeData[-1])
print(employeeData[-5])

list=[10, 40, 50,89, 100] #mutable- can be changed
list[1]=120
print(list)

#names = ("Java", "Python", "Dot Net", "C Sharp")
#names[2]="English" #tuple is immutable: TypeError: 'tuple'
# object does not support item assignment
#print(names)

#names = ("Java", "Python", "Dot Net", "C Sharp")
#del names
#print(names)

#concatenation of tuples;
t1=(1,2,3)
t2=(4,52,5)
print(t1+t2)

#Multply
t3=(1,2,3)
print(t3*4)

#Range Slices:
t4=(1,2,3,4,5,6)
print(t4[1:3])

#in:
employeeData1 = ("Tom", 25, 'M', 23.45, True)
print(25 in employeeData1)
print(35 in employeeData1)

#not in
print(35 not in employeeData1)

#len:
length=len(employeeData1)
print(length)

#max number:
number=(12,13,120,500)
print(max(number))

names = ("Java", "Python", "Dot Net", "C Sharp")
print(max(names))

names1 = ("abc", "cde", "efg", "xyz")
print(max(names1))

print(min(names1))


















































