import time

print("India is a country where language changes after every 100 KM")
time.sleep(0.5)
print("Now I can't able to cover much languages but here are some")
time.sleep(0.5)
print("Please Type Number Assigned to the language")
time.sleep(0.5)

lilang = ["Assammese","Bengali","Bhojpuri","Gujrati","Hindi","Kannada","Malyalam","Marathi","Odia","Punjabi","Tamil","Telugu"]

liregion = ["Jollywood","Tollywood","Bhojiwood","Dhollywood","Bollywood","Sandalwood","Mollywood","Mollywood","Ollywood","Pollywood","Kollywood","Tollywood"]

liassam = ["Ratnakar","Kanchanjhanga","Mission China","Raamdhenu","Tumi Aahibane","Priyar Priyo","Joymoti","Hiya Diya Niya","Doordarshan Eti Chandra","Basundhara","Village Rockstars","Bahniman","Nayak","Kanyadaan","Ruff and Tuff","Jeevan Baator Logori"]
liassamearn=[9.25,7,6,2.04,1.94,1.80,1.48,1,0.90,0.87,0.80,0.65,0.57,0.55,0.45,0.41]

libengali=["Amazon Obhijaan","Chander Pahar","Boss 2: Back to Rule","Paglu","Sathi","Panther: Hindustan Meri Jaan","Paran Jai Jaliya Re","Rangbaaz","Praktan","Awara","Posto","Shotru","Challenge 2","Zulfiqar","Haami","Durgeshgorer Guptodhon","Mishawr Rawhoshya","Abhimaan","rajkahini","Boss: Born to Rule","Challenge","Khokababu","Shudhu Tomari Janyo","Paglu 2","Shikari",]
libengaliearn = [52,20,12.50,9.92,9.78,9.50,9.50,9,8.50,8.50,8,7.56,7.55,7.50,7.40,7.25,7.10,7,7,6.94,6.80,6.25,6.20,6.15,6]

libhojpuri = ["Sasura Bada Paisawala","Ganga","Pratigya","Border","Crack Fighter","Nirahua Hindustani","Mehandi Laga ke Rakhna","Pandit ji Batai Na Biyah Kab hoi","Devra Bada Satawala","Saat Saheliyan"]
libhojpuriearn = [36,35,22,19,17,14,14,12,10,9]

ligujrati = ["Chaal Jeevi Laiye","Desh Re Joya Dada","Shu Thayu?","Kehvatlal Parivar","Chhello Divas","Sharato Lagu","Hellaro","Gujjubhai the Great","Naadi Dosh","GujjuBhai: Most Wanted","Golkeri","Bey Yaar","Karsandas Pay and Use","Love Ni Bhavai","Thai Jashe"]
ligujratiearn = [52.14,22,21,19.50,18,17.50,16,15,13.50,10,9,8.50,8,8,4]

lihindi = ["Dangal","Bajrangi Bhaijaan","Secret Superstar","PK","Sultan","Sanju","Tiger Zinda Hai","Padmaavat","Dhoom 3","War","Brahmastra Part One: Shiva","Andhadhun","3 Idiots","Chennai Express","Simmba","Kabir Singh","Dilwale","Prem Ratan Dhan Payo","Bajirao Mastani","Tanhaji: The Unsung Warrior","Kick","The Kashmir FIles","Happy New Year","Uri: The Surgical Strike","Thugs of Hindostan","Golmaal Again","Bharat","Good Newwz","Hindi Medium","Race 3","Ek tha Tiger","Krrish 3","Houseful 4","Yeh Jawaani Hai Deewani","Sooryavanshi","Toilet: A Love Story","Mission Mangal","Raees","Bang Bang","Bhool Bhulaiyaa 2","Drishyam 2","Baaghi 2","Dabangg 2","Tanu Weds Manu Returns","Bodyguard","Ae Dil Hai Mushkil","Gully Boy","Badhaai Ho","Total Dhamaal","Dabangg 3","Dabangg","Hichki","Rustom","Tubelight","Singham Returns","Airlift","Super 30","Jab Tak Hai Jaan","Ra.One","Judwaa 2","Gangubai Kathiawadi","Chhichhore","Kesari","RamLeela","Don 2","My Name is Khan","Rowdy Rathore"]
lihindiearn = [1924.7,858.8,830.8,742.3,614.9,580.1,562.5,560.7,545.7,460.6,412.7,410.2,397.3,391.5,387,375,371.3,366.1,354.4,351.9,349.5,344.2,343.9,339.3,317.7,310.3,307,304.2,304,302,301.9,298.4,296.8,295.5,291.8,290.2,282.8,275,270.8,263.9,256.8,251.1,251,243,234,230,229.5,225,222,219.3,215,215,214,214,212,210,209.1,209,206.3,205.5,203.9,203.7,202,202,201.2,200.6,200]

