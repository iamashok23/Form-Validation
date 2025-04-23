
import re

#name
while True:
    data = input("Enter Your Name: ")
    pattern = re.compile(r'^[A-Za-z ]+$')
    res = pattern.fullmatch(data)
    if res != None:
        name = res.group()
        break
    else:
        print("Enter name in correct manner !")

#Date of Birth
while True:
    data = input("Enter Date of Birth: ")
    pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
    res = pattern.fullmatch(data)
    if res != None:
        dob = res.group()
        break
    else:
        print("Enter Date of Birth in Correct Manner !")
#Email Id
while True:
    data = input("Enter Email Id: ")
    pattern = re.compile(r'^[a-z0-9]+@gmail.com$')
    res = pattern.fullmatch(data)
    if res != None:
        emailid = res.group()
        break
    else:
        print("Enter Email id in correct format !")
#Mobile Number
while True:
    data = input("Enter Mobile Number: ")
    pattern = re.compile(r'^[789]\d{9}$')
    res = pattern.fullmatch(data)
    if res != None:
        mobile = res.group()
        break
    else:
        print("Enter Mobile Number in Correct format !") 
#Gender
while True:
    data = input("Enter Gender [Male / Female]: ")
    pattern = re.compile(r'^Male|Female$')
    res = pattern.fullmatch(data)
    if res != None:
        gender = res.group()
        break
    else:
        print("Enter Gender in Correct format !")

print()
f = open("details.txt","a")
f.write("Details: \n\n")
f.write(f"Name: {name}\n")
f.write(f"Date of Birth: {dob}\n")
f.write(f"Email Id: {emailid}\n")
f.write(f"Gender: {gender}\n")
f.write(f"Mobile Number: {mobile}\n")
f.close()
print("check Your File")
'''
print(f"Name: {name}")
print(f"Date of birth: {dob}")
print(f"Email id: {emailid}")
print(f"Gender: {gender}")
print(f"Mobile number: {mobile}")
'''








