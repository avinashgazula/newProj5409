import csv
from timeit import Timer
import matplotlib.pyplot as plt
dp = [0, 1] 
	
while len(dp) < 21: 
    dp.append(0) 

def fibonacci(n): 
	if n <= 1: 
		return n 
	else: 
		if dp[n - 1] == 0: 
			dp[n - 1] = fibonacci(n - 1) 

		if dp[n - 2] == 0: 
			dp[n - 2] = fibonacci(n - 2) 
			
	dp[n] = dp[n - 2] + dp[n - 1] 
	return dp[n] 
	
values = []
bins = []

with open('C:/Users/Avinash/Desktop/fibonacci_times.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    with open("C:/Users/Avinash/Desktop/values.txt", 'r') as f:
        for n in f:
            t = Timer(lambda: fibonacci(int(n)))
            values.append(int(n))
            bins.append(t.timeit(number=1))
            print(t.timeit(number=1))
            writer.writerow([n.strip(), t.timeit(number=1)])

    plt.bar(values, bins)
    plt.show()

