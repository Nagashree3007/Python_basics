'''
@Author: Nagashree C R
@Date: 2024-07-10 
@Last Modified by: Nagashree C R
@Last Modified: 2024-07-10 
@Title : Find the minium notes given to user as a change anf print the notes given
''' 

def minimum_notes(change):
    sum = 0
    notes = [1000, 500, 100, 50, 10, 5, 2, 1]
    change_list = []  # Initialize the change_list here

    for note in notes:
        while sum + note <= change:
            sum += note
            change_list.append(note)

    return change_list


change = int(input("Enter the change you want: "))

# Calculate the minimum notes
notes_used = minimum_notes(change)

# Using a comprehension to format the output
notes_str = ", ".join(str(note) for note in notes_used)


print(f"The minimum notes for {change} are: {len(notes_used)}")
print(f'the notes are {notes_str}')
