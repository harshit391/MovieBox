import time

print("Oh my God,  I have list of Total 50 Highest Grossing movies How Much you want")
time.sleep(2)
li = ["Avatar - 2.922 billion","Avengers Endgame - 2.797 billion","Titanic - 2.187 billion","Star Wars: The Force Awakens - 2.068 billion","Avengers: Infinity war - 2.048 billion","Spider Man No Way Home - 1.916 billion","Jurassic World - 1.671 billion",'The Lion King - 1.656 billion','The Avengers - 1.518 billion',"Furious 7 - 1.516 billion","Top Gun: Maverick - 1.486 billion","Frozen II - 1.450 billion","Avengers: Age of Ultron - 1.402 billion","Black Panther - 1.347 billion","Harry Potter and the Deathly Hollows - Part 2 - 1.342 billion","Star Wars: The Last Jedi - 1.332 billion","Jurassic World: Fallen Kingdom - 1.309 billion","Frozen - 1.290 billion","Beauty and the Beast - 1.263 billion","Incredibles 2 - 1.242 billion","The Fate of Furious - 1.238 billion","Iron Man 3 - 1.214 billion","Minions - 1.159 billion","Captain America: Civil War - 1.153 billion","Aquaman - 1.148 billion","The Lord of the Rings: The Return of the King - 1.146 billion","Spider Man: Far from Home - 1.131 billion","Captain Marvel - 1.128 billion","Transformers: Dark of the Moon - 1.123 billion","Skyfall - 1.108 billion","Transformers: Age of Extinction - 1.104 billion","The Dark Knight Rises - 1.081 billion","Joker - 1.074 billion","Star Wars: The Rise of Skywalker - 1.074 billion","Toy Story 4 - 1.073 billion","Toy Story 3 - 1.067 billion","Pirates of the Caribbean: Dead Man's Chest - 1.066 billion","Rogue One: A Star Wars Story - 1.057 billion","Aladdin - 1.050 billion","Pirates of the Caribbean: On Stranger Tides - 1.045 billion","Despicable Me 3 - 1.035 billion","Jurassic Park - 1.034 billion","Finding Dory - 1.028 billion","Star Wars: Episode I - The Phantom Menace - 1.027 billion","Alice in Wonderland - 1.025 billion","Zootopia - 1.023 billion","The Hobbit: An Unexpected Journey - 1.017 billion","Harry Potter and the Philosopher's Stone - 1.007 billion","The Dark Knight - 1.006 billion","Jurassic World Dominion - 1.001 billion"]
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
        for i in range(a56):
            print((i+1),".",li[i])
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
        webbrowser.open("https://en.wikipedia.org/wiki/List_of_highest-grossing_films#Highest-grossing_films")
        continue 
    elif a567 == 1:
        print("Printing Running Movies in Cinemas right now")
        time.sleep(0.5)
        print(li[0])
        time.sleep(0.5)
        print(li[5])
        time.sleep(0.5)
        print(li[10])
        time.sleep(0.5)
        print(li[49])
        time.sleep(0.5)
        continue
    elif a567 == 2:
        print("Printing New Enteries of this list")
        time.sleep(0.5)
        print(li[5],"Released in 2021")
        time.sleep(0.5)
        print(li[10],"Released in 2022")
        time.sleep(0.5)
        print(li[49],"Released in 2022")
        time.sleep(0.5)
        continue
    break