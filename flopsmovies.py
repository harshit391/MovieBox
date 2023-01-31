import time

lin = ["The 355","Amsterdam","Moonfall","Turning Red","Lightyear","Snake Eyes: G.I. Joe Origins","Chaos Walking","The Last Duel","west Side Story","Space Jam: A New Legacy","The Suiicide Squad","The Matrix Ressuractions","Jungle Cruis","The New Mutants","The Call of the Wild","Dolittle","Onward","Mulan","Tenet","Wonder Woman 1984","Cats","Missing Link","Gemini Man","Terminator: Dark Fate","Dark Phoenix","Robin Hood","Mortal Engines","A Wrinkle in Time","King Arthur: Legend of the Sword","Valerian and the City of the Thousand Planets","Blade Runner 2049","The Mummy","Transfomers: The Last Knight","Live by Night","the Finest Hours","Allied","The Promise","Ben-Hur","The Huntsman: Winter's war","Deepwater Horizon","Monster Trucks","Teenage Mutant Ninja Turtles: Out of the Shadows","The BFG","Gods of Egypt","Ghostbusters","The Great Wall","Black Hat","The man from U.N.C.L.E.","Pixels","Seventh Son","Fantastic Four","Pan","Jupiter Ascending","Tommorow Land","The Good Dinasaur","R.I.P.D.","Jack and the Giant Slayer","47 Ronin","The Lone Ranger","Rise of the Guardians","Battleship","John Carter","Mars Needs Moms","Hugo","Green Lantren","How do you Know","The Wolfman","The Nutcracker in 3D","A Cristmas Carol","Speed Racer","The Invasion","Even Almighty","Zoom","Poseidon","The Great Raid","A Sound of thunder","XXX: State of the Union","Stealth","Sahara","The Alamo","Around the World in 80 Days","The Chronicles of Riddick","Alexander","Sinbad: The Legend of the Seven Seas","Gigil","Peter Pan","Ballistic: Ecks vs Sever","Harts's War","The Adventures of Pluto Nash","K-19: The Widowmaker","Windtalkers","Treasure Planet","Osmosis Jones","Monkeybone","Town and Country","Driven","Ali","Final Fantasy: The Spirits Within","Red Planet","Titan A.E.","Supermova","The Adventures of Rocky and Bullwinkle","Battlefield Earth","Chill Factor","Dudley Do-right","The Astronaut's Wife","Instict","The 13th Warrior","Hard Rain","Soldier","Sphere","Beloved","Jack Frost","Lolita","The Postman","Father's Day"]

lib = [75,80,138,175,200,110,100,100,100,150,185,190,200,80,150,175,200,200,200,200,100,102.3,138,196,200,100,110,125,175,180,185,195,217,65,80,85,90,100,115,120,125,135,140,140,144,150,70,75,88,95,125,150,175,190,200,154,200,225,250,145,220,263.7,150,170,200,100,150,100,200,120,80,175,75.6,160,80,80,113.1,135,160,107,110,120,155,60,75.6,130.6,70,95,100,100,120,140,70,75,90,94,107,137,80,90,90,98.6,103,70,70,75,80,160,70,75,80,80,85,62,80,85]

lic = [27.7,29.9,44.3,19.8,226.4,40.1,26.5,30.6,76,162.9,167.4,156.5,220.9,49.2,107.6,227.9,142,66.8,363.7,166.5,73.7,26.2,173.5,261.1,252.4,85.7,83.7,133.4,148.7,225.9,260.5,410,605.4,22.3,52.1,118.6,10.6,94.1,165,119.5,64.5,245.6,179.6,150.7,229.1,332,19.7,109.8,244.9,114.2,168,128.4,184,209,332.2,78.3,197.7,151.8,260.5,306.9,303,284.1,39,185.8,219.9,48.7,139.8,20.5,325.3,93.9,40,173.4,12.5,181.7,10.8,11.7,71,79.3,119.2,25.8,72.2,115.8,167.3,80.8,7.3,122,19.9,32.3,7.1,65.7,77.6,109.6,14,7.6,10.4,54.7,87.7,85.1,33.5,36.8,14.8,35.1,29.7,11.8,10,19.6,34.1,61.7,19.9,14.6,50.2,22.9,34.6,1.1,20.8,35.7]

