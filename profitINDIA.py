import time

print("This List Consits of Movies Which have earned fabulous numbers")
time.sleep(1)
print("Fabulous numbers even after having a limited budget")
time.sleep(1)
print("So I have Data From Year 2002 to 2022")
time.sleep(0.5)
print("Which year you want to see")
time.sleep(0.5)

liyear = {
2002:["Aankhen","Saathiya","Hum Tumhare hai Sanam","Company","Dil Hai Tumhara","Road","Shakthi","Hamraaz","Tumko Na Bhool Paayenge","Devdas","Kaante","Hathiyaar","Jaani Dushman"],
2003:["Munna Bhai M.B.B.S.","Baghban","Chalte Chalte","Kal Ho naa Ho","Gangaajal","Hungama","Koi... Mil Gaya","Andaaz","Tere Naam","Ek Aur Ek Gyarah","Darna Mana Hai","Dil ka Rishta","Saaya","Main Prem Ki Diwani Hoon","Kuch Naa Kaho","Talaash: The Hunt Begins","The Hero: Love Story of a Spy","Dum","Footpath","Xcuse Me"],
2004:["Dhoom","Main Hoon Na","Veer Zara","Hum Tum","Hulchul","Mujhse Shaadi Karogi","Masti","Aitraaz","Vaastu Shastra","Khakee","Lakshya","Kyun! Ho Gaya Na","Swades","Ab Tumhare Hawaale Watan Saathiyo","Krishna Cottage","Yuva","Chameli","Pride and Honour","Paap","Run","Deewar","Maqbool"],
2005:["Salaam Namastey","Bunty aur Babli","Black","BluffMaster!","Garam Masala","Kyaa Kool Hai Hum","Maine Pyaar Kyun Kiya","No Entry","Sarkar","Waqt: The Race Against Time","Kaal","Iqbal","Zeher","Apahran","Aashique Banaya Apne: Love Takes Over","Shabd","Dus","Vaah! Life Ho to Aisi","Mangal Pandey","Shaadi No. 1","Main , Meri Patni aur Woh..","Deewane Huye Paagal","Parineeta","Vaada","Kyon Ki its Fate"],
2006:["Vivah","Lage Raho Munna Bhai","Malamaal Weekly","Dhoom 2","Phir Hera Pheri","Range de Basanti","Fanaa","Taxi no. 9 2 11: Nau Do Gyarah","Krrish","Golmaal: Fun Unlimited","Don","Gangster","Kabul Express","Aksar","Kabhi Alvida Naa Kehna","Apna Sapna Money Money","Chup Chup Ke","Bhagam Bhag","36 China Town","Woh Lamhe..","Omakara","Humko Deewana Kar Gaye","Pyare Mohan","Zinda","Darna Zaroori Hai","Jaan-E-Mann: Lets Fall in Love Again","Being Cyrus","Fight Club"],
2007:["Swami","Taare Zameen Par","Chak De India","Om Shanti Om","Guru","Welcome","Partner","Namastey London","Jab we met","Bhool Bhulaiyaa","Heyy Babyy","Dhamaal","Life in a Metro","Shootout at Lokhandwala","Ta Ra Rum Pum","Apne","Honeymoon Travel Pvt. Ltd.","Dhol","Fool N Final","Dhan Dhana Dhan Goal","Dil Dosti Etc.."],
2008:["C Kkompany","Rab ne Bana Di Jodi","Mukhbiir","Singh is Kinng","Jannat: In Search of Heaven","A Wednesday","Jodhaa Akbar","Ghajini","Golmaal Returns","Race","Sarkar Raj","1920","Bhoothnath","One Two Three","Mere Baap Pehle Aap","Welcome to Sajjanpur","Thoda Pyaar Thoda Magic","Sunday","Mumbai Meri Jaan","Kidnap","De Taali"],
2009:["3 Idiots","Ajab Prem ki Ghazab Kahani","Wake up Sid","Love Aaj Kal","All the Best","Shortkut - The Coin is on","New York","Paa","Rocket Singh: Salesman of the Year","Luck By Chance","13B: Fear Has a New Address","Dev.D","Billu","Wanted","Luck","Chandini Chownk to China","De Dana Dan"],
2010:["Dabangg","My Name is Khan","Tere Bin Laden","Golmaal 3","Housefull","Tees Maar Khan","Kushti","Hello Hum Lallan Bol Rahe Hai","Atithi Tum Kab Jaoge?","Well Done Abba!","Phas Gaye Re Obama","Do Dooni Chaar","Once Upon a Time in Mumbai","Band Baaja Baraat","Khatta Meetha","Benny and Babloo","Karthik Calling Karthik","No Problem","Veer","Ishqiya","Prince","Lafangey Parindey"],
2011:["Ready","No One Killed Jessica","Delhi Belly","Mankatha","Bodyguard","Shaitan","Zindagi na Milegi Dobara","Ko","Aadukalam","Engeyum Eppodhum","Mayakkam Enna","Vaanam","Mumbai Diaries","Nadunisi Naaygal","aaranya Kaandam","Chiller Party","7 Aum Arivu"],
2012:["Kahaani","English Vinglish","OMG: Oh My God!","Dabangg 2","Rowdy Rathore","Vicky Donor","Jab Tak Hai Jaan","Housefull 2","Cocktail","Barfi!","Agneepath","Bol Bacchan","Gangs of Wasseypur","Paan singh Tomar","Billa 2"],
2013:["Naduvvula Konjam Pakkatha Kaanom","Fukrey","Aashqui 2","Chennai Express","Dhoom 3","Mirchi","Bhaag Milkha Bhaag","Celluloid","Krrish 3","Amen","Attrintiki Daredi","Singam 2","Balupu","Kai Po Che","Ranjhanna","Yeh Jawaani Hai Deewani","Vishwaroopam","Special 26","Bachchan","Race 2","ABCD","Baadshah"],
2014:["PK","Mr. and Mrs. Ramchari","Ugramm","Bangalore Days","Velayilla Pattahari","The Villian","Kick","Holiday: A Soldier is Never Off Duty","2 States","Humpty Sharma Ki Dulhania","Heropanti","Manniya","Jai Ho","Maan Karate","Singham Returns","Happy Ney Year","Manam","Gunday","Veeram","Race Gurram","Bang Bang","Govindudu Andari Vaadele","Main Tera Hero","Kaththi","Jilla","Lingaa","Yevadu","Anjaan","Action Jackson"],
2015:["Premam","Bajrangi Bhaijaan","Oru Vadakkan Selfie","Kanchana 2","Amar Akbar Anthony","Tanu Weds Manu Returns","Ennu Ninte Moideen","Charlie","Bhale Bhale Magadivoy","Two Countries","Baahubali: The Beginning","Oiku","Thani Oruvan","Any Body Can Dance 2","I","Bajirao Mastani","Vedalam","Prem Ratan Dhan Payo","Dilwale","Welcome Back","Baby","Srimathudu","Anegan","S/O Satyamurthy","Dil Dhadakne Do","Temper","Yennai Arindhaal","Kick 2","Bruce Lee - The Fighter","Rushramadevi","Massu Engira Masilamani"],
2016:["Dangal","Kattappanayile Rithwik Roshan","Action Hero Birju","Jacob's Kingdom of Heaven","Oppam","Airlift","Pulimurugan","Sultan","Rustom","Pichaikkaran","Baaghi","Pink","Ae Dil Hai Mushkil","Kabali","Remo","Janatha Garage","Kahanni 2","Soggade Chinni Nayana","Dear Zindagi","Sarrainodu","Dishoom","Happy Bhag Jayegi","A Aa..","irumugan","Housefull 3","M.S. Dhoni","Aranmanai 2","Their","Oopiri","Dhruva","To Father with Love","Fan","Carefree","Shivaay","Force 2","24","Azhar","A Flying Jatt","Sardaar Gabbar Singh"],
2017:["Secret Superstar","Arjun Reddy","Hindi Medium","Baahubali 2: The Conclusion","Badrinath Ki Dulhania","Mom","Fidaa","Fukrey Returns","Nenu Local","Toilet: A Love Story","Shatamanam Bhavati","Raajakumari","Tiger Zinda Hai","Tumhari Sulu","Khaidi No. 150","Shubh Mangal Savdhan","The Ghazi Attack","Ninnu Kori","MCA: Middle Class Abbayi","Sachin: A Billion Dreams","Judwaa 2","Seeking True Love","Jai Luv Kusa","Rarandoi Veduku Chudham","Golmaal Again","Theeran Adhigaran Ondru","Duvvada Jagandham","Mersal","Raees","Naam Shabana","Half Girlfriend","Jolly LLB 2","Velaikkaran","Vikram Vedha","Phillauri","Bairava","Nene Raju Nene Mantri","Raja the Great","Velayilla Pattahari 2","Kaabil","Mubarkan","Baadshaho","Gautamiputra Satakarni","Tubelight","Singam 3","Katamarayadu","Vivegam","Jab Harry Met Sejal","Munna Michael","Spyder"],
2018:["Andhadun","Hichki","Geetha Govindham","Badhaai Ho","Carry on Jatta 2","Stree","Sanju","Raazi","Tamizh Padam 2.00","Njan Prakshan","K.G.F Chapter 1","Mahanati","Rangsthaam 1985","Baaghi 2","Sonu Ke Titu Ki Sweety","96","Padmaavat","102 Not Out","Simmba","Veere Di Wedding","Dhadak","Kadaikutty Singam","Chekka Chivatha Vaanam","Parmanu: The Story of Pokhran","Padman","Irumbu Thirai","Sui Dhaaga","Bharath Ane Nenu","Bhaagamathie","Arvindha Sametha","Satyamev Jayate","Sarkar","Raid","Race 3","Jai Simha","2.0","Odiyan","GOLD","Sandarozhi","Naa Peru Surya Naa Illu India","Kayakular Kochunni","Kedarnath","Vada Chennai","Seema Raja","Thaanaa Serndha Koottam","Thugs of Hindostan","Kaala","October","Batti Gul Meter Chalu","Ek Villian","agnathavasi - Price in Exile","Saamy Square"],
2019:["URI: The Surgical Strike","Kabir Singh","Badla","Shadaa","Dream Girl","Luka CHhupi","Bala","Chhichhore","Mission Mangal","Lucifer","Yajamana","Kaithi","Kanchana 3","F2: Fun and Frustration","Gully Boy","Good Newwz","Article 15","Pati Patni Aur Woh","War","iSmart Shankar","Bharat","Housefull 4","Super 30","Avane Srimannarayana","Bigil","Batla House","Manjili","Namma Vettu Pillai","Viswasan","Comali","Total Dhamaal","Maharshi","Kesari","Mardaani 2","Petta","Dabangg 3","De De Pyaar De","Jersey","Prati Roju Pandaage","Venky Mama","Asuran","Saaho","KurukShetra","nerkonda Paarvai","Manikarnika","Sye Raa Narasimha Reddy","Marjaavan","Student of the Year 2","Vinaya Vidheya Rama","Kalank"],
2020:["Draupathi","Ayyapanum Koshiyam","varane Avashyamand","Forensic","Shylock","Sarileru Neekevaru","Tanhaji: The Unsung Warrior","Ala Vaikunthpurramulo","Shivaji Surathakal","Anjaam Pathiraa","Gypsy","Shubh Mangal Saavdhan","Thappad","Chhapak","Street Dancer 3D","Baaghi 3","Chal Mera Putt 2","Malang","Love aaj Kal","Jaanu","Jawani Jaaneman","Bhoot Part One: The Haunted Ship","Bheeshma","Darbar"],
2021:["Jathi Ratnalu","Honsla Rakh","Uppena","Kurup","Maanadu","Doctor","Love Story","Master","Pushpa: The Rise","Akhanda","Most Eligible bachelor","Vakeel Saab","Sooryavanshi","Annatthe","Antim: The Final Truth","Robeet","Karnan","Shyam Singha Roy","Krack"],
2022:["Kantara","The Kashmir Files","K.G.F. Chapter 2","Hridyam","Love Today","Bheesham Parvam","Karthikeya 2","777 Charlie","Saunkan Saunkane","Drishyam","Thiruchitrabalam","Bhool Bhulayiya","Vikram","Thallumala","Sita Ramam","Jana Gana Man","James","Sardar","Kaduva","Bheemla Nayak","Don","Sarkaru Vaaru Patta","Major","RRR","Bangarraju","PS - 1","Rocketry","Kaathu Vekalu","Vikrant Rona","Viruman","F3","Vendhu","Gangubai Kathiawada","Beast","Jug Jug Jeeyo","Bimbisara","E.T.","Valimai","Brahmastra","Godfather"]}

