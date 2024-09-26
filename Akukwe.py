grade = int(input("What is your present grade?"))
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'

sign = ""
Last_digit = grade % 10

if Last_digit >= 7:
    sign = '+'
elif Last_digit < 3:
    sign = '-'
else:
    sign = ""

if grade >= 93:
    sign = ""

if letter == 'F':
    sign = ""


print(f"Your letter grade is : {letter}{sign}")

if grade >= 70:
    print('congratulation you passed the class!')
else:
    print("stay focused and you'll get it next time!")