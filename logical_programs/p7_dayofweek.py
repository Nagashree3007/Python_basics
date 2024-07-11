''''
@Author: Nagashree C R
@Date: 2024-07-10 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-10 
@Title : find the day based on Date given
'''

class Util:
    @staticmethod
    def dayOfWeek(m, d, y):
        # Ensure inputs are integers
        m = int(m)
        d = int(d)
        y = int(y)
        
        # Calculate the day of the week index
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + (31 * m0) // 12) % 7
        
        # Define dictionary for day names
        dic = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
        
        # Return the day of the week index and its corresponding name
        return d0, dic[d0]

    
    
# Example usage: taking input from command line arguments
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py m d y")
        sys.exit(1)
    
    m = int(sys.argv[1])
    d = int(sys.argv[2])
    y = int(sys.argv[3])
    
    day_of_week_index, day_name = Util.dayOfWeek(m, d, y)
    print(f"Day of the week index: {day_of_week_index}")
    print(f"Day name: {day_name}")
