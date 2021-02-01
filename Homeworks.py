# this algorithm will subtract values a and b from each other

def simplesub(a, b):
    x = float(a) - float(b)
    return (print(x))


# this algorithm will add three numbers together

def addEm(a, b, c):
    x = a + b + c
    return (print(x))


# this function will create echo of word by how many times you want
def echo(a, b):
    x = b * a
    return (print(x))


def addwords(word1, word2):
    word1 = word1 * 5
    word2 = word2 * 3
    l = word1 + word2
    return (print(l))


# this describes the sum of to values
def sumDescription(value1, value2):
    x = value1 + value2
    return (print("the sum of " + str(value1) + " and " + str(value2) + " is " + str(x)))


def intro(name, town):
    x = "Hello. My name is " + name + ". I love the weather in " + town + "."
    return (print(x))


# HOMEWORK DOC D1 FINISHED
# HOMEWORK DOC 2 Start

# getting midpoint on a set of two coordinates
def getMidpoint(x1, y1, x2, y2):
    xu = (float(x1) + float(x2)) / 2
    yu = (float(y2) + float(y2)) / 2
    return (print([xu, yu]))


# takes 5 values and returns a string indicating the average of those 5 values
def getavgstring(p1, p2, p3, p4, p5):
    x = (p1 + p2 + p3 + p4 + p5) / 5
    return (print("The average value is " + str(x)))


def getmedian(p1, p2, p3, p4, p5):
    x = []
    for i in (p1, p2, p3, p4, p5):
        x.append(i)
    xsort = x.sort()
    return (print(x))


# HW2 done HW3 NEXT
# celcius to farenheit calculator
def ctof(temperature):
    f = round(float(temperature) * 1.8 + 32.00)
    return (print(f))


def ctofwords(temperature):
    celc = temperature
    if celc <= 1000 and celc >= -273.15:
        fahr = round(float(temperature) * 1.8 + 32.00)
        return (
            print("Notice: " + str(celc) + " Degrees Celsius is equivalent to " + str(fahr) + " degrees Fahrenheit."))
    else:
        return (print("Temperature out of range!!!!"))


def whatami(thing):
    y = type(thing)
    x = thing

    if y is int:
        print("integer")
    elif y is str:
        if x.isnumeric():
            print("string made of numbers")
        else:
            l = list(thing)
            p = []
            for item in l:
                if item.isnumeric() is True:
                    return (print("unidentified object"))

                else:
                    p.append(item)
            print("String with letters")

    else:
        print("Unidentified object")


def converttemp(tempurature):
    y = type(tempurature)
    x = tempurature

    if y is int:
        f = round(float(tempurature) * 1.8 + 32.00)
        return (print(f))

    elif y is str:
        if x.isnumeric():
            f = round(float(tempurature) * 1.8 + 32.00)
            return (print(f))

        else:
            l = list(tempurature)
            p = []
            for item in l:
                if item.isnumeric() is True:
                    return (print("i do not understand the input"))

                else:
                    p.append(item)
            print("Enter digits not letters.")

    else:
        print("I do not understand the input")


# HW DS4 below
# this problem takes two positive integers and returns a statement defining the area
# of a rectangle, if the integers are zero or negative the function will return
# please use positive numbers statement
def problem1(length, width):
    l = length
    w = width
    check = (l, w)
    for x in check:
        if x <= 0:
            return (print("please use positive numbers"))

    p = float(l) * float(w)
    print("the area of the rectangle is " + str(p) + " square inches.")


def problem2(aList):
    if len(aList) % 2 == 0:
        p = 0
        for x in aList:
            p += x

        return (print(str(p)))
    else:
        p = len(aList)
        newlist = []
        for x in aList:
            newlist.append(p)
        return (print(newlist))


def problem3(aList):
    newlist = []
    for x in aList:
        newlist.append(x ** x)
    return (print(newlist))


def problem4(mystring1, mystring2):
    return (print(str(mystring1) + str(mystring2) + str(mystring1)))


# finished hw4 next is hw5
# first function will find the sum off values in odd indices of a list without using built in functions

def getsumodds(given_list):
    """
    Find the sum of odd indices of given list
    :param given_list: list that user inputs
    :return: sum of odd indices of list
    """
    sum_odd_indexes = 0
    for i, num in enumerate(given_list):
        if i % 2 != 0:
            sum_odd_indexes += num

    return sum_odd_indexes
