hys = 0.5
heating_status = 1
heating_fire = 0

trash = 23
home_temp = 22.5

def stop_heating_fire():
    print("Fire is off")
    heating_fire = 0


def start_heating_fire():
    print("Fire is on")
    heating_fire = 1


if(heating_status == 0):
     print('the heating is OFF')

else:
    if(heating_fire == 1 and home_temp >= (trash + hys)):
        stop_heating_fire()

    elif(heating_fire == 0 and home_temp <= (trash - hys)):
        start_heating_fire()

    elif(heating_fire == 0 and home_temp >= (trash - hys)):
        print("The fire is off and the temperature will dicrease")

    elif(heating_fire == 1 and home_temp < (trash + hys)):
        print("The fire is running")

