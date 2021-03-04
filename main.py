#Data Types

#String

print("Hello"[0])

#Integer

print(123 + 345)

123_456_789

#Boolean

True
False

#Parse integer to string

new_num_char = str(6)
print(new_num_char)

#Parse String to float

float("100.5")

#print(70 + float("100.5"))
print(str(70) + str(100.5))


#-----------day-2-1-exercise

number_1 = input("Write number one: ")
number_2 = input("Write number two: ")

number_1_parse = int(number_1)
number_2_parse = int(number_2)

print("The sum of numbers: " + str(number_1_parse + number_2_parse))

#Priority order in calculate number
#PENDAS
#The calculate in Python begin in the left and continue until right
#The operation most important that stand most left will be prioritized in calculate
#()
#** ---> Potentiation
#* /
#+ -

#-----------day-2-2-exercise
#IMC calc

weight = input("Write your weight: ")
height = input("Write your height: ")

calcIMC = float(weight)/(float(height) ** 2)

print("Your IMC is: " + str(calcIMC))

#Arredondamento matemático em Python

#print(round(8 / 3))
#print(round(8/3 , 2))
#print(round(8 // 3))

#A best resource
#f-String
print(f"Your weight: {weight} and your height is: {height}")


#-----------day-2-3-exercise
#Life weeks calc

#A year have 365 days
#A year have 52 weeks
#A year have 12 months

actualYears = input("Write your age in years: ")

yearForCalc = int(actualYears)

amountDays90 = 90 * 365
amountMonths90 = 90 * 12
amountWeeks90 = 90 * 52

amountDaysInput = yearForCalc * 365
amountMonthsInput = yearForCalc * 12
amountWeeksInput = yearForCalc * 52

print(f"You have {amountDays90 - amountDaysInput} days, {amountMonths90 - amountMonthsInput} weeks, and {amountWeeks90 - amountWeeksInput} months left.")