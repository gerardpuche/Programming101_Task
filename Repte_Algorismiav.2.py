import random

numbers = [1,2,3,4,5,6,7,8,9] #Define a list with all the numbers that can be used

num = 0 #Create variable that should be the result, starts at 0

while num != 2023:
    random.shuffle(numbers) # Call the shuffle function
    num = numbers[0] * numbers[1] * numbers[2] * (numbers[3] * 10 + numbers[4]) - (numbers[5] + numbers[6]) * numbers[7] - numbers[8]
    
print(numbers)
print(num)