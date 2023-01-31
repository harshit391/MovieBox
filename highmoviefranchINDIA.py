import time

li0 = ["Baahubali","K.G.F","Spy Universe","Cop Universe","Robot","Housefull","Dhoom","Dabangg","Golmaal","Koi.. Mil Gaya","Race","Loki Universe","Baaghi","Ponniyin Selvan","Brahmastra Part One: Shiva","Drishyam","Pushpa","The Files","Dhamaal","Bhool Bhulaiyaa","Medium","Kanchana","Don","Tanu Weds Manu","Sharma ki Dulhaniya","Dinesh Horror Universe"]

li1 = [2,2,5,5,2,5,3,3,5,5,3,4,4,2,3,2,2,3,3,2,2,4,3,2,2,3]

li2 = [2349.60,1454.40,1360.60,1050.36,942.30,796,780.63,700.93,648.95,598.97,570,527.40,518.34,500.80,417.20,388.64,369.90,360.33,353.43,341.41,336.84,333.70,328.2,311.3,310.34,283.69]

li3 = ["Baahubali 2: The Conclusion","K.G.F Chapter: 2","Tiger Zinda Hai","Simmba","2.0","Housefull 4","Dhoom 3","Dabangg 3","Golmaal Again","Krrish 3","Race 3","Vikram","Baaghi 2","Ponniyin Selvan: Part 1","Brahmastra Part One: Shiva","Drishyam 2","Pushpa: The Rise","The Kashmir Files","Total Dhamaal","Bhool Bhulaiyaa 2","Hindi Medium","Kanchana 3","Don 2","Tanu Weds Manu Returns","Badrinath Ki Dulhaniya","Stree"]

li4 = ["Baahubali 2: The Conclusion","K.G.F Chapter: 2","Tiger Zinda Hai","Simmba","2.0","Housefull 4","Dhoom 3","Dabangg 3","Golmaal Again","Krrish 3","Race 3","Vikram","Baaghi 3","Ponniyin Selvan: Part 1","Brahmastra Part One: Shiva","Drishyam 2","Pushpa: The Rise","The Kashmir Files","Total Dhamaal","Bhool Bhulaiyaa 2","Angrezi Medium","Kanchana 3","Don 2","Tanu Weds Manu Returns","Badrinath Ki Dulhaniya","Bhediya"]

li=[]

