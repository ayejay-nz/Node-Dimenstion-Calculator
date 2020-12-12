import math
import time

from numba import jit

def calculator():
    sigma = 0
    TotalLines = 0
    n = 0

    SideLength = int(input("How long do you want each side to be?\n"))
    Dimension = int(input("What dimension would you like this shape to occupy?\n"))

    start = time.time()
    nodes = SideLength**Dimension #Calculates total nodes or points

    for i in range(1, nodes): #Gets the total unique lines that can be created
        sigma += i

    print(f"\nTotal iteration will be {sigma}\n")

    #Works out total possible combinations
    for x in range(0, sigma):
        a = math.factorial(sigma) 
        b = math.factorial(x) 
        c = sigma**(sigma-x) #Works out colour combinations for iteration
            
        n = (a//b)*c 
        TotalLines += n

        #Prints the progress through iterations
        if x%100 == 0 and x != 0:
            print(f"Will take approx {((time.time() - start)/(x/sigma)) - (time.time() - start)} seconds") #Estimated time of finishing
            print(f"\n{x}\n") #Printes iteration

    print(time.time() - start)
    print(f"\nnum({Dimension}){SideLength} is {len(str(TotalLines))} digits long\n")

    #Writes whole number to txt file
    txtname = f"num({Dimension}){SideLength}.txt"
    with open (txtname, "w") as txtfile:
        txtfile.write(str(TotalLines))

    #Converts to a shortned version to be displayed in scienctific notation
    rounded = round(TotalLines, 11)
    power = len(str(TotalLines)) - 1
    first = str(rounded)[:1]
    last = str(rounded)[1:11]
    scienficic_notation = (f"{first}.{last}x10^{power}")

    #Description of number
    desc = (f"num({Dimension}){SideLength} is {len(str(TotalLines))} digits long ({scienficic_notation})\n")

    #Converts txt file to list and appends new input if unique
    allnums = open("~numsizes.txt")
    allnumslst = allnums.readlines()
    if desc not in allnumslst:
        allnumslst.append(desc)
    allnumslst.sort()

    #Adds sorted back to txt file
    with open ("~numsizes.txt", "w") as numsizes:
        for i in allnumslst:
            numsizes.write(f"{i}")

    print(scienficic_notation)

calculator()