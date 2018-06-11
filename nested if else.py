def drive(car_speed):
    if car_speed>200:
        print("you are insane,man")
    elif car_speed>100:
        print("too fast")
    elif car_speed>70 and car_speed<80:
        print("the optimal speed for your car")
    else:
        print("you are driving below the speed limit")
c=int(input("enter no"))
drive(c)