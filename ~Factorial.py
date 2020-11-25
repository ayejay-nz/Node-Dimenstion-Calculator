import time
import math

length = int(input("What is the length of the side of the grid?\n"))
dimension = int(input("What dimension would you like the shape to occupy?\n"))
nodes = length**dimension

start = time.time()
sigma = 0
factorised = 1

for i in range(1, nodes):
    sigma += i
print(sigma)

factorised = math.factorial(sigma)

power = len(str(factorised)) - 1
first = str(factorised)[:1]
last = str(factorised)[1:11]
scienficic_notation = (f"{first}.{last}x10^{power}")

print(scienficic_notation)
print(f"Took {time.time() - start} seconds")