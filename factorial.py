import sys
from timeit import Timer
import csv
import matplotlib.pyplot as plt
sys.setrecursionlimit(150000)

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

values = []
bins = []

with open('C:/Users/Avinash/Desktop/factorial_times.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    with open("C:/Users/Avinash/Desktop/values.txt", 'r') as f:
        for n in f:
            t = Timer(lambda: factorial(int(n)))
            print(t.timeit(number=1))
            values.append(int(n))
            bins.append(t.timeit(number=1))
            # plt.scatter(int(n), t.timeit(number=1))
            writer.writerow([n.strip(), t.timeit(number=1)])

    plt.bar(values, bins)
    plt.show()

