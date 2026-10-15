#conditional if/else logic- these are keywords that instruct your
#program to do specific instuctions based on specific data


# condititional syntax (how it is written)
bill_amount = int(input("please type bill tender"(1,5,10)))

#if usually indicates that something is a possible option















#using the calaulator functions from the calculator.py file,
#create a main calculator function that uses if/else logic to
#allow the user to select different alithmetic operations and 
#than perform those operations by runing their repective functions

#Example an input where if the user enter 1, it will run the addition functions
#1= addition()
#2= subtractions()
#3= multipcation()
#4= division

def calculate_subtract():
    print("program has started: please type 2 numbers to subtract")
    num1 = int (input())
    num2 = int (input())
    print (num1+num2)

def calculate_addition():
    print("program has started: please type 2 numbers to add")
    num1 = int (input())
    num2 = int (input())
    print (num1+num2)

def calculate_multipcation():
    print("Program has started: please type 2 numbers to multipcation")
    num1 = int (input())
    num2 = int (input())
    print (num1+num2)

def calculate_division():
    print("program has started: please type 2 numbers to division")
    num1 = int (input())
    num2 = int (input())
    print (num1+num2)

chioic = input ("please a number")

if chioic == 1:
    calculate_add()
elif chioice ==2:
    calculate_subtract()
elif chioic == 3:
    calculate_multiply()
elif chioic == 4:
    calculate_division()



age = int(input())

if age < 7:
    print(8.00)
elif age > 8 and age < 20:
    print (12.00)
elif age > 21 and age < 60:
    print (20.00)
elif age > 61:
    print(0.00)



    def movieTicket():
        print("welcome to movie theater. please type age:")
        age = int(input)
        if age <= 7:
            print (your ticket is $8.00.)
        elif 