print("Convert decimal degrees to degrees, minutes and seconds. What are the decimal degrees to be converted?")
decimalDegrees = input()

degrees = int(decimalDegrees)
hold = (decimalDegrees - degrees) * 60
minutes = int(hold)
seconds = round((hold - minutes) * 60,2)

print degrees,u'\u00b0', minutes,"'",seconds,'"'