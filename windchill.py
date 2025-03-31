def windChill(T, V):
    cal = 35.74 + (0.6215 * T) - 35.75 * (V ** 0.16) + 0.4275 * T * (V ** 0.16)
    return cal

def temConvertor(C):
    # Convert Celsius to Fahrenheit
    return (C * 9/5) + 32

quest = int(input('What is the temperature? '))
unit = input('Fahrenheit or Celsius (F/C)? ').upper()  

# Iterate through wind speeds from 5 to 60 mph, in steps of 5
for V in range(5, 61, 5):
    if unit == 'C':
        converted = temConvertor(quest)
        windcal = windChill(converted, V)
        print(f"At temperature {converted:.1f}F, and wind speed {V} mph, the windchill is: {windcal:.2f}F")
    elif unit == 'F':
        windcal = windChill(quest, V)
        print(f"At temperature {quest:.1f}F, and wind speed {V} mph, the windchill is: {windcal:.2f}F")
