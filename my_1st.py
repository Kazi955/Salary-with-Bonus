# read in name as a string
name = str(input())

# read in salary as a float
salary = float(input())

# read in sell as a float
sell = float(input())

# calculate the total salary by adding 15% of the sell value to the base salary
total_salary = salary + (sell * 0.15)

# format the total salary to two decimal places
x = "{:.2f}".format(total_salary)

# print out the total salary with the name prefix and "TOTAL = R$ " prefix
print("TOTAL = R$ " + x)
