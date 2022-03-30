import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_names = len(names) # number of names
random_choice = random.randint(0, num_names-1) # random number between 0 and number of names
buyer = names[random_choice] # random name
print(buyer)
print(f'{buyer} is going to buy the meal today!')