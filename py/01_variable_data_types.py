# # Variables and Data Types

name = "Manman"     # String
age = 11            # Integer
weight = 15.7       # Float
is_female = True    # Boolean
school = "Py Bootcamp" # String

print("My name is " + name + " and I am " + str(age) + " years old.")
print("I am studying at " + school + ".")
print("My brother is " + str(age + 5) + " years old.")
print("My younger sister is weighed " + str(weight - 2.2) + "kg")


# celcius to fahrenheit convertor
celsius = 34
fahrenheit = (celsius * 9/5) + 32
print("Today is " + str(fahrenheit) + " degrees Fahrenheit.")

# time convertor
london_time = 12
italian_time = london_time + 1 
local_time = london_time + 7  # Example conversion (5 hours ahead)
print("Local time is " + str(local_time) + ".")
