import time

print("Oh my God,  I have list of Total 50 Highest Grossing movies in India How Much you want")
time.sleep(2)

li = ["Dangal","Baahubali 2: The Conclusion","K.G.F. Chapter 2","RRR","Secret Superstar","Bajrangi Bhaijaan","PK","2.0","Sultan","Dhom 3","Sanju","Padmaavat","Baahubali: The Beginning","Tiger Zinda Hai","War","3 Idiosts","Andhadhun","Ponniyan Selvan: I","Prem Ratan Dhan Payo","Brahmastra Part One: Shiva","Chennai Express","Vikram","Saaho","Kick","Kantara","Simmba","Happy New Year","Krrish 3","Kabir Singh","Dilwale","Tanhaji: The Unsung Warrior","URI: The Surgical Strike","Bajirao Mastani","Pushpa: The Rise","The Kashmir Files","Bang Bang!","Thugs of Hindostan","Ek tha Tiger","Bharat","Hindi Medium","Yeh Jawaani Hai Deewani","Good Newwz","Toliet: Ek Prem Katha","Golmaal Again","Raees","Race 3","Kabali","Houseful 4","Sooryavanshi","Mission Mangal"]

liearn = [2024,1810,1200,1200,977,969.06,854,625,623.33,589.2,586.85,585,581,565,495.50,475.5,460,456.89,432,431,424.54,420,419,402,400,397.21,397,393.37,379,376.85,367.65,359.73,358,355,340.92,340,335,334.39,325.58,323.3,319.6,318.57,311.5,311.05,308.88,306.55,305.16,300,396,294.17]

while True:
    a56 = int(input("Enter between 1 - 50: "))
    if a56 == 0:
        print("Please enter a valid value between 1 to 50")
        continue
    elif a56 >= 51:
        print("Sorry I have range of 50 only , I think I was too confident about having 50 movies data")
        continue
    else:
        print("Ok , So the list is Printing Top",a56,"Movies")
        time.sleep(0.5)
        for i in range(a56):
            print((i+1),".",li[i],"-->",liearn[i])
            time.sleep(0.5)
        break

print('So here is the List you wanted')
time.sleep(0.5)

print("If you want To know the Movies Currently Running in theatres from this list Press 1")
time.sleep(0.5)

print("If you want To know the Movies Recently Got there place in this list Press 2")
time.sleep(0.5)

print("If you want to know the Source Site of the info Then Press 3")
time.sleep(0.5)
print("If you want to exit the application Then Press 4")
time.sleep(0.5)

while True:
    a567 = int(input("Press between 1 to 4: "))
    if a567 == 4:
        import exitapplication
        import exitapplication
        break
    elif a567 == 3:
        print("Redirecting to the site")
        time.sleep(0.5)
        import webbrowser
        webbrowser.open("https://en.wikipedia.org/wiki/List_of_highest-grossing_Indian_films")
        continue 
    elif a567 == 1:
        print("Printing Running Movies in Cinemas right now")
        time.sleep(0.5)
        print(li[3])
        time.sleep(0.5)
        continue
    elif a567 == 2:
        print("Printing New Enteries of this list")
        time.sleep(0.5)
        print(li[2],"Released in 2022")
        time.sleep(0.5)
        print(li[3],"Released in 2022")
        time.sleep(0.5)
        print(li[17],"Released in 2022")
        time.sleep(0.5)
        print(li[19],"Released in 2021")
        time.sleep(0.5)
        print(li[21],"Released in 2022")
        time.sleep(0.5)
        print(li[24],"Released in 2022")
        time.sleep(0.5)
        print(li[34],"Released in 2022")
        time.sleep(0.5)
        print(li[33],"Released in 2021")
        time.sleep(0.5)
        print(li[48],"Released in 2021")
        time.sleep(0.5)
        continue
    break