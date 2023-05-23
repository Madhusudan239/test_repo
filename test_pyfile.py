import pandas as pd


class test_testcases():
    
    def sumof_num(self, x):
        x1 = x+x
        
        return x1
    
    def multiplication_num(self, y):
        y1 = y*y
        return y1
    
    def number_calculations(self,z):
        sumof = self.sumof_num(z)
        multiplication_of = self.multiplication_num(sumof)
        
        print(multiplication_of)
        return multiplication_of
    
o = test_testcases()
value = number_calculations(z)
    
        
