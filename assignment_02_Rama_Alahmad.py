#assignment_02
##exercise1
#def factorial(n):
#  f=1
#if n<=0 : 
#    print("invalid number")
#elif n==0 or n==1:
#   return 1 
#else:
# for i in range(1,n+1):
#    f*=i
#    return f
#n=int(input("please enter a positive number"))
#f=factorial(n)
#print("n,(factorial(n))")

##exercise2
#def divisor(n):
#    divisors=[]
#    for i in range(1,n+1):
#     if (n%i==0):
#      divisors.append(i)
#      return divisors
     
#n=int(input("please enter a number:"))
#print(divisor(n))

##exercise3
#def reverseString(s):
#  reversed_str=""
#  for char in range(len(s)-1):
#   return reversed_str
#s=str(input("enter a string:"))
#print(reversed_str)

##exercise4
#def even_numbers(n):
#    even_number =[]
#    for n in even_number:
#     if (n%2==0):
#            even_number.append(n)
#            return even_number
#n=[input("enter a list of integers:")]
#print (even_numbers)

##exercise5
#def password(p):
#    uppercase_letter= False
#    lowercase_letter= False
#    digit= False
#    special_charachter = "#,?,!,$"
#    sp= False
#    for char in p:
#       if (len(P)>=8):
#        digit= True
#       if ('A'<=char<='Z'):
#        uppercase_letter= True
#       if ('a'<=char<='z'):
#        lowercase_letter= True
#       if char in special_charachter:
#        sp=True
#    if (uppercase_letter and lowercase_letter and digit and sp):
#     return "strong password"
#    else:
#     return"weak password"
#p=input("enter a strong password:")
#print(password(P))

##exercise6
#def valid_IPv4_address(ip):
#    if len(octet)!=4:
#     return "invalid ip"
#     for octet in ip:
#       if n<0 or n>255:
#        return "invalid ip"
#    else:
#      return "valid ip"
#ip= input("please enter ip address:")  
#print(valid_IPv4_address(ip))