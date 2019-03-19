# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels. 
# The game ends when both players have made all possible substrings. 

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

# For better understanding, see the image below: 

# banana.png

# Your task is to determine the winner of the game and their score.

# Input Format

# A single line of input containing the string . 
# Note: The string  will contain only uppercase letters: .

# Output Format

# Print one line: the name of the winner and their score separated by a space.

# If the game is a draw, print Draw.

# Sample Input

# BANANA
# Sample Output

# Stuart 12

def minion_game(string):
    v = 'AEIOU'
    stuart, kevin, ln = 0, 0, len(s)

    for i in range(ln):  
        if s[i] in v:
            kevin += ln - i
        else:
            stuart += ln - i
        
    if stuart > kevin:
        print('Stuart', stuart)
    elif stuart == kevin:
        print('Draw')
    else:
        print('Kevin', kevin)    
        
if __name__ == '__main__':