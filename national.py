import time

print("Welcome to National Movie Box Part")
time.sleep(0.5)
print("There is a list of Topics I have had so far")
time.sleep(0.5)
print("Please type the assigned number to the topic you want")
time.sleep(0.5)
print("1.Highest Grossing movies in India: 1")
time.sleep(0.5)
print("2.Highest Grossing movies in India by year: 2")
time.sleep(0.5)
print("3.Highest Grossing movies in India by Language: 3")
time.sleep(0.5)                              
print("4.Highest Grossing movie Franchises in India: 4")
time.sleep(0.5)
print("5.Highest Profitable movies of India by Year: 5")
time.sleep(0.5)
print("Want to Go back Press 6")
time.sleep(0.5)

while True:
    a34 = int(input("So What's your Choice: "))
    if a34 == 1:
        print("Okay , So your are getting a list of Highest Grossing Movies of India")
        time.sleep(0.5)
        import highmovieINDIA
        import highmovieINDIA
    elif a34 ==2:
        print("Okay so you are getting a list of Highest Grossing movies of India by year")
        time.sleep(0.5)
        import highmovieINDIAyear
        import highmovieINDIAyear
    elif a34 == 3:
        print("Okay , So you are getting a list of Highest Grossing Movies in India by Language")
        time.sleep(0.5)
        import highmovieLANG
        import highmovieLANG
    elif a34 == 4:
        print("Okay , So you are getting a list of Highest Grossing Movie Franchises in India")
        time.sleep(0.5)
        import highmoviefranchINDIA
        import highmoviefranchINDIA
    elif a34 == 5:
        print("Okay So you are getting list of Highest Profitable Movies of India")
        time.sleep(0.5)
        import profitINDIA
        import profitINDIA
    elif a34 == 6:
        print("Going Back")
        time.sleep(0.5)
        import naorglo
        import naorglo
    else:
        print("Sorry My range is bit less Please Enter between 1 to 6 only")
        continue