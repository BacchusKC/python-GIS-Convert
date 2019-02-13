print("Convert radians to degrees, minutes and seconds. What are the radians to be converted?")
radians = input()

decimalDegrees = radians * 180 / 3.14159265
degrees = int(decimalDegrees)
hold = (decimalDegrees - degrees) * 60
minutes = int(hold)
seconds = round((hold - minutes) * 60,2)

print degrees,u'\u00b0', minutes,"'",seconds,'"'