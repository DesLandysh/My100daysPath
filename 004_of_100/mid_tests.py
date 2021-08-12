#import random
import mymodel

#rand_int = random.randint(1, 10)
#print(rand_int)

#print(mymodel.pi)

# from 0.0000.1 to 4.99999999
#random_float = random.random() * 5
#print(random_float)

states_of_us = ["Delaware", "Pennsylvania", "Alabama"]
states_of_us.extend(["Deskitten", "Maria"])
print(states_of_us[3])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches",\
#                "Cherries", "Pears", "Bell peppers", "Celery", "Tomatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
veges = ["Spinach", "Kale", "Tomatoes", "Celety", "Bell peppers"]

dirty_doz = [fruits, veges]
print(dirty_doz)