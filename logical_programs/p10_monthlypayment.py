'''
@Author: Nagashree C R
@Date: 2024-07-10 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-10  
@Title : Find the monthly payment should be done based on pI,year,Rate of intrest.
'''

class util:
    @staticmethod
    def monthlypayment(p,y,r):
        n=12*y
        R=r/(12*100)
        payment=p*R/(1-(1+R)**(-n))
        return payment
    
    
import sys


if __name__=='__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py m d y")
        sys.exit(1)
    p=int(sys.argv[1])
    y=int(sys.argv[2])
    r=int(sys.argv[3])
    result=util.monthlypayment(p,y,r)
    print(result) 