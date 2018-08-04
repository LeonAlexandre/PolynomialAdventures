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
    print('Currency ={:0.2f}'.format(args.currency))
    print('X = {:0.2f}'.format(args.x))
    print('Time = ',args.time)
    
def print_polynomial(args):
    poly_str = ''
    poly = args.polynomial
    for i in range(poly.highest_degree + 1):
        poly_str += '+ '+ '{:0.2f}'.format(poly.monomial_list[i].coeff) + 'x^'+ str(poly.monomial_list[i].degree)
    print('Polynomial: ' + poly_str)

def actions(args, controller): #perform most actions
    #handle input (in action function)
    if controller.command == 'unknown':
        print('Unknown command. type "help" for... well, help')
    elif controller.command == 'help':
        print('')
    elif controller.command == 'upgrade':
        args.upgrade(controller.arg_list)
    



def main():


    #main variables initalization
    args = Arguments()
    #polynomial

    controller = InputString('none')


    #beginning
    args.x = 2.0
    loop = 6
    #main game loop
    #print interface
    #ask for input
    #perform action
    #compute currency
    while controller.command is not 'stop':
        #print interface
        print_interface(args)
        print_polynomial(args)

        #asks for input
        print('')
        input_str = input('Controller:')
        controller.generate_command(input_str)

        actions(args,controller)

        #Time advances by itself now
        args.adv_time()
        args.currency += args.polynomial.compute_polynomial(args.x)

        #compute currency (only if time)
            

if __name__ == '__main__':
    main()

##End