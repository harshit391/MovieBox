import time

print("OMG !! , I have list of 49 Companies How much You Want")
time.sleep(0.5)

li = ["Warner Bros.","Universal Pictures","Columbia Pictures","Walt Disney Pictres","Marvel Studios","Paramount Pictures","20th century Fox","Legendry Pictures","New Line Cinemas","Dune Entertainment","Dreamworks Animation","Relativity Media","Diney Pixar","Amblen Entertainment","Village Roadshow","Metro Goldwyn Mayer Pictures","Dreamworks Pictures","Regency Enterprices","Lucas Films","Heyday Films","Walt Disney Animation","Lionsgate","Rat Pac Entertainment","Original Films","Summit Entertainment","TouchStone Pictures","Working Title Films","di Bonaventura Pictures","TSG Entertainment","Jerry Bruckheimer","Wingut Films","Bad Robot","Illumination Entertainment","Eon Productions","Perfect World Pictures","1492 Pictures","Sky Dance Productions","Fox 2000 Pictures","The Kennedy/Marsh","Imagine Entertainemnt","One Race Films","Atlas Entertainment","Ingenious Film Partners","Blue Sky Studios","Temple Hill Entertainment","Sony Pictures","Syncopy","Hasleri Studios","Blumhouse"]

li2 = [47.6,46.4,45.3,39.7,37.4,33.7,26.1,17,17,16.5,15.7,15.3,14.7,14.6,14.1,13.7,13.4,12.9,11.6,11.2,10.5,10.3,9.9,8.5,8.4,8.4,7.8,7.6,7.4,7.3,7.2,7.1,7.1,7.1,6.4,6.1,5.9,5.9,5.9,5.8,5.6,5.4,5.2,5.1,5,5,5,5,4.9,4.8]

while True:
    a89 = int(input("Enter between 1 - 49: "))
    if a89 == 0:
        print("Please enter a valid value between 1 to 49")
        continue
    elif a89 >= 49:
        print("Sorry I have range of 49 only , I think I was too confident about having 49 movies data")
        continue
    else:
        print("Ok , So the list is Printing Top",a89,"Movies")
        time.sleep(0.5)
        print("If you want gross figures to be printed with them Press 1")
        time.sleep(0.5)
        print("Else Press 2")
        time.sleep(0.5)
        while True:
            a090 = int(input("Please Enter 1 or 2: "))
            if a090 == 1:
                for i in range(a89):
                    print((i+1),".",li[i],"-->",li2[i]," Billion")
                    time.sleep(0.5)
                break
            elif a090 == 2:
                for i in range(a89):
                    print((i+1),".",li[i])
                    time.sleep(0.5)
                break
            else:
                print("Please Enter 1 or 2")
                time.sleep(0.5)
                continue
        break
    

print('So here is the List you wanted')
time.sleep(0.5)
print("If you want to know the Source Site of the info Then Press 1")
time.sleep(0.5)
print("If you want to exit the application Then Press 2")
time.sleep(0.5)

while True:
    a567 = int(input("Press between 1 to 2: "))
    if a567 == 2:
        import exitapplication
        import exitapplication
        break
    elif a567 == 1:
        print("Redirecting to the site")
        time.sleep(0.5)
        import webbrowser
        webbrowser.open("https://www.youtube.com/watch?v=hcWfHyeoaBw") 
        continue
    else:
        print("I think You mistakenly press the wrong key , Its Okay I will Ask you Again")
        time.sleep(0.5)
        print("If you want to know the Source Site of the info Then Press 1")
        time.sleep(0.5)
        print("If you want to exit the application Then Press 2")
        time.sleep(0.5)
        continue