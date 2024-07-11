'''
@Author: Nagashree C R
@Date: 2024-07-10 
@Last Modified by: Nagashree C R 
@Last Modified: 2024-07-10 
@Title : Find the sqare root of a number using newton's method
'''

def sqrt(c):
    if c < 0:
        raise ValueError("Input must be a nonnegative number.")
    
    epsilon = 1e-15  # Desired accuracy threshold
    t = c  # Initial guess for square root

    while abs(t - c / t) > epsilon * t:
        t = (c / t + t) / 2.0
    
    return t


# Example usage:
if __name__ == "__main__":
    c = float(input("Enter a nonnegative number: "))
    square_root = sqrt(c)
    print(f"The square root of {c} is approximately {square_root}")
