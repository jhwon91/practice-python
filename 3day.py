#BMI 2.0

# height = float(input())
# weight = int(input())

# BMI = weight/ height ** 2

# if BMI >= 35:
# 	print(f"Your BMI is {BMI}, you are clinically obese.")
# elif BMI >= 30:
# 	print(f"Your BMI is {BMI}, you are obese.")
# elif BMI >= 25:
# 	print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI >= 18.5:
# 	print(f"Your BMI is {BMI}, you are have a normal weight.")
# else:
# 	print(f"Your BMI is {BMI}, you are have underweight.")


#윤년

# year = int(input())

# if year % 4 == 0:
# 	if year % 100 == 0:
# 		if year % 400 == 0:
# 			print("leap year")
# 		else:
# 			print("not leap year")		
# 	else:
# 		print("leap year")
# else:
# 	print("not leap year")

#피자 주문
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

bill = 0

if size == "S":
	bill += 15
elif size == "M":
	bill += 20
else:
	bill += 25

want_add_pepperoni = input("Do you want pepperoni? Y or N")
if want_add_pepperoni == "Y":
	if size == "S"
		bill += 2
	else:
		bill +=3

want_add_cheese = input("Do you want extra cheese? Y or N")
if want_add_cheese == "Y":
	bill += 1

print(bill)


