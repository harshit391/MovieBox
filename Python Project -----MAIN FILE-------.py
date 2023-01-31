import time

print("Welcome to Movie Box")
time.sleep(1)
print("I am Harshit Singla , the Creater of Movie Box")
time.sleep(1)
print("You will get information about Top movies Globally and Indian and more Stuff about cinema")
time.sleep(1)
print("That's Why I am here to guide you through the movie box")
time.sleep(1)
print("I will be with you everytime")
time.sleep(1)

name = input("Please Enter your Good Name: ")

time.sleep(1)
while True:
    gender = input("Okay , Your Gender: ")
    if gender in ["m","M"]:
        print("Okay , So you are Respected Mr.",name,"Sir")
        break
    elif gender[0] in ["m","M"] and gender[-1] in ["e","E"]:
        print("Okay , So you are Respected Mr.",name,"Sir")
        break
    elif gender in ["f","F"]:
        print("Okay , So you are Respected Mr.",name,"Sir")
        break
    elif gender[0] in ["F","f"] and gender[-1] in ["E","e"]:
        print("Okay , So you are Respected Mr.",name,"Sir")
        break
    else:
        print("Oh It seems you are a very special person , Is it actually ?")
        yn = input()
        if yn[0] in ["Y","y"] and yn[-1] in ["s","S"]:
            print("Okay , So you are Respected",name)
            break
        elif yn in ["y","Y"]:
            print("Okay , So you are Respected",name)
            break
        else:
            print("Oh! Please then check you spellings")
            continue





print("Ok , So lets begin your journey")
time.sleep(1)
import naorglo