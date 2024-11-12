unit_from = input("Enter the unit you are converting from: ") #gets the temperature unit to convert from from the user and stores it in unit_from
unit_to = input("Enter the unit you are converting to: ") #gets the temperature unit to convert to from the user and stores it in unit_to
temperature = float(input(f"Enter the temperature in {unit_from}: ")) #gets the current temperature from the user that is going to be converted to a different unit and stores it in temperature

#checks which conversion the user wants to make (from what unit to what unit) and makes the corresponding conversion given the temperature the user inputted
if unit_from == "Fahrenheit" and unit_to == "Celsius":
    temperature = (temperature - 32) * 5/9
elif unit_from == "Fahrenheit" and unit_to == "Kelvin":
    temperature = ((temperature - 32) * 5/9) + 273.15
elif unit_from == "Fahrenheit" and unit_to == "Fahrenheit":
    temperature = temperature
elif unit_from == "Kelvin" and unit_to == "Fahrenheit":
    temperature = ((temperature - 273.15) * 9/5) + 32
elif unit_from == "Kelvin" and unit_to == "Celsius":
    temperature = temperature - 273.15
elif unit_from == "Kelvin" and unit_to == "Kelvin":
    temperature = temperature
elif unit_from == "Celsius" and unit_to == "Fahrenheit":
    temperature = (temperature * 9/5) + 32
elif unit_from == "Celsius" and unit_to == "Kelvin":
    temperature = temperature + 273.15
elif unit_from == "Celsius" and unit_to == "Celsius":
    temperature = temperature

print(f"That is {temperature:.1f} degrees {unit_to}.") #displays the converted temperature and the unit of that temperature to the user