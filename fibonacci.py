import csv
from timeit import Timer
import random
import matplotlib.pyplot as plt

# initialising the dp array
dp = [0, 1] 
	
# add zeroes to the dp array. will be calculated later
while len(dp) < 101: 
    dp.append(0) 

def fibonacci(n): 
	if n <= 1: 
		return n 
	else: 
        # values will be added to dp array when they are calculated
		if dp[n - 1] == 0: 
			dp[n - 1] = fibonacci(n - 1) 

		if dp[n - 2] == 0: 
			dp[n - 2] = fibonacci(n - 2) 

    # computed value for n is added to the dp array	
	dp[n] = dp[n - 2] + dp[n - 1] 
	return dp[n] 
	
values = []
bins = []

with open('fibonacci_log.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    with open("values.txt", 'r') as f:
        for n in f:
            # average time for 20 executions is calculated
            t = Timer(lambda: fibonacci(int(n)))
            time = t.timeit(number=20)
            values.append(int(n))
            bins.append(time)
            # write to csv file
            writer.writerow([random.randint(0, 1000000), n.strip(), time])

    # plot a bar graph
    plt.bar(values, bins)
    plt.show()

