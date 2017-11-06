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
x_n = list(set(y))
def main(start, end):
    with open('Csolution_length_1k.txt', 'w') as pathway:
        for i in range(start, end):
            term = collatz(i) #calls the function collatz below
            #pathway.write('n = ' +'{}'.format(i) + '\t'
            # + 'n\' = ' + str(len(term)) + '\n')
            x.append(i)
            y.append(len(term))
            ys.add(len(term))
            #y.sort()
            # writes to and formats the text file.
            #count_var = list([ys])
        for k in x_n:
            print k
            often = freq(k)
            y_n.append(often)


def freq(n):
    if n in x_n:
        frequency = y.count(n)
        return frequency
    else:
        return 0



def collatz(element):
    sequence = [element]
    while element > 1:
        if element % 2 == 0: #if element is even
            element = element/2
        else:
            element = 3 * element + 1
        sequence.append(element) # adds element to the set sequence
    return sequence #returns the set sequence to where collatz was called

if __name__ == '__main__': #runs the function main(a, b)
    main(1, 1000) #interval of (2^25, 2^26)
    print 'Task Completed'
    print ys
    print len(ys)
    print Counter(y)
    #x_n = [ys]
    plt.plot(x, y, 'b+')
    #plt.hist(y1, bins=y)
    plt.axis([1, 100000, 1, 400])
    plt.xlabel('n')
    plt.ylabel('n\'')
    plt.grid(True)
    plt.show()
