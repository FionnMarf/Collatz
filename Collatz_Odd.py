
###############################################################################
#Collects and counts iterations of the Collatz Hailstone function
#This one counts the number of odd iterations (n1 = 3n + 1) for n to go to 1
#in a given positive integer range
#Some code is redundant as I am not using it specifically at the moment
#this code is either commented out or not called for convenience.
#The Binary nature of this conjecture means it makes sense to have intervals
#between powers of 2.
###############################################################################


from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
y_n = []
y1 = []
x = []
y = [] #x and y axis for graphing
x1 = [y]
ys = set()
count = []
x_n = list(set(y)) #removes any duplicates in the list y then adds y to x_n
def main(start, end):
    with open('Csolution_length_1k.txt', 'w') as pathway:
        for i in range(start, end):
            term = Collatz_Len(i)
            #pathway.write('n = ' +'{}'.format(i) + '\t'
            # + 'n\' = ' + str(len(term)) + '\n')
            x.append(i) #add i to the list x
            y.append(term) #add term to the list y
            ys.add(term) #make term an element of ys
            #y.sort()
            #count_var = list([ys])
        #for k in x_n:
            #print k
            #often = freq(k)
            #y_n.append(often)


#def freq(n):
    #if n in x_n:
        #frequency = y.count(n)
        #return frequency
    #else:
        #return 0


def Collatz_Len(element):
    number = 0 #counts the number of iterations
    sequence = [element]
    while element > 1: #halts the function once element = 1
        if element % 2 == 0: #if element is even
            element = element/2
        else:
            element = 3 * element + 1
            number = number + 1 # increments number by 1 at each n%2=1
    return number #returns the set sequence to where collatz was called

#The below function is useful if you want to write the solution path to a file
def collatz(element): #Function for other Collatz investigations, Redundant here
    sequence = [element]
    while element > 1:
        if element % 2 == 0: #if element is even
            element = element/2
        else:
            element = 3 * element + 1
        sequence.append(element) # adds element to the set sequence
    return sequence #returns the set sequence to where collatz was called


if __name__ == '__main__': #runs the function main(a, b)
    main(1, 10000) #interval should ideally be powers of 2
    print 'Task Completed'
    print ys
    print len(ys) #Prints number of unique solution paths
    print Counter(y) #Prints number of each unique path in the interval
    #x_n = [ys]
    plt.plot(x, y, 'b+')
    #plt.hist(y1, bins=y)
    plt.axis([0, 100000, 0, 200])
    plt.xlabel('n')
    plt.ylabel('n\'')
    plt.grid(True)
    plt.show()
