password="@Marwane_2003"
i=1
enter_password="k"
while enter_password!=password and i<=4:
    enter_password=input("enter your password you have four tries:")
    if enter_password!=password:
        print("your password is incorrect")
        i+=1
        if i==5:
            print("your account is blocked")
            break
    if enter_password==password:
        print("welcome to your account")
        break