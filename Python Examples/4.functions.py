# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 09:26:13 2019

@author: Hani
"""

def my_function(fname):
    print(fname + "is the file name")
    
my_function("Emil")
my_function("Tobias")
my_function("Linus")

print("------------------------------------------------")



def my_function1(food):
    for x in food:
        print(x)

fruit = ["apple", "banana", "cherry"]
my_function1(fruit)

print("------------------------------------------------")

def my_function2(x):
    return 5 * x

print(my_function2(3))
print(my_function2(5*5*5))
print(my_function2(5*7+9))


print("--------------------------------------------------------------------")

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
    

myfunc()
print("Python is " + x)


print("-----------------------------------")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(10))
print("----------------------------")



sum = lambda x, y , z : x + y - z
print ( sum(56,7 , 3))


print("----------------------------------")

MyList = [0,1,2,3,4,10,13,22,25,100,120]
print("squared List:", set(map(lambda x: x**2, MyList)) )


print("-------------------------------------------------------------")


MyList = [0,1,2,3,4,10,13,22,25,100,120]

odd_numbers = list(filter(lambda x: x % 2, MyList))

print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, MyList))

print(even_numbers)


print("----------------------------------------------------------------")

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
def is_A_student(score):
    over_75 = list(filter(lambda sc: sc > 75 , scores))
    print(over_75)
    
is_A_student(scores)

print("---------------------------------------------------------------")



my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1,2,3,4,5]
my_test = ['hani','hasan','SE' , 'Fifa' , 'any']
results = list(zip(my_strings, my_numbers ,my_test))
print(results)


print("-----------------------------------------------------------------")
import functools

lis = [ 1 , 3, 5, 6, 2, ]

print ("The sum of the list elements is : ",end="")
print (functools.reduce(lambda a,b : a+b,lis))

print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 

