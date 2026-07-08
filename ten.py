#nested loops

# for i in range (1,6):
#     for j in range(1,6):
#      for k in range(1,6):
#             print(i,j,k)


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print("* ",end="  ",)  
#     print()    


#print chesssboard pattern
# for i in range (1,9):
#     for j in range(1,9):
#         if (i+j) %2 == 0:
#             print("W",end=" ")
#         else:
#            print ("B",end=" ")
#     print()

#print pattern in H and I in star

# for H pattern
# 
















# a = [11,13,14,15,16,17,18,19,20,12,15]
# mid=len(a)//2
# c=[]
# d=[]

# for i in range [len(a)]:







#a = [11,1,100,-900,10,15,16]  
# #print smallest and largest int from this list

# largest=0
# smallest=0
# for i in a:
#  if i> largest:
#   largest = i
#  if i < smallest:
#   smallest = i
   
# print(largest,smallest)
#
# #b = sorted(a)
#print(b)


# functions

#block of code which is executed whwn it is calling
#def functionname(< arguments >):
  #code to be executed
#DRY - dont repeat yourself

# def hello():
#  print ("hello good afternoon !!!!")
# hello()  # calling a function
# hello()

# def add2(a,b):#former parameters
#     print(a+b)
# add2(1,2)
# add2(10,20) #actual parameters

# types of arguments
#1.positional arguments  
# def add2(a,b):
#     print(a+b)
#     add2(3,8)

#2.keyword arguments
#def fullname(fname,mname,lname):
#print(fname+''mname+''lname)
#fullname(lname="jr",fname="robert",mname="downey")

#default arguments
#def add2(a=0,b=0):
#print(a+b)

# holo square
# for i in range(1,6):
#     for j in range(1,6):
#         if j == 1 or j == 5 or i==1 or i==5: 
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    

#     print()    


#S pattern

# for i in range(1,6):
#  for j in range(1,6):
#   if i == 1 or
#      print("*",end= " ")
# else:
#     print(" ",end=" ")
# print()

#return statement

# def add2(a,b):
#     return 1,"mohan", True
# print(add2(1,3))

# create a calculator using function:
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div (a,b):
#     return a/b

# def main():
#  while True:
#   print( "welcome to simple calculator..!!!!")
#   ch = int(input("enter your choice : \n1.Add\n2.Sub\n3.Mul\n4.Div\n5.exit\n:----"))

#   x = int(input("enter number:"))
#   y = int(input("enter the number:"))
#   if ch == 1:
#       print(add(x,y))
#   elif ch == 2:
#       print(sub(x,y))  
#   elif ch == 3:
#       print(mul(x,y))    
#   elif ch == 4:
#       print(div(x,y))   
#   elif ch == 5: 
#         break
#   else:
#       print("invalid choice")   
# main()       


# lambda function
# anonymous function

# z = lambda x,y : x+y
# print (z(2,3))

# product of 3 numbers
# z = lambda a,b,c: a*b*c 
# print (z(2,2,2))


# square of a number
# z= lambda a,b: a**b
# print(z(2,5))


#perimeter of a circle
# z= lambda r: 2*3.14*r
# print(z(3))

# area of a triangle
# z = lambda x,y:1/2*x*y
# print(z(2,3))

# average of 5 number
# z = lambda a,b,c,d,e:(a+b+c+d+e)/5
# print(z(4,5,6,7,7))

# square root of a number
# z = lambda x:x**1/2
# print(z(3))


# full name of a person



# # check if a person is eligible to vote or note
# check = lambda age: "eligible" if age >= 18 else "not eligible"
# print(check(21))

#age calculator
# bmi calculator





        
  










 
























