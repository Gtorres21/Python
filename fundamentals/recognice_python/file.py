num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit))
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])


if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

#The above block will print "It's Lower"

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")


    #The above block will print "Just Right"!

for x in range(5): 
    print(x) #Prints 1,2,3,4
for x in range(2,5):
    print(x)   #Prints 2,3,4,
for x in range(2,10,3): #In range of 2-10 not including 10 in increments of 3
    print(x) #prints 2,5,8 
x = 0 #Varible x = 0 
while(x < 5): #While loop is less than 5
    print(x) #prints x 
    x += 1 #each loop adds 1 

pizza_toppings.pop()  #Removes Last value
pizza_toppings.pop(1) #removes value index [1]

print(person) #prints variable person
person.pop('eye_color') #removes key "eye_color"
print(person) # prints updated variable person

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times() #prints the above function 10 times

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #runs the above function 4 times

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')  

print_hello_x_or_ten_times()  #prints hello 10
print_hello_x_or_ten_times(4) #prints hello 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)