import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

program_functionality = 0
language = 0
supported_languages = 2

while language not in [1, 2]:
    print("""
            Select your language: 
            [1] <- English
            [2] <- Portuguese\n
          """)
    try:
        language = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        clear_screen()

if language == 1:
    
elif language == 2:
    

while program_functionality not in [1, 2, 3, 4, 5]:
    print("""
            By Daniel Servejeira & Pedro Alonso Oliveira\n
            The program will:
            [1] <- Assignment Problem
            [2] <- Huffman Coding
            [3] <- Fractional Knapsack Problem
            [4] <- Knapsack Problem
            [5] <- Longest Common Subsequence\n
          """)
    try:
        program_functionality = int(input("Enter your choice: "))
    except ValueError:  
        print("Please enter a valid number.\n")
        clear_screen()
        
    clear_screen()

    if program_functionality == 1:
        
        
    elif program_functionality == 2:
        
    
    elif program_functionality == 3:
        
    
    elif program_functionality == 4:
        

    elif program_functionality == 5:
        