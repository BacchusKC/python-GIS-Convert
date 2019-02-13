print("Convert Degrees, Minutes and Seconds. What are the degress to be converted?")
degrees = input()
print("What are the minutes?")
minutes = input()
print("What are the seconds?")
seconds = input()

print degrees,u'\u00b0', minutes,"'",seconds,'"'

decimalDegrees = degrees + float(minutes)/60 + float(seconds)/3600

radianDegrees = decimalDegrees * 3.14159265 / 180

print round(radianDegrees, 3),"Radians"