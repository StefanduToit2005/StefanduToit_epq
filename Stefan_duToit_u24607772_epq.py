import math

#the epq function
def calculate_epq(a_d, s_c, h_c, d, p):
 
    return math.sqrt((2 * a_d * s_c) / (h_c * (1 - d / p)))

#Call the function and print the result

#Values
a_d = 12000
s_c = 50
h_c = 2
d = 40
p = 150

epq = calculate_epq(a_d, s_c, h_c, d, p)


#Other calculations:
runs_per_year = a_d / epq
run_length_days = epq / p

#Max inventory Calculation
max_inventory = epq * (1 - d / p)


#Printing results:
print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))

#Increasing the Production rate, decreases the optimal production quantity, increasing the number of production runs per year, and decreasing the length of each run. 
#The maximum inventory level also increases as the production rate increases.  