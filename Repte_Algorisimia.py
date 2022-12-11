import random #Import module to make random choices (in this case from numbers 1 to 9)

numbers = [1,2,3,4,5,6,7,8,9] #Define a list with all the numbers that can be used

num = 0 #Create variable that should be the result, starts at 0

#Create a while loop until the result is 2023 this makes a copy of the original 
#list, we'll operate with that one from now in order to not lose the original,
#then make a random choice an remove that choice from the list, so that it can't
#be used again (the number), do this for all 9 numbers, then make the equation.
#Finally print the numbers used and print the result to check that it is in fact 2023.

while num != 2023:
    changing_numbers = numbers.copy()
    first_number = random.choice(changing_numbers)
    changing_numbers.remove(first_number)
    second_number = random.choice(changing_numbers)
    changing_numbers.remove(second_number)
    third_number = random.choice(changing_numbers)
    changing_numbers.remove(third_number)
    fourth_number = random.choice(changing_numbers)
    changing_numbers.remove(fourth_number)
    fifth_number = random.choice(changing_numbers)
    changing_numbers.remove(fifth_number)
    sixth_number = random.choice(changing_numbers)
    changing_numbers.remove(sixth_number)
    seventh_number = random.choice(changing_numbers)
    changing_numbers.remove(seventh_number)
    eighth_number = random.choice(changing_numbers)
    changing_numbers.remove(eighth_number)
    ninth_number = random.choice(changing_numbers)
    print(numbers)
    num = first_number * second_number * third_number * (fourth_number * 10 + fifth_number) - (sixth_number + seventh_number) * eighth_number - ninth_number
    
print(first_number, second_number, third_number, fourth_number, fifth_number, sixth_number, seventh_number, eighth_number, ninth_number)
print(num)