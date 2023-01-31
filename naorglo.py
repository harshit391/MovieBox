import time

while True:
    
    a12 = int(input("If you want to Go global then type 1 and if you want to go for national cinema then type 2: "))
    
    if a12 == 1:
        import international
        import international
    
    elif a12 == 2:
        import national
        import national
    
    else:
        print("I think you entered something different value , Please correct it")
        time.sleep(0.5)
        print("Valid : 1 for Global and 2 for National")
        continue
    break