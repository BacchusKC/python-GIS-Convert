print("Convert degrees, minutes and seconds to decimal degrees. What are the degress to be converted?")
degrees = input()
print("What are the minutes?")
minutes = input()
print("What are the seconds?")
seconds = input()

print degrees,u'\u00b0', minutes,"'",seconds,'"'

decimalDegrees = degrees + float(minutes)/60 + float(seconds)/3600

print decimalDegrees