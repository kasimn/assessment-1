def covert_temperature():
    unit=input("is this temperature in Celsius or Fahrenheit (c/f: ")
    temp=float(input("enter the temperature: "))

    if unit == "c": 
        temp=(9 * temp) / 5 + 32
        print(f"the temperature in Fahrenheit is: {temp}")
    elif unit == "F":
        temp = temp - (32 * 5 / 9)
        print (temp)

convert_temperature()
