import time
import os

print("Welcome to encryption tutorial")
print("In this we'll learn CEASER CIPHER generation")

time.sleep(3)
cls=lambda:os.system('cls')
choice='yes'
choice2='yes'

while (choice == choice2):
    x=0
    
    cls()
    print("Enter an information to get the CEASER CIPHER for it :")
    str=input()

    l=len(str) #length of the input text


    enc=[]   #declaring array for cipher text
    enc=['']*(l)

    while(x<l):
        y=ord(str[x])
        y+=3
        enc[x]=chr(y)
        x+=1

    print("information text :",end=' ')
    print(str)   
    print("encrypted text   :",end=' ')
    x=0
    while(x<l):
        print(enc[x].upper(),end='')
        x+=1
    else:
        print()

    print("\n")
    
    print("Wish to continue for another information ?")
    print("yes/no :",end=' ')
    choice2=(input())
    
   
    
    
else:
    cls()
    print("Thankyou for using Ceaser Cipher Cryptography Technique.")
    print("Wish you good luck!")
    print()
