"""
    basics
"""
# a=10
# b=2.5
# c="ABC"
# d=False
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# user={
#     "name":"Mukundan",
#     "age":21,
#     "department":"CSE"
# }
# print(user["name"],"is",user["age"],"yrs old and he is from",user["department"])

# age=int(input("Enter the age:"))
# if(age>=18):
#     print("Eligible for voting")
# else:
#     print("Not eligible")

# list=[1,2,3,4,5]
# list.append(10)
# list[0]=23
# print(list)

# tup=(1,2,3,4)

# sett={1,2,3,4,5,3,4}
# print(sett)

"""
 loops
 """
# print("for loop example")
# for i in range(0,50,5):
#     print(i)

# print("WHile loop example")
# j=0
# while(j<5):
#     print(j)
#     j+=1

"""
 List learning
"""

# list=[1,2,3,4,5]
# list.append(9)
# print(list)
# list.insert(1,20)
# print(list)
# list.remove(1)
# print(list)
# list.pop()
# print(list)
# list.pop(2)
# print(list)
# list.clear()
# print(list)

# list2=[1,2,3,4,5,1]
# print(len(list2))
# print(sum(list2))
# print(max(list2))
# print(min(list2))
# list2.sort()
# print(list2)
# list2.reverse()
# print(list2)

# list3={1,"Hello",4.5,False}
# print(list3)

"""
tuple    
"""
# tup=(1,2,3,4)
# print(tup[0])

# print(tup.count(2)) it count tot 2s
# print(tup.index(3)) it taks the ind of the ele

#tuple packing/unpacking
# t=10,20
# print(t)
# print(type(t))
# a,b=(10,20)
# print(a)
# print(b)

"""
 set learning
"""

# s={1,2,2,3}
# print(s)
# s.add(4)
# print(s)
# s.remove(2)
# print(s)
# s.discard(5) same as remove but if it exists else no Key err like that
# print(s)

# a={1,2,3}
# b={3,4,5}
# print(a | b)  union | print all
# print(a & b)   intersection & it print only comon
# print(a - b)    difference - it print pres in a but not in b
# print(a ^ b)   symmetric difference ^ prints all except comon

# s={1,2,3,4,5,6}
# if(15 in s):
#     print("Exists")
# else:
#     print("It doesnt")


"""
dictionary learning
"""

# user={
#     "name":"Mukundan",
#      "age":21,
#      "skills":["dsa","java"]
#      }
# print(user["name"])
# print(user["skills"][0])
# print(user.get("age"))

# user["age"]=22
# user["city"]="Chennai"
# print(user)
# print(user.get("age"))
# print(user.get("city"))

# del user["age"]
# user.pop("city")
# print(user.keys())
# print(user.values())
# print(user.items())

# print(user)
# for key,val in user.items():
#     print(key,val)
# sq={x:x*x for x in range(5)}
# print(sq)

#remove dup in list
# nums=[1,2,2,3]
# u=list(set(nums))
# print(u)

# s="banana"
# freq={}
# for ch in s:
#     freq[ch]=freq.get(ch,0)+1
# print(freq)


# a,b=10,20
# print("Before swap")
# print(a,b)
# a,b=b,a
# print("After swap")
# print(a,b)

"""
 same like switch case
"""
# x=4
# match x:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case _:
#         print("Default")

"""
    operators

"""

#Arithmetic
# a=10
# b=3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)

#relationAL
# a=10
# b=5
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)

# Assignment
# x = 10
# x += 5
# print(x)
# x -= 2
# print(x)
# x *= 2
# print(x)
# x /= 2
# print(x)
# x //= 2
# print(x)
# x %= 2
# print(x)
# x **= 2
# print(x)

#Logical
# a=True
# b=False
# print(a and b)
# print(a or b)
# print(not b)

#bitwise


# a=5
# b=3
# print(a&b)
# print(a|b)
# print(a^b) XOR same means zero else one
# print(~a)   NOT
# print(a<<1)
# print(a>>1)


#Membership operators

# a=[1,2,3]
# print(1 in a)
# print(5 not in a)

# b={"name":"Mukundan","age":21}
# print("name" in b)
# print(21 not in b)


# identity operator
# a=[1,2,3,4,5]
# b=a
# c=[1,2,3,4,5]
# print(a==b) checks value same
# print(a is b) checks memory space

# print(a==c)
# print(a is c)

# def add(a,b):
#     return a+b
# def add(a,b,c):
#     return a+b+c

# print(add(10,20,30))

# s="banana"
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# print(s.count("a"))
# print(s.find("n"))
# print(s.replace("a", "o"))
# print(s.startswith("ba"))
# print(s.endswith("na"))


# def greet(name="User"):
#     print("Hello", name)
# greet("ramesh")

# def total(*nums):
#     return sum(nums)
# print(total(1,2,3))

# def user(**info):
#     print(info)
# user(name="Mukundan", age=21)


# s = "I love India"
# words = s.split(" ")
# words.reverse()
# print(words)
# new = " ".join(words)
# print(new)

# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b 
#     def sub(self):
#         return self.b-self.a
#     def div(self):
#         return self.b/self.a
#     def mul(self):
#         return self.a*self.b 

# calc=Calculator(10,20)
# print(calc.add())
# print(calc.sub())
# print(calc.mul())
# print(calc.div())


# def add(a,b):
#     return a+b
# add=lambda a,b:a+b 
# sub=lambda a,b:a-b 
# mul=lambda a,b:a*b 
# div=lambda a,b:a/b
# print(add(2,3))  

n=10
m=2
arr=[1,2,3,4,5]
try:
    r=n/m
except ZeroDivisionError:
    print("Division by Zero error")
except IndexError:
    print("Array Index out of bound")
else:
    print("No exception occured",r)
finally:
    print("This is always executed")

a="1"
a=int(a)
print(a)
print(type(a))