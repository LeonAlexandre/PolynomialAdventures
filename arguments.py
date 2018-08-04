##Arguments class
##contains all the changes essentially
#main game object
from monomial import Monomial, Polynomial


class Arguments():

    def __init__(self,x = 1.0, currency = 0.0, time = 0):
        self.x = x
        self.x_step = 0.1
        self.currency = currency
        self.time = time
        self.polynomial = Polynomial()

    def adv_time(self):
        self.time += 1


    def upgrade(self,arg_list):
        #order of upgrade:
        #monomial or x
        #if monomial, degree
        #if degree not used, buy and create it
        #otherwise increment it by its coeff_step
        #if x, increment x by x_step

        #update the currency!!

        if not arg_list:
            print('UPGRADE ERROR: Plase specify arguments')
        elif arg_list[0] == 'monomial':
            if len(arg_list) < 2:
                print('ERROR: Please specify degree')
            else:
                deg = int(arg_list[1])
                if type(deg) is float:
                    print('Please specify degree as int')
                elif deg > self.polynomial.highest_degree:
                    self.polynomial.add_monomial(0.1,0.1)
                else:
                    self.polynomial.monomial_list[deg].increase_coeff()


        
        elif arg_list[0] == 'x':
            self.x += self.x_step


        else:
            print('Invalid upgrade arguments')
