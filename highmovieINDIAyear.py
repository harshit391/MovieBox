import time

print("Oh my God, I have list of Highest Grossing movies By Year from 1940 to 2022 , How Much you want")
time.sleep(0.5)

liyear = ["Zindagi","Khazanchi","Basant","Kismet","Rattan","Zeenat","Anmol Ghadi","Jugnu","Chandralekha","Barsaat","Samadhi","Awaara","Aan","Anarkali","Nagin","Pather Panchali","Jagte Raho","Mother India","Madhumati","Char Dil Char Rahen","Mughal-e-Azam","Ganga Jamna","Bees Saal Baad","Mere Mehboob","Sangam","Waqt","Phool Aur Patthar","Hamraaz","Ankhen","Aradhana","Mera Naam Joker","Caravan","Seeta aur Geeta","Bobby","Roti Kapda aur Makaan","Sholay","Barood","Amar Akbar Anthony","Muqaddar Ka Sikandar","Suhaag","Adventures of Ali-Baba and the Forty Theives","Kranti","Disco Dancer","Coolie","Jagir","Ram Teri Ganga Maili","Karma","Hukumar","Tezaab","Maine Pyar Kiya","Dil","Saajan","Beta","Aankhen","Hum Aapke Hain Koun..!","Dilwale Dulhania Le Jayenge","Raja Hindustani","Dil to Pagal Hai","Kuch Kuch Hota Hai","Hum Saath Saath Hain","Mohabbatein","Kabhi Khushi Kabhi Gham..","DevDas","Kal Ho Naa Ho","Veer-Zara","No Entry","Dhoom 2","Om Shanti Om","Ghajini","3 Idiots","Enthiran","Bodyguard","Ek tha Tiger","Dhoom 3","PK","Bajrangi Bhaijaan","Dangal","Baahubali 2: The Conclusion","2.0","War","Tanhaji: The Unsung Warrior","Pushpa: The Rise","RRR"]

liyearearnings=[0.55,0.70,0.80,1,1,0.70,1,0.50,1.55,2,1.35,15.61,3.57,2.35,2.9,10,4.44,8,4,5.27,11,11,3,6,8,6,17,13.33,6.5,17.85,16.81,35.3,19.53,30,10.5,58,19.32,15.5,26,10,22.11,20,100.7,18,35.32,19,14,11,16,28,18,18,23.5,25.25,200,87.5,71.87,106.74,81.71,90.01,135.53,168,86.09,97.64,74.13,151.39,149.87,232,459.96,289,234,334.39,589.2,832,969.06,2024,1810,800,475,368,365,1500]

while True:
    startyear = int(input("Enter Start year of list: "))
    if startyear<1940:
        print("Sorry I have data onwards 1940 year only")
        time.sleep(0.5)
        continue
    else:
        endyear = int(input("Enter the end year of the list: "))
        if endyear>2022:
            print("Sorry 2022 is the current year , I have no data afterwards")
            continue
        else:
            print("Printing List from year",startyear,"to year",endyear)
            time.sleep(0.5)
            s = startyear
            d = 2022-startyear
            e = 82-d
            for i in range((endyear-startyear)+1):
                print(s,".",liyear[e],"-->",liyearearnings[e],"Crores")
                e=e+1
                s=s+1
                time.sleep(0.5)
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
        webbrowser.open("https://en.wikipedia.org/wiki/List_of_highest-grossing_Indian_films#Highest-grossing_films_by_year") 
        continue
    else:
        print("I think You mistakenly press the wrong key , Its Okay I will Ask you Again")
        time.sleep(0.5)
        print("If you want to know the Source Site of the info Then Press 1")
        time.sleep(0.5)
        print("If you want to exit the application Then Press 2")
        time.sleep(0.5)
        continue