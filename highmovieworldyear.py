import time

print("Oh my God, I have list of Highest Grossing movies By Year from 1915 to 2022 , How Much you want")
time.sleep(0.5)

li = ["1915. The Birth of a nation - 50 million","1916. Intolerance - 1 Million","1917. Cleopatra - 500 Thousand","1918 . Mickey - 8 Million","1919. The Miracle Man - 3 Million","1920. Way Down East - 5 Million","1921. The Four Horseman of Apocalypse - 5 Million","1922. Douglas Fairbanks in Robin Hood - 2.5 Million","1923. The Covered Wagon - 5 Million","1924. The Seas Hawk - 3 Million","1925. The Big Parade - 19 Million","1926. For Heaven’s Sake - 2.6 Million","1927. Wings - 3.6 Million","1928. The Singing Fool - 5.9 Million","1929. The Broadway Melody - 4.4 Million","1930. All Quiet on the Western front - 3 Million","1931. Frankenstein - 12 Million","1932. The Sign of the Cross - 2.7 Million","1933. King Kong - 5.3 Million","1934. The Merry Widow - 2.6 Million","1935. Mutiny on the Bounty - 4.4 million","1936. San Francisco - 6 Million","1937. Snow White and the Seven Dwarfs - 418 Million","1938. You Can’t Take it with you - 5 Million","1939. Gone with the Wind - 400 Million","1940. Pinocchio - 87 Million","1941. Sergeant York - 7.8 Million","1942. Bambi - 268 Million","1943. For Whom the Bell Tolls - 11 Million","1944. Going my way - 6.5 Million","1945.  Mom and Dad - 80 Million","1946. Song of the South - 65 Million","1947. Forever Amber - 8 Million","1948. Easter Parade - 5.9 Million","1949. Samson and Delilah - 14 Million","1950. Cinderella - 263 Million","1951. Quo Vadis - 21 Million","1952. This is Cinerama - 50 Million","1953. Peter Pan - 145 Million","1954. Rear Window - 24.5 Million","1955. Lady and the Tramp - 187 Million","1956. The Ten Commandments - 90 Million","1957. The Bridge on the River Kwai - 30.6 Million","1958. South Pacific - 30 Million","1959. Ben-Hur - 90 Million","1960. Swiss Family Robinson - 30 Million","1961. One Hundred and One Dalmatians - 303 Million","1962. Lawrence of Arabia - 77 Million","1963. Cleopatra - 40.3 Million","1964. My Fair Lady - 55 Million","1965. The Sound of Music - 286 Million","1966. The Bible: In the Beginning - 25 Million","1967. The Jungle Book - 378 Million","1968. 2001: A Space Odyssey - 141 Million","1969. Butch Cassidy and the Sundance Kid - 152 Million","1970. Love Story - 173 Million","1971. The French Connection - 75 Million","1972. The Godfather - 246 Million","1973. The Exorcist - 413 Million","1974. The Towering Inferno - 203 Million","1975. Jaws - 476 Million","1976. Rocky - 225 Million","1977. Star Wars - 775 Million","1978. grease - 400 Million","1979. Moonraker - 210 Million","1980. The Empire Strikes Back - 547 Million","1981. raiders of the Lost Ark - 389 Million","1982. E.T. the Extra Terrestrial - 797 Million","1983. Return of the Jedi - 475 Million","1984. Indiana Jones and the Temple of Doom - 333 Million","1985. Back to the Future - 389 Million","1986. Top Gun - 356 Million","1987. fatal Attraction - 320 Million","1988. Rain Man - 354 Million","1989. Indiana Jones and the Last Crusade - 474 Million","1990. Ghost - 505 Million","1991. Terminator 2 - Judgement Day - 523 Million","1992. Aladdin - 504 Million","1993. Jurassic Park - 1.034 Billion","1994. The Lion King - 968 Million","1995. Toy Story - 373 Million","1996. Independence Day - 817 Million","1997. Titanic - 2.187 Billion","1998. Armageddon - 553 Million","1999. Star Wars: Episode I - The Phantom Menace - 1.027 Billion","2000. Mission Impossible 2 - 546 Million","2001. Harry Potter and the Philosopher’s Stone - 1.006 Billion","2002. The Lord of the Rings: The Two Towers - 947 Million","2003. The Lord of the Rings: The Return of the King - 1.146 Billiom","2004. Shrek 2 - 919 Million","2005. Harry Potter and the Goblet of Fire - 896 Million","2006. Pirates of the Caribbean: Dead Man’s Chest - 1.066 Billion","2007. Pirates of the Caribbean: At World’s End - 963 Million","2008. The Dark Knight - 1.006 Billion","2009. Avatar - 2.922 Billion","2010. Toy Story 3 - 1.066 Billion","2011. Harry Potter and the Deathly Hollows Part 2 - 1.342 Billion","2012. The Avengers - 1.518 Billion","2013. Frozen - 1.290 Billion","2014. Transformers: Age of Extinction - 1.104 Billion","2015. Star Wars: The Force Awakens - 2.068 Billion","2016. Captain America: Civil War - 1.153 Billion","2017. Star Wars: The last Jedi - 1.332 Billion","2018. Avengers: Infinity War - 2.048 Billion","2019. Avengers: End Game - 2.797 Billion","2020. Demon Slayer: Mugen Train - 506 Million","2021. Spider Man: No Way Home - 1.916 Billion","2022. Top Gun: Maverick - 1.486 Billion"]
while True:
    styea = int(input("Which Year you want the list Start from: "))
    endyea = int(input("Which Year you want the list End at: "))
    if styea < 1915:
        print("I had never gone too old yet So could you enter after 1915")
        continue
    elif endyea >= 2023:
        print("Actually 2022 is the current year So I have no data for Year after 2022")
        continue
    if endyea < 1915:
        print("Sorry I can't able to print list backward yet")
        continue
    elif styea >= 2023:
        print("Actually 2022 is the current year So I have no data for Year after 2022")
        continue
    else:
        print("Ok , So the list is Printing Movies from year",styea,"to year",endyea)
        s=styea-1915
        for i in range((endyea-styea)+1):
            print(li[s])
            s=s+1
            time.sleep(0.5)
        break
print('So here is the List you wanted')
time.sleep(0.5)
print("If you want To know the Movies Currently Running in theatres from this list Press 1")
time.sleep(0.5)
print("If you want to know the Source Site of the info Then Press 2")
time.sleep(0.5)
print("If you want to exit the application Then Press 3")
time.sleep(0.5)

while True:
    a567 = int(input("Press between 1 to 3: "))
    if a567 == 3:
        import exitapplication
        import exitapplication
        break
    elif a567 == 2:
        print("Redirecting to the site")
        time.sleep(0.5)
        import webbrowser
        webbrowser.open("https://en.wikipedia.org/wiki/List_of_highest-grossing_films#High-grossing_films_by_year") 
        continue
    elif a567 == 1:
        print("Printing Running Movies in Cinemas right now")
        time.sleep(0.5)
        print(li[94])
        time.sleep(0.5)
        print(li[106])
        time.sleep(0.5)
        print(li[107])
        time.sleep(0.5)
        continue
    else:
        print("I think You mistakenly press the wrong key , Its Okay I will Ask you Again")
        time.sleep(0.5)
        print("If you want To know the Movies Currently Running in theatres from this list Press 1")
        time.sleep(0.5)
        print("If you want to know the Source Site of the info Then Press 2")
        time.sleep(0.5)
        print("If you want to exit the application Then Press 3")
        time.sleep(0.5)
        continue