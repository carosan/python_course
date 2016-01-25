def celsius_fahrenheit(temp_str, temp_num):
	if temp_str == "fahrenheit":
		new_temp = (temp_num - 32) * 5/9
		return new_temp
	elif temp_str == "celsius":
		new_temp = temp_num * 9/5 + 32
		return new_temp
	else:
		print("invalid " + temp_str)
		