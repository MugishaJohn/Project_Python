#print("Hello")
#Banking program
import math
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle: "))

    if principle <= 0:
       print("The principle must be greater than zero") 
       principle = float(input("Enter the principle: "))

while rate <= 0:
    rate = float(input("enter the rate: "))

    if rate <= 0:
        print("The rate can not be negative or equal to zero")

        rate = float(input("enter the rate"))

while time <= 0:
    
    time = int(input("Enter the time: "))

    if time <= 0:
        print("The time can not be negative !!")
        time = int(input("Enter the time: "))

interest_period = int(input("Enter the interest period: "))


sign = (interest_period + rate)/rate

value = math.pow(sign,time)
value = math.floor(value)
print(value)

Amount = 0
Amount = float(Amount)

Amount = principle * value
print(f"The entire amount is: {Amount}")


