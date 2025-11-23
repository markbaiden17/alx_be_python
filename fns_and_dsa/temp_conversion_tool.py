FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahreinheit):
    return (fahreinheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahreinheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        unit = input("Is this temperature in Celsius or Fahreinheit? (C/F): ") .strip() .upper()

        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")

        elif unit == 'C':
            converted_temp = convert_to_fahreinheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")

        else:
            print("Invalid unit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

main()