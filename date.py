from datetime import datetime

birthday = "19/04/1975" #dad
mum_birthday = "30/08/1977"
child1_birthday ="17/06/2005"
child2_birthday = "04/09/2008"

birthday_obj = datetime.strptime(birthday, '%d/%m/%Y')
child1birthday_obj = datetime.strptime(child1_birthday, '%d/%m/%Y')
mumbirthday_obj = datetime.strptime(mum_birthday, '%d/%m/%Y')
child2birthday_obj = datetime.strptime(child2_birthday, '%d/%m/%Y')


now = datetime.now()

if(birthday_obj.day == now.day and birthday_obj.month == now.month):
    dad_age = str(now.year - birthday_obj.year)
    print("Happy Birthday Dad! " + dad_age + " today!")

elif(child1birthday_obj.day == now.day and child1birthday_obj.month == now.month):
    child1_age = str(now.year - child1birthday_obj.year)
    print("Happy Birthday Child1! " + child1_age + " today!")
    
elif(mumbirthday_obj.day == now.day and mumbirthday_obj.month == now.month):
    mum_age = str(now.year - mumbirthday_obj.year)
    print("Happy Birthday Mum! " + mum_age + " today!")
    
elif(child2birthday_obj.day == now.day and child2birthday_obj.month == now.month):
    child2_age = str(now.year - child2birthday_obj.year)
    print("Happy Birthday Child2! " + child2_age + " today!")
    
else :
    print("Oh I don't think today is your birthday:\nbut I can tell you how many days until your next one.")

    def get_user_birthday():
#        year auto set but can be asked with:  year = int(input('When is your birthday? [YY] '))
        year = int('08')
        month = int(input('When is your birthday? [MM] '))
        day = int(input('When is your birthday? [DD] '))

        anon_birthday = datetime(year,month,day)
        return anon_birthday


    def calculate_dates(original_date, now):
        date1 = now
        date2 = datetime(now.year, original_date.month, original_date.day)
        delta = date2 - date1
        days = delta.total_seconds() / 60 /60 /24

        return days


    def show_info(self):
        pass

    bd = get_user_birthday()
    now = datetime.now()
    c = int(calculate_dates(bd,now))
    
    if c < 0:
        c= str(abs(c))
        print("That was "+ c +" days ago.")
        exit()
    
    elif c!= 0:
        c = str(int(calculate_dates(bd,now)))
        print("That's in "+ c +" days!")
        c = int(calculate_dates(bd,now))
        exit()
    
    elif c == 0:
        print("Woah! I am truly sorry, I must've been mistaken, that makes your birthday... Today! \nHappy Birthday. ")
        exit()
    
    else:
        exit()
