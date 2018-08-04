##Arguments class
##contains all the changes essentially
#main game object
from monomial import Monomial, Polynomial


class Arguments():

    def __init__(self,x = 1.0, currency = 0.0, time = 0):
        self.x = x
        self.currency = currency
        self.time = time
        self.polynomial = Polynomial()

    def adv_time(self):
        self.time += 1