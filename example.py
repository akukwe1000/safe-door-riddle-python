def windChill(T, V):
    cal = 35.74 + (0.6215*T) - 35.75 *(V**0.16) + 0.4275* T *(V**0.16)
    return cal

solve = windChill(8, 10)
print(f'the windchill is {solve}')

def temConvertor(C):
    kelvin = C + 273
    return kelvin

msg = int(input('what is the temperature: '))
convert = temConvertor(msg)
print(f'temperature in kelvin is {convert}K')

