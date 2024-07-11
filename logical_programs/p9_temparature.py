'''
@Author: Nagashree C R
@Date: 2024-07-10 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-10 
@Title : temperature conversion
'''

class Util:
    @staticmethod
    def temp(t,N):
        if N =="f":
            c= (t - 32)*(5/9)
            return c
        else:
            f=(t * 9/5) + 32 
            return  f
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py m d y")
        sys.exit(1)
    
    t = int(sys.argv[1])
    N = sys.argv[2]
    
    
    temperature = Util.temp(t,N)
    print(temperature)