likannada = ["K.G.F. Chapter 2","Kantara","K.G.F. Chapter 1","777 Charlie","Kurukshetra","James","Raajakumara","Vikrant Rona","Avane Srimannarayana","Roberrt","The Villian","Yajamana","Pailwaan","Mr. and Mrs. Ramchari","Anjaniputra","Mungaru Male","Hebbuli","Pogaru","Kotigobba 3","Natasaarvabhowma","Kranthiveera Sangolli Rayanna","Yuvarathnaa","Uppi 2","Tagaru","Doddmane Hudga","Bul Bul","Kirik Party","Kotigobba 2","Jogi the King","Gaalipata 2","Maanikya","Shivalinga","Saarathi","Master Piece","Aaptharakshaka","Super","Milana","Chakravarthy","Jackie","Ranna","Salaga","Aapthamitra","Odeya","Tarak","Mufti","RangiTaranga"]
likannadaearn = [1228.3,393.3,226.1,100.5,90,79.5,71,70.3,56.5,54.7,52.5,52,49.5,47.5,45.5,45,45,44,42.6,42,40,39.7,39.5,39.5,38,37,36.5,36,35,35,34.5,33,33,32.5,31,30,30,29,29,26.5,26.2,26,25.5,25.2,25.1,25]

limalayalam = ["Pulimurugan","Lucifer","Bheeshma Parvam","Kurup","Premam","Kayamkulam Kochunni","Drishyam","Hridayam","Ennu Ninte Moideen","Odiyan","Oppam","Njan Prakashan","Two Countries","Jana Gana Mana","Marakkar: Lion of the Arabian Sea","Munthirivallikal Thalirkkumbol","Madhuraraja","Thallumaala","Kaduva","Anjaam Pathiraa","Bangalore Days","The Great Father","Amar Akbar Anthony","Abhrahaminte Santhathikal","Ezra","Jaya Jaya Jaya Jaya Hey","Ramaleela","Charlie","Rorschach","Kumbalangi Nights","Jomon's Gospels","Shylock","Thanneermathan Dinangal","Jacob's Kingdom of Heaven","Ayyappanum Koshiyum","Aadhu - Oru Bheegara Jeevi Aana 2","Kattappanayile Rithwik Roshan","CBI 5: The Brain","Varathan","Twenty: 20","Mamangam","Oru Vadakkan Selfie","Aadhi","Love Action Drama","Action Hero Biju","Ittymaani: Made in China","Driving Licence","Varane Avashyamund","Oozham","Kerala Varma Pazhassi Raja","The Priest","CIA: Comrade in America","Theevandi","Take off","Classmates","Njandukalude Naattil Oridavela","Velipadinte Pushthakam","Parava","Rajamanikyam"]
limalayalamearn = [141.6,127.4,87,81,77.1,67,64,55.5,55.4,53.6,52.5,50.7,50.5,50.1,49.3,49,47.5,47.5,46.5,45.2,45,43.5,43,42.5,41,41,40.5,40,39.2,37,36,35.9,35.5,35,34.5,34.5,34,33.5,33,33,32.5,32,31.5,30.2,30,30,29.5,29,29,28,27.9,27.5,27.1,27,26,25.6,25.3,25.1,25]

limarathi = ["Sairat","Natsamrat","Katyar Kaljat Ghusali","Timepass 2","Lai Bhaari","Timepass","Duniyadari","Mee Shivajiraje Bhosale Boltoy","Ventilator","Naal","Takatak","Hirkani"]
limarathiearn = [110,46.71,40.12,37.16,37,31,28.75,24,23.72,22.15,21,14]

