print("Welcome to car rentals!")

while input("Would you like to continue (y/n)? ") =='y': 

    costemer_code = input("Customer code (b or d): ") 
    days = int(input("Number of days: ")) 
    odom_start = int(input("Odometer reading at the start: "))
    odom_end = int(input("Odometer reading at the end: "))
    miles_driven =odom_end-odom_start # reikna hversu margir Km vorukeyðir

    if costemer_code == 'b':
        cost = days*40+miles_driven*0.25
    elif costemer_code == 'd':
        miles_driven_per_day = (miles_driven/days)-100 # reiknar út km keyrða á dag ásamt að finna hversu mikið umfarm var farið ef talan er neikævð þá er keyrt undir 100km
        if miles_driven_per_day<0:  # tékka hvort km keyðir á dag séu undir 100
            cost = days*60 # ef það er keyrðir undir 100 km á dag bætist ekki við aukakostnaður
        else:
            cost = days*60+miles_driven_per_day*0.25*days   
    print("Miles driven:",miles_driven)
    print("Amount due:", float(round(cost,1))) # nota round til að fá bara ein markverðan aukastaf