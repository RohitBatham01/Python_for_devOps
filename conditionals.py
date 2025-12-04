day_of_week=input("Enter the day os week: ").lower()  # take input from user    .upper() for uppercase
print("Day of week is:", day_of_week)  # print the day of week

if day_of_week=="saturday" or day_of_week=="sunday":  # check if day is Sat urday or Sunday
    print("i will workhard 2x") 
else:
    print("i will workhard")

num1=input("Enter first no.: ")  # take input from user
num2=input("Enter second no. :")  # take input from user

choice = input("Enter the operation: (Options + , - , * , / , %) ")  # take input from user for operation

if choice== "+":
    sum_of_numbers=float(num1)+float(num2)  # add two numbers after converting string to float   Type Casting
    print("addition",sum_of_numbers)  # print the sum

elif choice== "":
    sum_of_numbers=float(num1)-float(num2) 
    print("subtraction",sum_of_numbers)

elif choice== "*":
    sum_of_numbers=float(num1)*float(num2) 
    print("multiplication",sum_of_numbers)

elif choice== "/":
    sum_of_numbers=float(num1)/float(num2) 
    print("division",sum_of_numbers)

elif choice== "%":
    sum_of_numbers=float(num1)%float(num2) 
    print("remainder",sum_of_numbers)

else:
    print("invalid choice")