liodia = ["Ishq Tu Hi Tu","Super Michchua","Pilata Bigidi Galla","Rangila Baba","Jaga Hathare Pagha","Something Something","Balunga Toka","Mun Eka Tumara","Bhala Pae Tote 100 Ru 100","Raja Jhia Sange Hoi Galla Bhaba"]
liodiaearn = [6.79,5.98,5.76,4.79,4.25,3.70,3.40,3.34,3.25,3.04]

lipunjabi = ["The Legend of Maula Jatt","Carry on Jatta 2","Saunkan Saunkane","Chal Mera Putt 2","Honsla Rakh","Shadaa","Chaar Sahibzaade","Chhalla Mud ke nhi Aaya","Sardaarji","Chal Mera Putt 3","Qismat 2","Manje Bistre","Babe Bhangra Paunde ne","Ardaas Karaan","Chal Mera Putt","Qismat","Angrej","Jatt and Juliet 2","Muklawa","Sajjan Singh Rangroot","Love Punjab","Ambarsariya","Bambukat","Sardaarji 2","Vekh Baraatan Challiyan","Aaja Mexico Chaliye","Jatt and Juliet","Punjab 1984","Vadhayiyan ji Vadhayiyaan","Super Singh","Jatt James Bond","Sufna","Manje Bistre 2","Nikka Zaildar 2","Lahoriye","Mar Gaye Oye Loko","Kala Shah Kala","Sadda Haq","Maa","Golak Bugni Bank Te Batua","Chaar Sahibzaade: Rise of Banda Singh Bahadur","Puaada","Carry on Jatta","Disco Singh","Ashke","Nikka Zaidar 3","Paani Ch Madhaani","Yaar Mera Titliaan","Ardaas","Guddiyan Patole","Rabb Da Radio","Laavan Phere","Galwakdi","Lucky Di Unlucky Story","Nikka Zaildar","Laung Laachi","Daakuan Da Munda"]
lipunjabiearn = [230,57.67,57.60,57.15,54.62,53.10,46.34,39.43,38.38,35.84,33.27,32.50,32.11,31.82,31.29,31.28,31.19,27.95,25.52,25.51,25.16,24.88,24.51,24.20,23.90,23.72,23.09,22.64,20.15,20.05,20,19.35,19.25,19.20,19,19,19,18.94,18.79,18.20,18.05,18.05,18,18,18,17.95,17.82,17.03,17,17,16,16,15.91,15.70,15,15,15]

litamil = ["2.0","Ponniyan Selvan: Part 1","Vikram","Bigil","Kabali","Enthiran","Mersal","Sarkar","Master","I","Beast","Petta","Darbar","Viswasam","Valimai","Kaala","Theri","Annatthe","Sivaji","Lingaa","Kaththi","Kanchana 3","Thuppaki","Vedalam","Vivegam","Singam 2","Don","Kanchana 2","Singam 3","Bairavaa","7 Aum Arivu","Nerkonda Paarvai","Vishwaroopam","Dasavatharam","24","Thiruchitrambaiam","Kaithi","Doctor","Arrambham"]
litamilearn = [654.4,500.8,424.5,304.6,294.2,290.6,257.5,255.9,245.3,239.2,237.3,225.5,209.3,184,163.2,156.1,154.5,154.1,152.4,151.8,131.2,130,127.9,127.5,124.6,121.8,121.5,113,111.9,110.5,109.3,108.5,108,107.5,107.2,104.7,102.9,101.4,100.3,]

litelugu = ["Baahubali 2: The Conclusion","RRR","Baahubali: The Beginning","Saaho","Pushpa: TheRise - Part 1","Ala Vaikunthapurramuloo","Sye Raa Narasimha Reddy","Sarileru Neekevvaru","Rangasthalam 1985","Sarakaru Vaari Paata","Maharshi","Bharath Ane Nenu","Khaidi No. 159","Bheemla Nayak","Aravindha Sametha","Srimanthudu","Radhe Shyam","F2: Fun and Frustartion","Janatha Garage","Vakeel Saab","Sarraibodu","Attarintiki Daredi","Akhanda","Jai Lava Kusa","Magadheera","Geetha Govindam","Spyder","Duvvada Jagannadham","Karthikeya 2","Gabbar Singh","Race Gurram","Katamarayudu","Godfather","Dookudu","Eega"]
liteluguearn = [1749,1131.1,600.6,417.6,369.9,274.2,248,237.1,213.4,192.4,184.6,178.1,166.2,161.3,155,153,148.4,140.5,139.6,137.2,134.5,132.9,132.6,131.9,128.8,126,121.8,117.1,113.3,106,105,102.7,102,101,100.5,]
for i in range(len(lilang)):
    print(i+1,".",lilang[i])
    time.sleep(0.5)

