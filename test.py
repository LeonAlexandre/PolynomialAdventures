import os
import math
from monomial import Monomial
from input_parser import InputString

def adv_time(time):
    return time + 1

class arguments():

    def __init__(self,x = 1.0, currency = 0.0, time = 0):
        self.x = x
        self.currency = currency
        self.time = time



def test_it():
    print('Hello')
    print('This is really fun! I love my life!')

    highest_degree = 0

    print('Highest degree: ' + str(highest_degree))

    mono_list = []

    loop = 6

    for i in range(loop):
        mono_list.append(Monomial(1,i,0.1))
        highest_degree += 1


    print('Passing parameter 1.6')
    polysum = 0.0
    for i in range(highest_degree):
        res = mono_list[i].compute_monomial(1.6)
        print(str(i)+'th polynomial = '+ str(res))
        polysum += res

    print('Final result = ',polysum)

def main():


    #main variables initalization
    args = arguments()
    #polynomial


    print(args.time)


    #test_it()

if __name__ == '__main__':
    main()