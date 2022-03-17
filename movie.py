
global booktik
booktik = 0

def t_movie():
    global booktik
    booktik = booktik+1
    print("which movie do you want to watch?")
    print("1.BEAST ")
    print("2.RRR")
    print("3.VIKRAM")
    print("4.back")
    movie = int(input("choose your movie: "))
    if movie == 4:
     center()
     theater()
     return 0
    if booktik == 1:
      theater()

def theater():
    print("which screen do you want to watch movie: ")
    print("1.SCREEN 1")
    print("2.SCREEN 2")
    print("3.SCREEN 3")
    a = int(input("choose your screen: "))
    ticket = int(input("number of ticket do you want?: "))
    print(str(ticket)+"  ticket booked successfully")

    timing(a)

def timing(a):
    time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    time2 = {
        "1": "10.15-1.15",
        "2": "1.25-4.25",
        "3": "4.35-7.35",
        "4": "7.45-10.45"
    }
    time3 = {
        "1": "10.30-1.30",
        "2": "1.40-4.40",
        "3": "4.50-7.50",
        "4": "8.00-10.45"
    }
    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        print("successful!, enjoy movie at "+x)
        print("*************** Thank you for using  ticket booking app ************************")


    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("successful!, enjoy movie at "+x)
        print("*************** Thank you for using  ticket booking app ************************")


    elif a == 3:
        print("choose your time:")
        print(time3)
        t = input("select your time:")
        x = time3[t]
        print("successful!, enjoy movie at "+x)
        print("*************** Thank you for using  ticket booking app ************************")


    return 0


def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        cinema()
    else:
        print("wrong choice")


def center():
    print("Select seat Sliver-Gold-Platinam ")
    print("1.Sliver-150")
    print("2.Gold-200")
    print("3.platinum-250")
    print("4.back")
    a = int(input("choose your option: "))
    movie(a)
    return 0

def cinema():
    print("**********welcome to movie ticket booking:********** ")
    print("where you want to watch movie?:")
    print("1.inox")
    print("2.pvr ")
    print("3.santhi ")
    th = int(input("choose your option: "))
    if th == 1:
     center()
    elif th == 2:
      center()
    elif th == 3:
      center()
    else:
     print("wrong choice")


cinema() 
