# Write a method that will take in a number of minutes, and returns a
# string that formats the number into `hrs:minutes`.
#
# Difficulty: easy.

def time_conversion(min):
	hr = 0
	while min >= 60:
		hr = hr + 1
		min = min - 60
	if min < 10:
		min = ("0" + str(min))
	print (hr + ":" + min)
	
	return (str(hr) + ":" + str(min))



print('time_conversion(15) == "0:15": ' + str(time_conversion(15) == '0:15'))
print('time_conversion(150) == "2:30": ' + str(time_conversion(150) == '2:30'))
print('time_conversion(360) == "6:00": ' + str(time_conversion(360) == '6:00'))
