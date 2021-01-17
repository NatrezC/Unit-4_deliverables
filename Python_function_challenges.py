#1 Write a function named sum_to() that takes a number parameter n and returns the sum of the numbers from 1 to n. For example:

def sum_to(n):
    sum =  0
    for i in range(1 + n):
        sum +=i
    print(sum)

sum_to(6)

sum_to(10)

#2 Write a function named largest() that takes a list parameter and returns the largest element in that list. You can assume the list contents are all positive numbers. For example:

num_list_1 = [10, 4, 2, 231, 91, 54]

# largest =  max(num_list_1)
# print(largest)

num_list_2 = [1,2,3,4,0]
# largest_two =  max(num_list_2)
# print(largest_two)

def largest(num_list_1):
    largest_num = 0
    for num in num_list_1:
        if num >largest_num:
            largest_num = num
    print(largest_num)

largest(num_list_1)

def largest_two(num_list_2):
    largest_num = 0
    for num in num_list_2:
        if num > largest_num:
            largest_num = num
    print(largest_num)

largest_two(num_list_2)

#3 Write a function named occurances() that takes two string parameters and counts the number of occurrances of the second string inside the first string. 

#Write a function named product() that takes an arbitrary number of parameters, multiplies them all together, and returns the product. (HINT: Review your notes on *args).
numbers = [1,2,3,4,5]

def product(numbers):
    product =  1
    for number in numbers:
        product *= number
    print(product)

product(numbers)
    

