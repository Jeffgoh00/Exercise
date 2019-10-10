weight = int (input ('Fill in your weight:'))
high = int (input ('Fill in your high: '))

BMI = weight/high
print (BMI)

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