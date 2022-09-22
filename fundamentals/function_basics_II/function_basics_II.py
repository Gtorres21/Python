#1.  Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    arr = []
    for i in range(num):
        if num >= 0:
            arr.append(num)
            num = num - 1
    return arr   

print(countdown(5))    




#2.  Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2


def print_and_return(num1,num2):
    arr = [num1,num2]
    print(arr[0])
    return arr[1]

print((print_and_return(4,2)))



#3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
arr = []
def first_plus_length(arr):
    sum = len(arr) + arr[0]
    return sum
print(first_plus_length([1,2,3,4,5]))





# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False


def values_greater_than_second(arr):
    new_arr = []
    if len(arr) < 2:
        return False 
        
    for i in range(0,len(arr)):
        # print(i)
        if arr[i]>arr[1]:
            new_arr.append(arr[i])
        
    print(len(new_arr))

    return new_arr


print(values_greater_than_second([5,2,3,2,1,4]))
        





#5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def this_length_that_value(num1,num2):
    arr = []
    for num1 in range(0,num1):
        num1 = num2
        arr.append(num1)


    return (arr)

print(this_length_that_value(6,2))