print("Okkaayy .. I have 26 Different Franchices So How much You want")
while True:
    a456 = int(input("Please Enter between (1-26): "))
    if a456==0:
        print("Sorry , O is not valid")
        time.sleep(0.5)
        continue
    elif a456 > 26:
        print("Sorry I don't have enough range")
        time.sleep(0.5)
        continue
    else:
        print("Printing Top",a456,"Movie Franchises")
        time.sleep(0.5)
        print("But There ! you can customize as your wish , Just Press the Assigned the Numbers")
        time.sleep(0.5)
        print("Customize means which data you want only that is printed")
        time.sleep(0.5)
        print("If you want to know How Many Movies are in the Franchise Then Press 1")
        time.sleep(0.5)
        print("If you want to know the Gross Figures earned by Franchise Then Press 2")
        time.sleep(0.5)
        print("If you want to know the highest grossing movie in that franchise then press 3")
        time.sleep(0.5)
        print("If you want to know the Recent Entry in the Franchise Then Press 4")
        time.sleep(0.5)
        while True:
            a8904 = int(input("How Many Customizations you want: "))
            if a8904 == 0:
                print("Since No Customization is Choosen So Only Names will be Printed")
                time.sleep(0.5)
                for i in range(a456):
                    print(i+1,".",li0[i])
                    time.sleep(0.5)            
                break
            elif a8904 > 5:
                print("Sorry I have only 4 customizations , Printing below again")
                time.sleep(0.5)
                print("If you want to know How Many Movies are in the Franchise Then Press 1")
                time.sleep(0.5)
                print("If you want to know the Gross Figures earned by Franchise Then Press 2")
                time.sleep(0.5)
                print("If you want to know the highest grossing movie in that franchise then press 3")
                time.sleep(0.5)
                print("If you want to know the Recent Entry in the Franchise Then Press 4")
                time.sleep(0.5)
                continue
            elif a8904 == 4:
                print("Printing List with All 4 Customizations")
                time.sleep(1)
                print(["Name of the Franchise","Gross Figures Earned","Highest Grosser","Recent Entry"])
                print()
                time.sleep(0.5)
                for i in range(a456):
                    print(i+1,'.',li0[i],"-->",li1[i],"Movies","-->",li2[i],"Crores","-->",li3[i],"-->",li4[i])
                    time.sleep(0.5)
                break
            else:
                print("Okay So you want",a8904,"customizations")
                time.sleep(0.5)
                for k in range(a8904):
                    li.append(int(input("Enter the assigned number to the customization you want: ")))
                li = set(li)
                while True:
                    if li == {1}:
                        print(["Name of the Franchise","No. of Movies"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,".",li0[i],"-->",li1[i],"Movies")
                            time.sleep(0.5)
                        break
                    elif li == {2}:
                        print(["Name of the Franchise","Gross Figures Earned"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,".",li0[i],"-->",li2[i],"Crores")
                            time.sleep(0.5)
                        break
                    elif li == {3}:
                        print(["Name of the Franchise","Highest Grosser"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,".",li0[i],"-->",li3[i])
                            time.sleep(0.5)
                        break
                    elif li =={4}:
                        print(["Name of the Franchise","Recent Entry"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,".",li0[i],"-->",li4[i])
                            time.sleep(0.5)
                        break
                    elif li=={1,2}:
                        print(["Name of the Franchise","No. of Movies","Gross Figures Earned"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,'.',li0[i],"-->",li1[i],"Movies","-->",li2[i],"Crores")
                            time.sleep(0.5)
                        break
                    elif li=={2,3}:
                        print(["Name of the Franchise","Gross Figures Earned","Highest Grosser"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,'.',li0[i],"-->",li2[i],"Crores","-->",li3[i])
                            time.sleep(0.5)
                        break
                    elif li=={2,4}:
                        print(["Name of the Franchise","Gross Figures Earned","Recent Entry"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,'.',li0[i],"-->",li2[i],"Crores","-->",li4[i])
                            time.sleep(0.5)
                        break
                    elif li=={1,3}:
                        print(["Name of the Franchise","No. of Movies","Highest Grosser"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,'.',li0[i],"-->",li1[i],"Movies","-->",li3[i])
                            time.sleep(0.5)
                        break
                    elif li=={1,4}:
                        print(["Name of the Franchise","No. of Movies","Recent Entry"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,'.',li0[i],"-->",li1[i],"Movies","-->",li4[i])
                            time.sleep(0.5)
                        break
                    elif li=={3,4}:
                        print(["Name of the Franchise","Highest Grosser","Recent Entry"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,'.',li0[i],"-->",li3[i],"-->",li4[i])
                            time.sleep(0.5)
                        break
                    elif li=={1,2,3}:
                        print(["Name of the Franchise","No. of Movies","Gross Figures Earned","Highest Grosser"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,'.',li0[i],"-->",li1[i],"Movies","-->",li2[i],"Crores","-->",li3[i])
                            time.sleep(0.5)
                        break
                    elif li=={4,2,3}:
                        print(["Name of the Franchise","Gross Figures Earned","Highest Grosser","Recent Entry"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,'.',li0[i],"-->",li2[i],"Crores","-->",li3[i],"-->",li4[i])
                            time.sleep(0.5)
                        break
                    elif li=={1,2,4}:
                        print(["Name of the Franchise","No. of Movies","Gross Figures Earned","Recent Entry"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,'.',li0[i],"-->",li1[i],"Movies","-->",li2[i],"Crores","-->",li4[i])
                            time.sleep(0.5)
                        break
                    elif li=={1,4,3}:
                        print(["Name of the Franchise","Highest Grosser","Recent Entry"])
                        print()
                        time.sleep(0.5)
                        for i in range(a456):
                            print(i+1,'.',li0[i],"-->",li1[i],"Movies","-->",li3[i],"-->",li4[i])
                            time.sleep(0.5)
                        break
                break
        break

print("So Here is the List you wanted")
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
        webbrowser.open("https://www.imdb.com/list/ls041952416/") 
        continue
    else:
        print("I think You mistakenly press the wrong key , Its Okay I will Ask you Again")
        time.sleep(0.5)
        print("If you want to know the Source Site of the info Then Press 1")
        time.sleep(0.5)
        print("If you want to exit the application Then Press 2")
        time.sleep(0.5)
        continue