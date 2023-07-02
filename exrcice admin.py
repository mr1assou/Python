admins=["marwane","hamza","raghad","malika","mohamadine"]
name=input("please enter your name:").lower()
print(name)
#print(name in admins)
if name in admins:
    answer=input("welcome back you are a admin you want update or delete you name:").lower()
    if answer=="update" or answer=="u":
        newname=input("enter your new name please:")
        admins[admins.index(name)]=newname
    elif answer=="delete" or answer=="d":
        admins.remove(name)
    else:
        print("wrong option")
else:
    wrong_op=input("you are not a admin add you Y/N:").lower()
    if wrong_op=="yes" or wrong_op=="y":
        admins.append(name)
    elif wrong_op=="no" or wrong_op=="n":
        print("you are not added")
print(admins)
        
     
