#list
#collection of data:
#[12,33,121,333,3133,]
#properties

# 1.list can have any element of any size
# data = [1,2.2,"mohan",true,12,13,14]
#2. lists are ordered

# a = [1,2,3,4]
# b= [3,2,1,4]
# print(a==b)
#3. lists are intexed
#0 1 2 3 4
# a= [ 11,12,13,14,15,16,17,18,19]
# b = [11,13,15,16,17,19,]
# print(a)

#print(a[1])
#print(a[3:8])
# print (a[0:9:2])
# print(a[:7])
# print(a[4:])
# print(a[::-1])

# (start:stop:step)

# print(a[0])

# 01234
# 0 1 2 3 4

#list are mutable
#strr are immutable
# a = [11,12,13,14,15]
# a[0] = "mohan"
# print (a)

# b = "mohan"
# b = "hohan"
# b[0]= "h"
# print (b)

#dynamic
# a = [11,12,13,14,15]
# a[0:2]= [31,32,33,34,35,36,37]
# print(a)


##6. lists are nested


# inbuilt methods
# to add elements

#append (element)
#adds an element to the end of the lost

# a = [11,12,13,14,15]
# a.append(100)
# a.append(200)
# print(a)

#extend( adds an itreable to the list)

# a= [11,12,13,14,15]
# a.extend([23,24,"mohan"])
# print(a)

#insert (index,value)

# a=(11,12,13,14)
# a.insert(2,"mohan")
#print(a)

#to remove elements remove(element)
# a = [11,12,13,14,15,11,11,11]
# a.remove(11)
# print(a)

#pop () remove the last element from the list
#pop (index)

# a= [11,12,13,142,65,78]
# a.pop(0)
# a.pop(0)
# print(a)

#tuple
#collectn of data
#a= (2,3,4,"mohan",672,32,2,23)
#ordered
#indexed
#immutable

# a = (1,2,3,4)
#a[0] = 10
#print(a)

# 2 boxes

# elastic - list
# metal box - tuple

# a= [11,12,13,14,15]
# b= "mohan das"
# c= (100,200,300,400,500)
# for i in c:
#    print (i)
# a = "mohan"
# print(a[0])
# print(len(a))

# for i in range(0,len(a)):
#     print(i,a[i])
#     fruits= ["apple","orange","banana","watermelon","pineapple","mango"]
# for i in range(0,len(fruits)):
#     print(i,fruits[i])

# prime number
# num = int(input("enter a number:"))
# primr = 0 
# for i   in range(2,num):
#     if num % i == 0:
#         prime = 1
#         break
# if num <= 1:
#  print ("not prime")
# else:
#     print("prime number")




#find vowels and their position in a string 

# name = input("enter your name")
# for i in range(0,len(name)):
#     if name [i]== "a" or name[i]=="e" or name[i]== "i" or name[i] =="o" or name[i]== "u":
#         print(i,name[i])



# name  = input("enter your name")
# vowel="aeiou"
# for i in range(0,len(name)):
#     if name [i] in "aeiou":
#         print(i,name[i])


#create a list of even numbers and odd numbers from first 100 numbers
# c = [1,2,3,4,1,3,4,2,7,8,9,2,3,4,5]
# remove duplicates from this list

# num = []
# even = []
# odd = []

# for i in range (1,101):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
#         print(even)
#         print(odd)

# c = [1,2,3,4,1,3,4,2,7,8,9,2,3,4,5]
# b = []
# for i in c:
#  if i not in b:
#   b.append(i)
# print(b)

# remove duplicates from this list 

#pass statements
# age = 18
# if age >=18:
#     pass
# b = 10
# print (b)

#break
#continue

# for i in range(1,11):
#     if i == 6:
#      break
#     print(i)

# for i in range (1,11):
#  if i==6:
#   continue
# print(i)


#prime num

# num = int(input("enter your number"))
# if num == 1:
#     print("not prime")
# else:
#     for i in range(2,6):
#         if num %i ==0:
#            print("not a prime")
#         break
#     else:
#      print("prime number")


# input n words and make it into a  sentence


# n = int (input("enter your words"))
# sentence = ""

# for i in range(n):
#    word=input("enter the word")
#    sentence = sentence+word+" "
# print (sentence)
   
   
#reverse  of a string without using ( -1 )    

string=input("enter the string")  
i=len(string)-1
rev=""
while i>=0:
   rev=rev+string[i]
   i=i-1
print(rev)


 










        






          








