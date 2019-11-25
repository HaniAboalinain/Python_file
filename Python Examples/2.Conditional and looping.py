# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:16:36 2019

@author: Hani
"""
"""
a,b = 10,10

if a > b :
    print("a > b")
    
elif a<b:
    print("b > a")

else:
    print("a = b")

print("------------------")

a,b = 100,100
max = a if (a > b) else b
print(max)



print("------------------")
"""
"""
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

if num1 > num2:
    print(num2 , num1 , sep="  ")
else:
    print(num1 , num2 , sep="  ") 


print("----------------------")

name = input("enter your name ! ")
age = int(input("enter your age : "))

if age < 18 :
    print("Under age ")
    avg = float(input("Enter your school avg: "))
    if avg > 90:
        print("Excellent avg")
    elif avg < 90.0 and avg > 50.0:
        print("passed")
    else:
        print("failed")

else :
    print("adult")
    jobTitle = input("enter your job title ! ")
    print(age , name , jobTitle , sep=" -- ")
    
"""
    
"""
for a in range(3):
    print(a)

print("--------------")


for a in range(1,60,15):
    print(a)
        
    
print("--------------")

for x in "hani":
    print(x)    
"""
"""
i = 0 
while True:
    a=input('>>>')
    if a == 'exit':
        break
    print(a)
"""
"""
for x in range(11):
    print("*")
    
for x in range(11):
    print("*" , end=" ")  
""" 
    
    
for x in range(1 , 9 , 1):
    for y in range(x):
        print("*" , end="")
    print("\n")

print("------------------")

for x in range(1 , 9 , 1):
    for y in range(x):
        print("*" , end="")
    print("\n")
    
print("---------------------")

try:
    x = float(input("Your number: ")) 
    inverse = 1.0 / x 

except ValueError:
    print("You should have given either an int or a float") 

except ZeroDivisionError:
    print("Infinity")

finally:
    print("There may or may not have been an exception.")