def value(a,c):
    print("So , I have a List of",len(a),"Movies How much you want")
    while True:
        a990 = int(input("Enter the value: "))
        if a990<1:
            print("Please Enter a valid Input between 1 to",len(a))
            continue
        elif a990>len(a):
            print("Sorry I have list till ",len(a),"only")
            continue
        else:
            print("Okay, Printing Top",a990,lilang[a331-1],"Movies")
            for i in range(a990):
                print(i+1,".",a[i],"-->",c[i],"Crores")
                time.sleep(0.5)
            break
    return "Here is your list"

while True:
    a331 = int(input("Please Enter Between 1 to 12: "))
    if a331==0:
        print("Please Enter a Valid Value")
        time.sleep(0.5)
        continue
    elif a331>12:
        print("Sorry I have only 12 Languages Yet , Please Enter from 1 to 12")
        continue
    else:
        print("Okay so you want list of Highest Grossing",lilang[a331-1],"movies")
        time.sleep(0.5)
        if a331==1:
            print(value(a=liassam,c=liassamearn))
        elif a331==2:
            print(value(a=libengali,c=libengaliearn))
        elif a331==3:
            print(value(a=libhojpuri,c=libhojpuriearn))
        elif a331==4:
            print(value(a=ligujrati,c=ligujratiearn))
        elif a331==5:
            print(value(a=lihindi,c=lihindiearn))
        elif a331==6:
            print(value(a=likannada,c=likannadaearn))
        elif a331==7:
            print(value(a=limalayalam,c=limalayalamearn))
        elif a331==8:
            print(value(a=limarathi,c=limarathiearn))
        elif a331==9:
            print(value(a=liodia,c=liodiaearn))
        elif a331==10:
            print(value(a=lipunjabi,c=lipunjabiearn))
        elif a331==11:
            print(value(a=litamil,c=litamilearn))
        elif a331==12:
            print(value(a=litelugu,c=liteluguearn))
        break

print("If you want to know the Source Site of the info Then Press 1")
time.sleep(0.5)
print("If you want to know the name by which regional cinema is recognized (like hindi - bollywood) Press 2")
time.sleep(0.5)
print("If you want to exit the application Then Press 3")
time.sleep(0.5)


while True:
    a567 = int(input("Press between 1 to 3: "))
    if a567 == 3:
        import exitapplication
        import exitapplication
        break
    elif a567 == 1:
        print("Redirecting to the site")
        time.sleep(0.5)
        import webbrowser
        webbrowser.open("https://en.wikipedia.org/wiki/List_of_highest-grossing_Indian_films#Highest-grossing_films_by_language") 
        continue
    elif a567 == 2:
        print("Type the assigned number to the language from list given below")
        time.sleep(2.5)
        for i in range(len(lilang)):
            print(i+1,".",lilang[i])
        while True:
            a331 = int(input("Please Enter Between 1 to 12: "))
            if a331==0:
                print("Please Enter a Valid Value")
                continue
            elif a331>12:
                print("Sorry I have only 12 Languages Yet , Please Enter from 1 to 12")
                continue
            else:
                print(lilang[a331-1],"Cinema is known as --->",liregion[a331-1])
                time.sleep(0.5)
                print("If you want to know the name by which regional cinema is recognized (like hindi - bollywood) Press 2")
                time.sleep(0.5)
                print("If you want to exit the application Then Press 3")
                time.sleep(0.5)
            break
        continue
    else:
        print("I think You mistakenly press the wrong key , Its Okay I will Ask you Again")
        time.sleep(0.5)
        print("If you want to know the Source Site of the info Then Press 1")
        time.sleep(0.5)
        print("If you want to know the name by which regional cinema is recognized (like hindi - bollywood) Press 2")
        time.sleep(0.5)
        print("If you want to exit the application Then Press 3")
        time.sleep(0.5)
        continue    