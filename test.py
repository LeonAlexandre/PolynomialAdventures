import os
import math
from monomial import Monomial, Polynomial
from input_parser import InputString
from arguments import Arguments






def test_it(args):
    print('Hello')
    print('This is really fun! I love my life!')

    
    args.x = 1.6


    loop = 6

    for i in range(loop):
        args.polynomial.add_monomial(1.0,0.1)
    


    print('Passing parameter 1.6')
    polysum = 0.0
    polysum = args.polynomial.compute_polynomial(args.x)

    print('Final result = ',polysum)


def print_interface(args):
    #print the interface of the game
    print('Polynomial Adventures v0.01')
    print('Currency =', args.currency)
    print('X = ', args.x)
    print('Time = ',args.time)

def main():


    #main variables initalization
    args = Arguments()
    #polynomial

    controller = InputString('none')


    #beginning
    args.x = 2.0
    loop = 6
    #for i in range(loop):
    #    args.polynomial.add_monomial(0.1,0.1)

    #print('Passing parameter 2.0')
    #for testing purposes
    



    #main game loop
    #print interface
    #ask for input
    #perform action
    #compute currency
    while controller.command is not 'stop':
        #print interface
        print_interface(args)

        #asks for input
        input_str = input('Controller:')
        controller.generate_command(input_str)

        #handle input (in action function)
        if controller.command == 'time':
            args.adv_time()
            args.currency += args.polynomial.compute_polynomial(args.x)
        elif controller.command == 'unknown':
            print('Unknown command. type "help" for... well, help')
        elif controller.command == 'none':
            print('')


        #compute currency (only if time)
            
        
    



if __name__ == '__main__':
    main()

##End