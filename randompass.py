import random
import string
import pyperclip
def menu(): #select the length
    print("Select the length of the password you want")
    num=int(input("1.Of length 4\n2.Of length 6\n3.Of length 8\n4.Of length 12"))
    return num
def header(): # for the header only
        print("\n\n\n\n\n\n\n\n\n\n\n")
        print( "\t\t        <><><>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>--<><><>") 
        print("\t\t        <><><>---<>---<>---<>---<>---<>---<< CryptKey>>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<><><>")
        print( "\t\t        <><><>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>---<>--<><><>")
        print("\n")
val=string.ascii_letters+string.digits+string.punctuation # sum all the character whether they are uppercase, lowercase or special character
header()
choice=menu()    #give the value according to the selection  to pass_len
if(choice==1):
     pass_len=4
elif(choice==2):
     pass_len=6
elif(choice==3):
     pass_len=8
else:
     pass_len=12
password=""
for el in range(pass_len):
    password +=random.choice(val) #choice function of the random modulue and give them val in the parethesis this function will choose anything onto this

print("The strong password that the system suggest you is ",password) #show the random password
#this is the code to copy the pasword on the clipboard
copy=input("To copy the password press (C) else press anything").upper()
if(copy=="C"):
    pyperclip.copy(password)