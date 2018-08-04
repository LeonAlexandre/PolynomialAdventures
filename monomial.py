import math

class Monomial():
    # has the form coeff * x ^ degree

    def __init__(self, coeff = 0.0, degree = 0, coeff_step = 0.1):
        self.coeff = coeff
        self.degree = int(degree)
        self.coeff_step = coeff_step



    def increase_coeff(self):
        self.coeff += self.coeff_step

    def compute_monomial(self,x):
        return (self.coeff * math.pow(x, self.degree))
        