libudget = {
2002:[1.96,7.5,12,9.5,7.25,6,10,15,11,50,30,7,18],
2003:[10,10,11,22,4.5,6,25,9.25,10,9.5,4.5,8.25,3,24,8,9.75,35,7.75,5.5,2.25],
2004:[11,15,18,8.5,10,19,12,11,5,25,14,10,25,20,4,18,3.5,17,3,6.75,21,3],
2005:[11,14,20,10,17,19,15,24,14,16,13,2.25,5,11,4.5,7,23,12,34,15,2.5,20,25,8,21],
2006:[8,19,7,35,18,28,30,10,40,15,38,6.5,12,5.25,50,9.5,12,32,19,7.75,26,17,13,13,8.75,40,4,8.25],
2007:[2.75,12,20,35,22,32,28,21,15,25,31,19,9.5,18,28,20,10,14,24,19,3.5],
2008:[0.15,22.67,5,30,10,3,33,65,25,46,28,7,20,14,20,9,23,22,3.5,31,12],
2009:[55,25,13,35,20,4.5,28,21,16,15,12,11,26,52,20,80,60],
2010:[41,50,25.8,40,30,35,6,1.75,15,10,6,2,38,15,35,4.75,20,35,48,19,37,19],
2011:[30,9,23,24,60,11,45,20,18,20,23,20,10.2,1.5,5.5,8,80],
2012:[8,10,20,50,60,15,50,45,35,50,58,50,9.2,7,35],
2013:[0.8,8,18,70,100,15,41,3.5,95,3.5,55,45,221,30,36,75,95,50,11,94,27,55],
2014:[85,6,4,10,20,40,100,50,50,35,25,15,65,15,80,150,25,55,45,50,160,30,40,70,50,100,40,65,80],
2015:[4,90,4,17,7,40,10,7,10,12,180,40,20,60,90,140,5,180,165,75,65,70,25,45,80,40,50,30,60,80,60],
2016:[70,3,3,4,7,35,25,140,50,10,35,30,70,90,225,50,20,30,50,50,50,20,35,40,85,100,15,75,50,50,50,110,65,100,40,70,35,45,75],
2017:[50,4,25,250,40,35,20,25,15,75,15,20,160,15,50,20,20,20,25,30,75,20,50,20,125,25,50,115,125,25,50,85,40,30,25,55,25,30,30,90,55,65,50,135,75,70,100,125,45,120],
2018:[30,25,15,30,8,25,100,35,10,10,50,20,55,65,40,15,175,35,125,45,40,25,35,35,75,25,50,75,30,70,50,120,70,150,25,350,30,85,30,55,40,60,40,40,70,235,125,45,50,45,90,50],
2019:[40,50,20,10,40,25,40,50,75,35,15,30,40,45,75,100,30,40,170,25,125,125,90,25,135,50,30,35,85,25,105,90,100,35,125,125,75,30,35,40,40,275,60,75,100,190,50,75,85,125],
2020:[0.75,5,4.3,4,12,75,125,100,4,20,5,45,24,36,70,100,8,64,40,10,40,37,50,240],
2021:[4,12,22,27,30,40,30,135,170,70,25,70,160,150,40,50,52,50,70],
2022:[16,20,100,7,10,17,22,20,12,50,30,70,135,20,30,20,60,40,20,75,50,90,30,550,30,250,25,35,95,30,70,35,125,150,85,40,75,150,400,100]}

