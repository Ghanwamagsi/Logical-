#check if a given number is positive, negtive, or zero.

num=float(input("enter a number:"))
if num>0:
    print("positive number.")
elif num==9:
    print("zero")
else:
    print("negative number")

#create a program that tasks the user to enter their exam score and prints out their grade based on the following criteria: A(90-100)
#B(80-89), C (70-79), D (60-69), F(below 60).


exam_score = int(input("enter exam score:"))

if exam_score >= 90:
    print("Grade: A")
elif 80 <= exam_score <=89:
    print("Grade: B")
elif 70 <= exam_score <=79:
    print("Grade: C")
elif 60 <= exam_score <= 69:
    print("Grade: D")
else:
    print("Grade: F")


#takes a user's input of two numbers and prints out the maximum and minimum among them.
    
num1= float(input("enter the first number:"))
num2= float(input("enter the second number:"))
maximum = max(num1,num2)
minimum = min(num1,num2)
print("The maximum number is:", maximum)
print("The minimum number is:", minimum)


#write a python script to determine whether a given year is a leap year or not.


year = int(input("enter a year.:"))
if year%4==0:
    if year %100==0:
        print(year, "is is leap.")
        if year%400==0:
          print(year,"is not leap year.")
        else:
            print(year, "is a leap year.")

#prompts the user to enter two numbersand prints out larger of the two.

num1= float(input("enter a larger number:"))
num2= float(input("enter both number is equal:"))
if num1>num2:
    print("The lager number is:", num1)
elif num1<num2:
    print("The larger number:", num2)
else:
    print("Both numbers are equal")


#create a program that tasks the user to enter their age and prints out wheather they are a child, teenager, adult, or senior citizen.
    
age = int(input("ente a your age."))
if age<13:
    print("you are a child")
elif age<20:
    print("you are a teenager.")
elif age<65:
    print("you are a adult.")
else:
    print("you are a senior citizen.")





