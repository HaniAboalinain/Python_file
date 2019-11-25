# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:25:55 2019

@author: Hani
"""

"""
#Q1
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the Second number: "))

if num1 > num2 :
    print(num1)
else:
    print(num2)
    
    
print("------------------------------------------------------------------------")

#Q2
number = int(input("Enter the number you want to get table of multiplication: "))

for i in range(1 , 11 , 1):
    print(number , "*" , i , "=" , number * i)





print("------------------------------------------------------------------------")


#Q3

for i in range(1 , 6 , 1):
    for j in range(i):
        print("*" , end="")
    print()
    
for i in range (5, 1, -1):
    for j in range(0, i -1):
        print("*", end='')
    print()

print("------------------------------------------------------------------------")

#Q4

letters =  ["x","y","z","a","b","c"]
for i in letters:
    if i == "a":
        continue
    elif i== "c":
        break
    print(i)
    

the output = 
x
y
z
b
       


print("------------------------------------------------------------------------")

#Q5
for x in range (12 , 25 , 3):
    print(x)
    

the output = 
12
15
18
21
24
      


print("------------------------------------------------------------------------")

#Q6
i = 1 
while i < 6 :
    print(i)
    if i== 3:
        break
    i +=1
 
the output = 
1
2
3
    



print("------------------------------------------------------------------------")

#Q7
num = int(input("enter the number: "))
sum = 0 

for i in range(1 , num , 1):
    sum = sum + i
   
print("sum =" , sum)




print("------------------------------------------------------------------------")

#Q8

num = int(input("enter the numberto get if odd or even: "))

if num % 2 ==0 :
    print("the number is even" , num)
else:
    print("the number is odd:" , num)

print("------------------------------------------------------------------------")
"""
#Q9

for i in range(1,10):
    for j in range(10 - i):
        print (" " , end=" ")
    for j in range(1,i):
        print(j, end=" ")
    for i in range(i , 0 , -1):
        print(i , end=" ")
    print()
for i in range(8,0 , -1):
    for j in range(10 - i):
        print (" " , end=" ")
    for j in range(1,i):
        print(j, end=" ")
    for i in range(i , 0 , -1):
        print(i , end=" ")
    print()        

print("------------------------------------------------------------------------")

#Q10

while True: 
    try:
        n = input("Please enter an integer: ")
        n = int(n) 
        break
    except ValueError:
        print("No valid integer! Please try again ...") 
print("Great, you successfully entered an integer!")


print("------------------------------------------------------------------------")

#Q11

try:
    a=3
    if a < 4:
        b=a/(a-3)
    print("Value od b =",b)
except (ZeroDivisionError, NameError):
    print("\n Error Occured and Handled")
    
"""
output = 
Error Occured and Handled

"""
        
    