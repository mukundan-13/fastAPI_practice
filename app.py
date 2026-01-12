# # x=10
# # #print(x*20)
# # course='Python "hello'
# # print(course)
# # #run shortcut ctrl+r

# # first="hello"
# # second="buddy"
# # third=f"{first} {second}"
# # print(third)
# import math

# course="       python programming       "
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.lstrip())
# print(course.rstrip())
# print(course.find("pro")) #it returns index of the st pos
# print(course.replace("p","j"))
# print("ro" in course)
# print("swift" not in course)

# print(round(2.9))
# print(abs(-3.5))
# print(math.ceil(2.3))
# print(math.floor(2.9))
# print(math.factorial(5))

# x=input("x:")
# y=int(x)+1
# print(f"x:{x},y:{y}")

# print(bool(0))
# print(bool(2))
# print(bool(""))
# print(bool("False"))

# s="Apple"
# print(s[1:-1])

# age=21
# message="Eligible" if age>18 else "Not eligible"
# print(message)

# success=True
# for i in range(3):
#     print("attemp")
#     if success:
#         print("success")
#         break 
# else:
#     print("Not success")

# print(type(5))
# print(type(range(5)))

command=""
while command!="quit":
    command=input(">")
    print("ECHO",command)