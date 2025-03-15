def hotel_cost(days):
    return 140*(days)
def plane_ride_cost(city):
    if "Charlatte" == city:
        return 183
    elif "Tampa" == city:
        return 220 
    elif "Pittisburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475
def rental_car_cost(days):
    if days >= 7 :
        return 40*days-50
    elif days >= 3 :
        return 40*days-20
    else:
        return 40*days
def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money
print("The cost of the car rental was",rental_car_cost(5))
print("The cost of the planer ride was",plane_ride_cost("Los Angeles"))
print("The cost of the car rental was",hotel_cost(9))
print("\n The cost in total was",hotel_cost(9))



    