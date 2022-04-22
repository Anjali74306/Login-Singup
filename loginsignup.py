# import json
# import os

# print("WELCOME IN LOGIN AND SIGNUP PAGE!")
# def signup(password):
#     if len(password)>=6 and len(password)<=16:
#         if password>="a" or password<="z":
#             if "@" in password or "#" in password:
#                 if "1"in password or "2"in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password or "0" in password:
#                     print("strong passward")
#                 else:
#                     print("week passward")
#                     p=input("Enter your passward:")
#                     signup(p)
#             else:
#                 print("add special character.")
#                 p=input("Enter your paasward:")   
#                 signup(p)
#         else:
#             print("add alphabets")
#             p=input("Enter your paasward:")
#             signup(p)
#     else:
#         print("please check the lenght of passward, atleast 6 and maximum 16.")
#         p=input("ENter your passward:")
#         signup(p)
# def confrm_pasword(p,p1):
#     if p==p1:
#         print("correct")
#     else:
#         print("your confirm passward is not match with passward.")
#         p1=input("Enter your confirm passward:")
# user=input("what you want to do login or signup:")
# file=os.path.exists("signup.json")
# if file ==False:
#     if user=="signup":
#         n=input("Enter your name:")
#         p=input("Enter your passward:")
#         signup(p)
#         p1=input("Enter your confim passward:")
#         confrm_pasword(p,p1)
#         print("congrats",n,"you signed up successfully")
#         dob=input("Enter your dob")
#         g=input("Enter your gender male or female:")
#         l=[]
#         dic={}
#         n1=["name","passward","dob","gemder"]
#         info=[n,p,dob,g]
#         for i in range(len(n1)):
#             dic.update({n1[i]:info[i]})
#         l.append(dic)
#         with open("signup.json","a") as f:
#             json.dump(l,f,indent=2)
# elif file==True:
#     if user=="signup":
#         n=input("Enter your name:")
#         p=input("Enter your passward:")
#         signup(p)
#         p1=input("Enter your confirm passward:")
#         confrm_pasword(p,p1)
#         r=open("signup.json","r")
#         n2=r.read()
#         if n in n2:
#             print("name is already exists")
#         else:
#             print("congrates",n,"you are signed up successfully")
#             dob=input("Enter your dob:")
#             h=input("Enter your hobby:")
#             g=input("Enter your gender:")
#             d=input("Enter yiur description:")
#             dic={}
#             n1=["name","passward","dob","gender"]
#             info=[n,p,dob,h,g,d]
#             for i in range(len(n1)):
#                 dic.update({n1[i]:info[i]})
#             with open("signup.json","r") as f:
#                 data=json.load(f)
#             data.append(dic)
#             with open("signup.json","w") as f:
#                 json.dump(data,f,indent=2)
#     elif user=="login":
#         u=input("Enter your name :")
#         u1=input("Enter your passward:")
#         with open("signup.json","r") as f:
#             da=json.load(f)
#             for i in range(len(da)): 
#                 if da[i]["name"]==u:
#                     if da[i]["passward"]==u1:
#                         print("login successfully")
#                         print("your name is",da[i]["name"],"\n")
#                         print("and your data is :-\n")
#                         for x,y in da[i].items():
#                             print(x,'=',y)
                            
#                     else:
#                         print("this name is not exist in this file.")
#                         break

# a="nav"
# a="gurukul"
# print(a)


# a="anjali\nsingh"
# print(a)


# a="2020"
# b="01"
# c="22"
# print(a,"/",b,"/",c)

