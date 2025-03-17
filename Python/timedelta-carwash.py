import datetime
import sys

small_time = 30
medium_time = 45
big_time = 60
current_date = datetime.datetime.now() #or datetime.datetime.today() - datetime.now() takes the machine timezone as basis.

while(True):

    car_type = input("Which car size? (s, m or b) or press q to exit\n")

    if car_type.lower() == "s":
        estimated_times = current_date + datetime.timedelta(minutes=small_time)
        print(f"The car was left {current_date.strftime("%d/%m/%Y %H:%M")} and is estimated to be ready at {estimated_times.strftime("%d/%m/%Y %H:%M")}")
        break

    elif car_type.lower() == "m":
        estimated_times = current_date + datetime.timedelta(minutes=medium_time)
        print(f"The car was left {current_date.strftime("%d/%m/%Y %H:%M")} and is estimated to be ready at {estimated_times.strftime("%d/%m/%Y %H:%M")}")
        break

    elif car_type.lower() == "b":
        estimated_times = current_date + datetime.timedelta(minutes=big_time)
        print(f"The car was left {current_date.strftime("%d/%m/%Y %H:%M")} and is estimated to be ready at {estimated_times.strftime("%d/%m/%Y %H:%M")}")
        break
    
    elif car_type.lower() == "q":
        sys.exit("Good bye")

    print("Invalid car size\n")
