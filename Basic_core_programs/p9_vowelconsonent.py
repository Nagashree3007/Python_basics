'''
@Author: Nagashree C R
@Date: 2024-07-11
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-11
@Title : find given charecter is vowel or consonent
'''


VOWEL="AEIOU"

def vowel(char):
  if char in VOWEL:
    print(f'{char} is vowel')
  else:
    print(f'{char} is consonent')
    
    
char=input()
char=char.upper()
vowel(char)