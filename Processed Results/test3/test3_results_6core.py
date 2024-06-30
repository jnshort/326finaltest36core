import numpy as np

def main():
    # Value determined from non-deadlocking tests from ndTests folder
    no_deadlock_max = 155000

    print("starting")
    total = np.zeros(999)
    testResults = open("test3_log_6core.txt", "r")
    _ = testResults.readline()
    minimum = np.inf
    maximum = 0
    sum = 0
    no_deadlock = 0 

    for i in range(999):
        line = testResults.readline().strip("\n")
        numAsInt = int(line.split("\t")[0].split(" ")[1])
        total[i] = numAsInt
        if total[i] < minimum:
            minimum = total[i]
        if total[i] > maximum:
            if total[i] > no_deadlock_max:
                no_deadlock += 1
            else:
                maximum = total[i]
        sum += total[i]
    average = sum/999

    print(f"Min: {minimum}")
    print(f"Max: {maximum}")
    print(f"Avg: {average}")
    print(f"No deadlock encountered: {no_deadlock} times")

main()