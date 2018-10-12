height = 1.75
weight = 80.5

bmi = weight/height**2

if bmi < 18.5:
	print("too light")
elif 18.5 < bmi <25.5:
	print("normal")
elif 25 < bmi < 28:
	print("too heavy")
elif 25 < bmi < 25:
	print("obsity")
else:
	print("serious obsity")


x = input("please enter a number")
while x < 100:
	if x < 10:
		print("x is smaller than 10")
	elif x < 20:
		print("x is smaller than 20")
	elif x < 50:
		print("x is smaller than 50")
	else:
		print("x is smaller than 100")
	
