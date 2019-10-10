weight = input ('Fill in your weight:')
high = input ('Fill in your high:')

weight = flaot (weight)
high = float (high)

BMI = weight / high
	print ('your BMI', BMI)

if BMI < 18.5:
	print ('underweight')
elif (BMI >= 18.5 and BMI < 24):
	print ('normal range')
elif (BMI >= 24 and BMI < 27):
	print ('too heavy')
elif (BMI >= 27 and BMI < 30):
	print ('mild obesity')
elif (BMI >= 30 and BMI < 35):
	print ('moderate obesity')
else:
	print ('severe obesity')