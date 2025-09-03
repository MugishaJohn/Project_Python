# Temperature scale converter program

Temp_degrees = float(input("Enter your temperature degrees: "))

unit = input("Enter your temp scale unit: ")


if unit == "K":
    Temp_degrees = Temp_degrees - 273
    unit = "Kelvin"

    print(f"The degrees are {Temp_degrees} Celsius")

elif unit == "c":
    Temp_degrees = Temp_degrees + 273
    unit = "Celcius"
    print(f"The new weight is{Temp_degrees} Kelvin")
         


else:
    print("You entered an invalid unit,please try again")   

   







