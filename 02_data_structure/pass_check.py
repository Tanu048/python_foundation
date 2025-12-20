password=input("ENter your password: ")

strength=0
special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"

is_a_num = any(i.isdigit() for i in password)
has_upp = any(i.isupper() for i in password)
has_low = any (i.islower() for i in password)
has_special = any(char in special_chars for char in password)

if len(password) > 8:
    if is_a_num:
        strength+=1
    else:
        print("Needs a number")
    if has_upp:
        strength += 1
    else:
        print("Needs uppercase letters")
    if has_low: 
        strength += 1 
    else:
        print("Needs lowercase characters")
    if has_special:
        strength += 1
    else: 
        print("Add special character.")    


    if strength==1:print("Your password strength is *LOW*")
    if strength==2:print("Your password strength is *MEDIUM*")
    if strength==3:print("Your password strength is *HIGH*")
    if strength==4:print("Your password strength is *EXCELLENT*")

else:
    print("Password must carry 8 or more characters!!!")