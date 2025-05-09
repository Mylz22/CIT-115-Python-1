flt_temp = float(input("Enter the Temperature: "))

str_unit = input("Enter 'F' for Fahrenheit or 'C' for Celcius: ")

if str_unit not in ('f', 'C')
    print("Enter a F or C")
    exit()

if str_unit == 'F':
    if flt_temp > 212:
        print("Temp can not be > 212")
    else:
        flt_celcius = (5.0 / 9) * (flt_temp - 32)
        print(f"The Celcius equivalent is: {flt_celcius: .1f}}")
else: # str_unit == 'C'
    if flt_temp > 100:
        print("Temp can not be > 100")
    else:
        flt_fahrenheit = ((9.0 / 5.0) * flt_temp) + 32
        print(f"The Fahrenheit equivalent is: {flt_fahrenheit}")
