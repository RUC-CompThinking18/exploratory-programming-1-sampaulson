#this function takes a list of floats and finds the average of those floats
def average (numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum/float(len(numbers))
    return average

#print 1: with a list of numbers put in directly as an argument
print average([1.0,2.0,3.0])

#print 2: with a variable I created entered as an argument
bloo = [4.5,3.73,60.1]
print average(bloo)

#print 3: with its value returned into a variable
#         and that variable printed to the terminal
choo = average(bloo)
print choo
