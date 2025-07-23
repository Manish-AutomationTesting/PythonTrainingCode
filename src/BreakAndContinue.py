name="Alexander"
for i in name:
    print(i)
    if(i=='x'):
        break

print("**********")
name="Alexander"
for i in name:
    print(i)
    if(i=='x'):
        continue

print("********")
str=["Python", "Java", "C-Sharp", "Dot Net"]
for l in range(len(str)):
    print(str[l])
    if(str[l]=="Java"):
        print("Hey I Found Java!!!")
        break

print("********")
str=["Python", "Java", "C-Sharp", "Dot Net"]
for l in range(len(str)):
    print(str[l])
    if(str[l]=="Java"):
        print("Hey I Found Java!!!")
        continue


print("*********")
lang=["Hindi", "English", "French", "Spanish", "German", "Chinese"]
flag=False
for index in range(len(lang)):
    print(lang[index])
    if(lang[index]=="Spanish"):
        print("Spanish is the 2nd most popular language in the world")
        flag=True
        break
if(flag):
    print("I want to Learn Spanish")
