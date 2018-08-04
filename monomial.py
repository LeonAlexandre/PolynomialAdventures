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

class Polynomial():

    def __init__(self):
        self.monomial_list = []
        self.monomial_list.append(Monomial(0.1,0,0.1))
        self.highest_degree = 0
        self.contrib_list = []
        
        
    def add_monomial(self,coeff, coeff_step):
        self.monomial_list.append(Monomial(coeff,self.highest_degree + 1,coeff_step))
        self.highest_degree +=1

    def compute_polynomial(self,x):
        polysum = 0.0
        for i in range(self.highest_degree + 1):
            res = self.monomial_list[i].compute_monomial(x)
            polysum += res
        return polysum

    def contrib(self,x):
        #returns a list of contributions
        return [1]
