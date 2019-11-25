# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:51:16 2019

@author: Hani
"""

s1 = "Hello Orange Academy"
print(s1)
print(s1[0])
print(s1[-2])
print(s1[2:10])
print (s1[5:])
print ( s1.capitalize() )
print (s1 * 2)
print ( s1.upper() )
print (s1.center(20) )
print (s1.replace('Orange', 'Amman'))
print (' world '.strip() )
s2='#'.join(['hello','Orange'])
print(s2)



print("----------------------------------------------")
list1=[1,20,-1,0,1000]
list2=[23,546]

list1.extend(list2)
print(list1)
print(len(list1))
print(min(list1))
print(max (list1) )
print( sum (list1) )
print(sorted(list1))
list1.sort()
print(list1)




print("----------------------------------------------")
my_tuple = 1,20,100,5,3,20 
print(my_tuple)


print("----------------------------------------------")

my_list=['a','b']
t1 = ("Apple",) # Note , is for one item
t2 = t1 + (1,2,3) + tuple(my_list)
print (t2)
print (t2[0])
print (t2[1:4])


print("----------------------------------------------")


s1={1,2,3,4,5,6}
s2={2,4,6,8,10}
print ( s1 | s2 ) 
print ( s1 & s2 ) 
print ( s1 - s2 ) 
print ( s1 ^ s2 )

print("------------------------------------------------")



infoStd = {
"id": "111199996666",
"name": "Mustang",
"university": "xyz",
"major":"coding"
}
print(infoStd)


for x, y in infoStd.items():
    print(x, ":" ,y)
    
print("-------------------------------------------------")
my_list1 = ["Apple",1,1.2222]
my_list2 = [10,20,["Orage",3]]
my_list3= my_list1 + my_list2
print(my_list3)
print("Apple" in my_list3 )

print(my_list3[1])
print(my_list3[5][1])
print(my_list3[2:])
print(my_list3[:-1])    


print("-------------------------------------------------")
my_list1 = ["b","c","a"]
del my_list1[0]
print (my_list1)


