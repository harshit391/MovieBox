import time

print("Welcome to the Global Movie Box Part")
time.sleep(0.5)

print("There is a list of Topics I have had so far")
time.sleep(0.5)

print("Please type the assigned number to the topic you want")
time.sleep(0.5)

print("1.Highest Grossing movies worldwide: 1")
time.sleep(0.5)
print("2.Highest Grossing movies worldwide by year: 2")
time.sleep(0.5)
print("3.Highest Grossing movie Companies worldwide: 3")
time.sleep(0.5)                              
print("4.Highest Grossing movie Franchises: 4")
time.sleep(0.5)
print("5.Biggest Flops in the year: 5")
time.sleep(0.5)
print("Want to Go back Press 6")
time.sleep(0.5)

while True:
    a34 = int(input("So What's your Choice: "))
    if a34 == 1:
        print("Okay , So your are getting a list of Highest Grossing Movies Worldwide")
        time.sleep(0.5)
        import highmovieworl
        import highmovieworl
    elif a34 ==2:
        print("Okay so you are getting a list of Highest Grossing movies Worldwide by year")
        time.sleep(0.5)
        import highmovieworldyear
        import highmovieworldyear
    elif a34 == 3:
        print("Okay , So you are getting a list of Highest Grossing Movie Companies by this year")
        time.sleep(0.5)
        import highmoviecomp
        import highmoviecomp
    elif a34 == 4:
        print("Okay , So you are getting a list of Highest Grossing Movie Franchises")
        time.sleep(0.5)
        import highmoviefranch
        import highmoviefranch
    elif a34 == 5:
        print("Okay , So you are getting List of Flop Movies")
        time.sleep(0.5)
        import flopsmovies
        import flopsmovies
    elif a34 == 6:
        print("Going Back")
        time.sleep(0.5)
        import naorglo
        import naorglo
    else:
        print("Sorry My range is bit less Please Enter between 1 to 6 only")
        continue
    break