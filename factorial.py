import sys
from timeit import Timer
import csv
import matplotlib.pyplot as plt
import random
sys.setrecursionlimit(150000)

# returns the factorial of a number
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

values = []
bins = []

with open('factorial_log.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    with open("values.txt", 'r') as f:
        for n in f:
            # returns the average execution time for 20 executions
            t = Timer(lambda: factorial(int(n)))
            time = t.timeit(number=20)
            values.append(int(n))
            bins.append(time)
            # write to a log file
            writer.writerow([random.randint(0,100000), n.strip(), time])

    plt.bar(values, bins)
    plt.show()

