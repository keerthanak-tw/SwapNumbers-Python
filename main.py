# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from pip._vendor.distlib.compat import raw_input


def swaps(inputArray):
    noOfSwaps = 0
    for i in range(len(inputArray)):
        if inputArray[i] != i+1:
            noOfSwaps += 1
            indexOfElement = inputArray.index(i + 1)
            inputArray[i], inputArray[indexOfElement] = i + 1, inputArray[i]
    return noOfSwaps


if __name__ == '__main__':
    noOfElements = input()
    inputArray = raw_input()
    array = [int(x) for x in inputArray.split(",")]
    noOfSwaps = swaps(array)
    print(noOfSwaps)
