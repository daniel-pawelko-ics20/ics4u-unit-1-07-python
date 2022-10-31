#!/usr/bin/env python3

# Created on: Oct-2022
# Created by: Daniel Pawelko
# Created for: ICS4U
# Spit out csv file with grades and assignments

# Imports
import numpy


def grader(assArr, namesArr):
    # Defining array
    arr = [[0] * len(namesArr) for i in range(len(assArr))]

    # Adding student names
    arr[0] = namesArr
    arr[0].insert(0, "")

    # Adding assignments and grades
    for y in range(1, len(assArr) - 1):
        arr[y][0] = assArr[y]
        for x in range(1, len(namesArr) - 1):
            arr[y][x] = str(round(numpy.random.normal(loc=75, scale=10, size=None)))

    # Returning array
    return arr


def main():
    # Define arrays
    arrNames = []
    arrAss = []

    # Convert file to array
    with open("./names.txt") as file:
        while True:
            line = file.readline()
            if not line:
                file.close()
                break
            arrNames.append(line.rstrip("\n"))

    # Convert file to array
    with open("./ass.txt") as file:
        while True:
            line = file.readline()
            if not line:
                file.close()
                break
            arrAss.append(line.rstrip("\n"))

    # Call function
    returned = grader(arrAss, arrNames)

    # Export String
    exportString = ""

    # Create string to be writtin to file
    for y in range(len(returned) - 1):
        for x in range(len(returned[0]) - 1):
            exportString += returned[y][x]
            exportString += ","
        exportString += "\n"

    # Write to file
    with open("table.csv", "w") as file:
        file.write(exportString)
        file.close()

    # Done
    print("\nDone.")


if __name__ == "__main__":
    main()
