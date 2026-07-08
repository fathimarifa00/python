#sequence
# ''
# ""
# ''' '''

#name = "mohan"
# print(name)
#print (type(name))

data = "mohan's resume"
qt = '''gandhi once said that "say no to violence" '''
print(qt)

#escape sequence

data = 'mohan\'s resume'
print (qt)
#\' -- '
#\" -- "
#\n - new line 
#\t - tab space
#\b - backspace

print (qt)
#raw string
qt








#a= input('enter a number --')
#b= input('enter')
#print (a+b)

# a=int(input('enter a number--'))
# b=int(input('enter a number --'))
# print (a+b)

# a=float(input('enter a number--'))
# b=float(input('enter a number'))
# print(a+b)
 
 #string format
name ="mohan"
marriedstatus = False
age = 29
rating = 4.9

result=f" my name is {name},marriedstatus is{marriedstatus} ,my age is {age},my rating is {rating}"

print(result)



#control statements
#loops

#while
i= 1
while i <= 10:
    print(i)
    i = i+ 1

# sum of first 10 numbers   
#print ("mohan")    
# i = 1
# sum= 0
# while i<=10:
#     sum = sum + i
#     i = i + 1
# print(sum) 

#from 1 to 100  sum of even and odd 

# i = 1
# esum = 0
# osum = 0
# while i <= 100:
#     if i % 2 == 0 :
#         esum = esum + i
#     else:
#         osum = osum + i
#     i = i + 1

# print(esum)
# print(osum)  

# #sum of digits in a number
# # input= 345
# output = 12
# num  = 12345
# sum = 0
# while num > 0 :
#     b = num % 10
#     sum = sum + b
#     #print(num)
#     num = num // 10
# print (sum)

#reverse of a number
#456
#654
num = 345
while num > 0:
 rev = 0
b= num %10
rev = rev * 10 + b
num= num // 10
print (rev)







