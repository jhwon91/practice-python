#Data Types
#String
# print("Hello"[0])

#Int
# print(123_456)

# input_number = input()
# print(type(input_number))
# first = int(input_number[0])
# second= int(input_number[1])
# print(first + second)

#BMI
# height = float(input())
# weight = int(input())
# BMI = weight/height ** 2
# print(int(BMI))

#f-string
# score = 0
# height = 1.8
# isWinning = True
# print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")

#삶의 주
# age = int(input())
# rest = (90 - age) * 52
# print(f"you have {rest} left.")

#final project
print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
split_people = int(input("How many people to split the bill?"))
tip /= 100 
total = total * (tip+1)
each_cost = (total/split_people)
# print(f"Each person should pay: ${round(each_cost,2)}")
each_cost = "{:.2f}".format(each_cost)
print(f"Each person should pay: ${each_cost}")






