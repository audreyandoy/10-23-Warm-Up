# CONCEPT REVIEW

#variables
book = "Harry Pott"
number = 27

# loops
for i in range(3):
    print("hello")

# conditionals
if book == "Harry Potter":
    print("That's a magical book")
else:
    print("That's not a book")

''''
# functions
def add():
    global number
    print(number)
    number = 55
    print(number)
add()

print(number)

'''

# lists
wish_list = ["new car", "covid to be over", "2020 to be over"]

#length
print(len(wish_list))
wish_list.append("I don't know")
print(wish_list)
wish_list.pop(0)
print(wish_list)
wish_list.remove("2020 to be over")
print(wish_list)
print(len(wish_list))

for i in wish_list:
    print(i)