liearn = {
2002:[62.95,29.1,34.76,25.02,18.03,13.23,20.36,29.7,19.89,89.46,43,9.63,18.56],
2003:[56.28,43.11,43.38,86.09,16.67,20.24,82.33,28.81,24.54,20.99,9,14.6,5.15,39.31,13.08,14.66,45.13,9.05,6.37,2.6],
2004:[72.47,89.7,97.6,42.63,32.86,55.98,34.14,26.04,10.17,49.09,26.25,16.35,40,30.16,5.9,26,5.01,23.48,4.01,7.74,21.86,3],
2005:[57.2,63.74,66.6,32.71,54.65,60.77,47.22,74,39.3,42.48,33.11,5.6,11.06,23.16,9.32,12.08,38.83,19,52,20.49,3.37,26.5,32.63,9.53,23.15],
2006:[53.9,126.2,42.7,150,69.12,97.9,103,32.17,126.55,46.72,106.34,18,29,12.18,113,20.73,25.5,67.82,38,15,42,27.36,18.61,17.68,10.64,46.26,4.6,8.88],
2007:[23.5,98.48,109,148.16,83.67,117.91,100.91,71.4,50.9,82.8,84,50.73,24.45,46.04,70,45,19.51,23,27.62,21.72,3.74],
2008:[4.83,187,23,136,41.5,12,120,232,80,103.45,59.46,14.5,38.8,27,36.2,14.7,37.25,31.96,5.02,35.6,13.1],
2009:[400.61,103.73,47.1,119,61,12.67,78.33,50,33.65,29,23,20.82,47.5,93.23,33.58,120,78.43],
2010:[221.4,223,115,170,124.5,100,16.79,4.75,39,25,14,4.5,85.2,33.3,63,7.25,28.22,48.7,64,25,48,22.7],
2011:[180,45.2,114,100,2234,39.76,153,50,30,32,36,28,14.09,2,7,10,100],
2012:[100,102,180,253.54,281,68.32,211,186,125.7,174.73,193,165,27.85,20.18,62],
2013:[18,49,109,423,556.4,80,210,16.57,393.37,12.15,187,136,60,83,94,178,220,103,20,161,39.34,80],
2014:[792,53,31,50,92,155,378,178.3,173,119.6,75.8,43,186.3,42,216.5,397,62,130.8,100,108.9,340,61,77.2,117.5,80,154,57.5,80.4,88.7],
2015:[77.2,922.1,31.5,114,46.4,258,57.2,36.1,50,50.3,650,141.2,64.7,165.9,240,362,125.7,450.8,388,168.6,142.9,153,54,93,150,74,87.5,36.6,68.5,91,68],
2016:[2122.3,37.1,31.2,39.3,52,228,150,607.7,216,43,125.8,104.2,240.7,309,75,140,55.9,82.3,136.1,134,119.5,46.5,80,89,185.7,215.4,31,154.5,97.7,89.6,88.4,182.2,99.4,147.2,58.7,102,50.1,56.2,85.5],
2017:[830.8,51.5,304,1749,198,158.6,87.8,107,60,290.2,55,71,562.5,50,166.2,63.4,63,59.1,72.6,85.6,205.5,54.5,131.9,51,310.3,59,117.1,257.5,275,54,107.5,182,84.5,62.5,52,110.5,50,56.6,54.5,155.4,92.5,106.3,80.7,214,111.9,102.7,124.6,147,51.1,121.8],
2018:[410.2,215,126,225,56.3,173.9,580.1,193,51.3,50.7,226.1,85.1,213.4,251.1,148.5,55.5,560.7,111.3,387,139.3,116.5,70,92.5,91.9,192.5,62.5,124.4,178.1,66.8,155,109,255.9,149,302,50,654.4,53.6,150,51.5,94.2,67,95,62.5,57,95,317.7,156.1,54.5,60,52.5,96.1,52.5],
2019:[339.3,375,132.4,53,196.5,114.1,165,203.7,282.8,127.4,52,102.9,130,140.5,229.5,304.2,88,109,460.6,66.7,307,296.8,209.1,56.5,304.6,112.5,66,76,184,54,222,184.6,202,63.5,225.5,219.3,130.9,51.7,60.2,61.8,61.5,417.6,90,108.5,131.5,248,61,91.3,97.3,138.1],
2020:[0.75,5,4.3,4,12,75,125,100,4,20,5,45,24,36,70,100,8,64,40,10,40,37,50,240],
2021:[71,54,92,100,100,100,68.5,300,365,150,51,137.65,294.17,240,58.37,70,63.5,53,70],
2022:[400.9,340.1,1250,56,70,100,118,105.7,57.6,216.3,115,266.9,500,73,105,54,150.7,100,50,180.5,117.7,205,66,1200,63.89,500,50.5,70,184.5,57.7,134,61.5,209.2,243.5,135.2,63.1,110.3,194.5,431,105]}


