#comparison operators
# equal to  ==
a=5
b=6
print(a==b)
#not equall to !=
print(a!=b)



#logical operators
# and
# true true True
# true false False
# false true False
# false false False
a=5
b=5
if a>3 and b==5:
  print("yes")


  # or
  # true true True
  # true false True
  # false true True
  # false false False
  if a>=5 or b==7:
    print("yes")
  
  if (a>=4 or a==b)and(b==5 or a>2):
    print("yes")

 #not
 if not a==10:
  print("no") 
   























# conditional statement
# if condition:
   #code to be executed

age= 34
if age >= 18:
   print("eligible")
age= 15
if age >= 18:
  print("eligible")   
else:
   print("not eligible") 

  
# check if a number is odd or even
a=5
if a%2==0:
 print("a is a even")
else: 
 print("a is a not a even")

# check if a number is a multiple of five

a=2
if a*5==5:
  print("a is a multiple of 5")
else:
 print("a is a not a multiple of 5")

# largest of two numbers
# a = 5
# b = 7
if a>b:
  print("a is larger")
else:
  print("b is a larger")

  mark=35
  if mark > 70:
    print("B+")
  elif mark> 60: 
   print("B") 
  elif mark > 50:
    print("C+")
  elif mark> 40:
    print("C")
  else:
    print("fail")
    #check if a num is neg or pos or 0
    num= 5
    if num >0:
      print("pos")
    elif num <0:
      print("neg")
    else:
      print("0")

      #largest of 3 numbers
      a=10
      b=11
      c= -100

      if a>b and a>c:
        print("a is larger")
      elif b > a and b>c:
        print("b is largest")
      else:
        print("c is largest")

        


        
      


