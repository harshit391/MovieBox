import time

li0=["Marvel Cinematic Universe","Star Wars","Spider-Man","Wizarding World","James Bond","Avenegrs","Batman","Fast and Furious","DC Extended Universe","X-Men","Jurassic Park","Middle-earth","Transformers","Despicable Me","Pirates of the Caribbean","Mission: Impossible","Shrek","The Twilight Saga","Toy Story","Ice Age","The Hunger Games","Frozen","Thor","The Lion King","Godzilla"]

li1=[30,12,12,11,27,4,17,10,11,13,6,7,7,5,5,6,5,5,5,5,4,2,4,3,36]

li2=[27.981,10.317,9.804,9.667,7.832,7.767,6.841,6.620,6.192,6.085,6.003,5.953,4.853,4.645,4.524,3.570,3.510,3.346,3.269,3.217,2.968,2.740,2.709,2.625,2.569]

li3=["Avengers Endgame: 2.797 Billion","The Force Awakens: 2.068 Billion","No Way Home: 1.916 Billion","Harry potter and the Deathly Hollows Part 2: 1.342 Billion","Sky Fall: 1.108 Billion","Endgame: 2.797 Billion","The Dark Knight Rises: 1.081 Billion","Furious 7: 1.516 Billion","Aquaman: 1.148 Billion","Deadpool 2: 785 Million","Jurassic World: 1.671 Billion","The Lord of the Rings - The Return of the Kings: 1.146 Billion","Dark of the Moon: 1.123 Billion","Minions: 1.159 Billion","Dead's Men Chest: 1.066 Billion","Fallout: 791 Million","Shrek 2: 919 Million","Breaking Down Part 2: 829 Million","Toy Story 4: 1.073 Billion","Dawn of the Dinosaurs: 886 Million","Caching Fire: 865 Million","Frozen II: 1.450 Million","Ragnarok: 853 Million","The Lion King: 1.656 Billion","Godzilla: 529 Million"]

li4=["Black Panther 2 - Wakanda Forever","The Rise of Sky Walker","No Way Home","The Secrets of DumbleDore","No Time to Die","Endgame","The Batman","F9","Black Adam","The New Mutants","Jurassic World Dominion","The Hobbit: The Battle of the Five Armies","BumbleBee","Minions: The Rise of Gru","Dead Men Tell No Tales","Mission: Impossible - Fallout","Puss in Boots: The Last Wish","Breaking Dawn - Part 2","Light Year","Ice Age: Collision Cource","The Hunger Games: Mockingjay Part 2","Frozen II","Thor: Love and Thunder","Black is King","Godzilla vs. Kong"]

li=[]

print("Okkaayy .. I have 25 Different Franchices So How much You want")
while True:
    a456 = int(input("Please Enter between (1-25): "))
    if a456==0:
        print("Sorry , O is not valid")
        time.sleep(0.5)
        continue
    elif a456 > 25:
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
        webbrowser.open("https://en.wikipedia.org/wiki/List_of_highest-grossing_films#Highest-grossing_franchises_and_film_series") 
        continue
    else:
        print("I think You mistakenly press the wrong key , Its Okay I will Ask you Again")
        time.sleep(0.5)
        print("If you want to know the Source Site of the info Then Press 1")
        time.sleep(0.5)
        print("If you want to exit the application Then Press 2")
        time.sleep(0.5)
        continue