print("So , I have data from Year 1997 to Year 2022")
time.sleep(0.5)
print("You want to know the flop movies from which movie")
time.sleep(0.5)
print("Please Take this in consideration that movie is not flop due to loss only")
time.sleep(0.5)
print("It will also because of audience reviews")
time.sleep(0.5)

def iploop(a,s,m):
    print("Printing flop movies from",a)
    time.sleep(0.5)
    li89 = ["Name of the Movie","Budget in Million","Earnings in Million"]
    print(li89)
    print()
    time.sleep(0.5)
    for i in range(s,m):
        li567=[]
        li567.append(lin[i])
        li567.append(lib[i])
        li567.append(lic[i])
        print(li567)
        time.sleep(0.5)
    return "Here is your list"
    
while True:
    a7896 = int(input("Please Enter between 1997 to 2022: "))
    if a7896 > 2022:
        print("Sorry Current Year is 2022 So I Have Data till this year only")
        continue
    elif a7896 < 1997:
        print("Actually before 1997 My data was not too perfect to show So I Cut it off for better")
        continue
    else:
        if a7896 == 1997:
            print(iploop(a=a7896,s=113,m=116))
            break
        elif a7896 == 1998:
            print(iploop(a=a7896,s=108,m=113))
            break
        elif a7896 == 1999:
            print(iploop(a=a7896,s=103,m=108))
            break
        elif a7896 == 2000:
            print(iploop(a=a7896,s=98,m=103))
            break
        elif a7896 == 2001:
            print(iploop(a=a7896,s=92,m=98))
            break
        elif a7896 == 2002:
            print(iploop(a=a7896,s=86,m=92))
            break
        elif a7896 == 2003:
            print(iploop(a=a7896,s=83,m=86))
            break
        elif a7896 == 2004:
            print(iploop(a=a7896,s=79,m=83))
            break
        elif a7896 == 2005:
            print(iploop(a=a7896,s=74,m=79))
            break
        elif a7896 == 2006:
            print(iploop(a=a7896,s=72,m=74))
            break
        elif a7896 == 2007:
            print(iploop(a=a7896,s=70,m=72))
            break
        elif a7896 == 2008:
            print(iploop(a=a7896,s=69,m=70))
            break
        elif a7896 == 2009:
            print(iploop(a=a7896,s=68,m=69))
            break
        elif a7896 == 2010:
            print(iploop(a=a7896,s=65,m=68))
            break
        elif a7896 == 2011:
            print(iploop(a=a7896,s=62,m=65))
            break
        elif a7896 == 2012:
            print(iploop(a=a7896,s=59,m=62))
            break
        elif a7896 == 2013:
            print(iploop(a=a7896,s=55,m=59))
            break
        elif a7896 == 2014:
            print("Printing flop movies from 2014")
            time.sleep(0.5)
            print("Oops , Sorry! I have no data for 2014 ,Could you please try any other year")
            continue
        elif a7896 == 2015:
            print(iploop(a=a7896,s=46,m=55))
            break
        elif a7896 == 2016:
            print(iploop(a=a7896,s=33,m=46))
            break
        elif a7896 == 2017:
            print(iploop(a=a7896,s=28,m=33))
            break
        elif a7896 == 2018:
            print(iploop(a=a7896,s=25,m=28))
            break
        elif a7896 == 2019:
            print(iploop(a=a7896,s=20,m=25))
            break
        elif a7896 == 2020:
            print(iploop(a=a7896,s=13,m=20))
            break
        elif a7896 == 2021:
            print(iploop(a=a7896,s=5,m=13))
            break
        elif a7896 == 2022:
            print(iploop(a=a7896,s=0,m=5))
            break
    break


print("If you want to know the Source Site of the info Then Press 1")
time.sleep(0.5)
print("If you want to exit the application Then Press 2")
time.sleep(0.5)

while True:
    a567 = int(input("Press between 1 to 2: "))
    if a567 == 1:
        print("Redirecting to the site")
        time.sleep(0.5)
        import webbrowser
        webbrowser.open("https://en.wikipedia.org/wiki/List_of_biggest_box-office_bombs#Biggest_box_office_bombs")
        continue 
    elif a567 == 2:
        import exitapplication
        import exitapplication
        break
    else:
        print("I think You mistakenly press the wrong key , Its Okay I will Ask you Again")
        time.sleep(0.5)
        print("If you want to know the Source Site of the info Then Press 1")
        time.sleep(0.5)
        print("If you want to exit the application Then Press 2")
        time.sleep(0.5)
        continue