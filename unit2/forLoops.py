# what is a loop --> code thats repeats.

#while loops = a block code that repeats itself until the triggering
#condition is no longer TRUE. CAN BE INFINTE


#for loops = a type of loop (code block that repeats itself)But
#it is finite

#THINK OF FOR LOOPS AS THE COUNTING LOOP

#FOR LOOP SYNTAX 
# i stand for itertator = programmers decided make this universal
# symbol for a placeholder for counting

for number in range (1,500):
    print(number / 2) 

# list --> a collection type that acts as a container for
#multiple data types

foodItem_1 = "apple"

groceryList = [ 'apples', "oranges", "water","chips", 'grondbeef']

print(groceryList)

for i in groceryList:
    print("i need to buy"+ i)

grades = [100, 98, 75, 77, 89, 80]

for grade in grades:
    # show me the grades lower than 85
    if grade < 85:
        print(grade)

fighterA = ['johnny bravo, 100, 50']
fighterB = ["dexter lab, 120, 40"]

fighter = [fighter_b , fighter_a]

for fightername in fighters:
    print ("name of fighters")




    book_1 = "math"
    book_2 = "social studies"

    book_for_school = book_2, book_1


    inventory = ["weapons", "haling potion", "sheild","armor"]

    # when we want to add an item to list we use the append()method
    inventory.append("spell book")
    print(inventory)

    # list are index based - meaning we can search and find values inside of 
    #list because it structured 

    #To pull a specific value from a list, use the list index position
    # list always start from  0.
    print(inventory[0]) 

    # find the method for removing and item from list- specifically,
    #remove the healing potion

    inventory.remove("healing potion")
    inventory.pop(1)

    print(inventory) 

    #how do we add the healing potion back to our inventory
    #list-specifically at index 3
    inventory.insert(3, "healing potion")
    