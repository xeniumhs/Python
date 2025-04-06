import time

user=input("Enter your name: ")

timestamp=time.strftime('%H:%M:%S')
print("The time is: ",timestamp)
print(time.strftime('%H'))
hour=int(time.strftime('%H'))
min=int(time.strftime('%M'))
sec=int(time.strftime('%S'))



if(hour<12):
        print("Good morning ",user)
elif hour==12 :
        if min == 0 and sec == 0:
            print("Good noon",user)
        else:
            print("Good Afternoon",user)
elif hour>12 and hour<17:
      print("Good Afternoon",user)
elif hour>=17 and hour<21:
      print("Good Evening",user)
else:
    {
        print("Good night",user)
    }