while True:
    a12345 = int(input("Please Enter between 2002 and 2022: "))
    if a12345 > 2022:
        print("Sorry! I have list till 2022 only")
        continue
    elif a12345 < 2002:
        print("Sorry! I dont able to fetch data from that much old times")
        continue
    else:
        print("Ok Printing list of Movies from",a12345)
        time.sleep(0.5)
        print("OMG I have length of",len(liyear[a12345]))
        time.sleep(0.5)
        print("How much you want")
        while True:    
            s = len(liyear[a12345])
            asdf = int(input("You want top how much movie: "))
            if asdf==0 or asdf>s:
                print("Please Enter a Valid value between 1 and",s)
                continue
            else:
                print(["Name of Movie","Budget","Earned","Profit Percentage"])
                print()
                time.sleep(1)
                for i in range(asdf):
                    ps = ((liearn[a12345][i])/libudget[a12345][i])*100
                    print(i+1,".",liyear[a12345][i],"----",libudget[a12345][i],"Crores","----",liearn[a12345][i],"Crores","----",round(ps),"% Profit")
                    time.sleep(0.5)
            break
    break
        

print("So Here is your list")
time.sleep(0.5)
print("If you want to know the source site Press 1")
time.sleep(0.5)
print("If you want to exit the application Press 2")
time.sleep(0.5)



while True:
    a567 = int(input("Press between 1 to 2: "))
    if a567 == 2:
        import exitapplication
        import exitapplication
        break
    elif a567 == 1:
        print("I Collected info from different sites by searching every movie (over 500) movies on Google")
        time.sleep(0.5) 
        continue
    else:
        print("I think You mistakenly press the wrong key , Its Okay I will Ask you Again")
        time.sleep(0.5)
        print("If you want to know the Source Site of the info Then Press 1")
        time.sleep(0.5)
        print("If you want to exit the application Then Press 2")
        time.sleep(0.5)
        continue