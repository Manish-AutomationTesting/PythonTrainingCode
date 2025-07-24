# set - not order based
# it stores different types of data
# it performs different mathematical operations
# it does not store duplicate elements

# define a set: use {}
s1 = {100, "Tom", 12.34, True, "Tom"}
s2 = {1, 2, 1, 2, 1, 1, 3, 2}
print(s2)
print(s1)

# set () function:
s3 = set("Python")
print(s3)

s4 = set([30, 40, 50, 60, 70, 50])
print(s4)

s5 = set((10, 20, 45, 43, 20))
print(s5)

# While creating a set object, you can store only numbers, string, tuple
# list and dictionary objects are not allowed

set1 = {(10, 20), 30, 40}
print(set1)
# set2 = {[10, 20], 30, 40}
# print(set2)  # TypeError: unhashable type: 'list'

# set Operations:
# Union:
p1 = {1, 2, 3, 4, 5}
p2 = {4, 5, 6, 7, 8}
print(p1 | p2)
print(p1.union(p2))
print(p2.union(p1))

# Intersections: &
p3 = {1, 2, 3, 4, 5}
p4 = {4, 5, 6, 7, 8}
print(p3 & p4)
print(p3.intersection(p4))

# difference of two sets: - or difference method
p5 = {1, 2, 3, 4, 5}
p6 = {4, 5, 6, 7, 8}
print(p5 - p6)
print(p6 - p5)
print(p5.difference(p6))
print(p6.difference(p5))

# Symmetric difference: ^
p7 = {1, 2, 3, 4, 5}
p8 = {4, 5, 6, 7, 8}
print(p7^p8)
print(p7.symmetric_difference(p8))

#Set - In Built methods:
#1. add():
s1={"Java", "Python", "C++"}
s1.add("Perl")
print(s1)

#2. Update:
s2={"Java", "Python", "C++"}
s2.update(["C", "VBA"])
print(s2)

s2.update(("Ruby", "JavaScript"))
print(s2)

#3, clear:
s2.clear()
print(s2)

#4. copy:
lang={"Java", "Python", "C++"}
lang1=lang.copy()
print(lang1)

#5. discard:
lang={"Java", "Python", "C++"}
lang.discard("C++")
print(lang)

lang.discard("Naveen")
print(lang)
#6. remove:
student ={"Naveen", "Tom", "Steve", "Peter"}
student.remove("Tom")
print(student)
student.remove("Sam")



















