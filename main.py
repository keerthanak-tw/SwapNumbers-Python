# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def swaps(array):
    noOfSwaps = 0
    for i in range(len(array)):
        if array[i] != i+1:
            noOfSwaps += 1
            indexOfElement = array.index(i+1)
            array[i], array[indexOfElement] = i+1, array[i]
    return noOfSwaps


if __name__ == '__main__':
    noOfSwaps = swaps([7, 1, 3, 2, 4, 5, 6])
    print(noOfSwaps)
