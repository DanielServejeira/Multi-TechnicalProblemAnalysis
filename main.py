import os
from translates.main_translation import translate
from algorithms.fractional_knapsack_problem import run_fractional_knapsack_interface
from algorithms.boolean_knapsack_problem import run_boolean_knapsack_interface
from algorithms.lcs import run_lcs_interface

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def problem(language: str) -> int:
    problem = -1

    while problem not in [0, 1, 2, 3, 4, 5]:
        print(f"""
            {translate(language, 'author')}\n
                {translate(language, 'problem_choosing')}
                [1] <- {translate(language, 'assignment_problem')}
                [2] <- {translate(language, 'huffman_coding')}
                [3] <- {translate(language, 'fractional_knapsack_problem')}
                [4] <- {translate(language, 'boolean_knapsack_problem')}
                [5] <- {translate(language, 'longest_common_subsequence')}
                [0] <- {translate(language, 'exit')}\n
            """)
        try:
            problem = int(input(f"{translate(language, 'program_functionality')} "))
        except ValueError:  
            print(f"{translate(language, "value_error")}\n")
            clear_screen()

    return problem

opt = -1
supported_languages = 2
program_functionality = -1

while opt < 0 or opt > supported_languages:
    print("""
            Select your language:\n
                [0] <- EN-US
                [1] <- PT-BR\n
          """)
    try:
        opt = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        clear_screen()

language = {0: "en-us",
            1: "pt-br"}

while program_functionality != 0:
    program_functionality = problem(language[opt])

    if(program_functionality == 0):
        break
    elif(program_functionality == 1):
        run_assignment_problem_interface(language[opt])
    elif(program_functionality == 2):
        run_huffman_coding_interface(language[opt])
    elif(program_functionality == 3):
        run_fractional_knapsack_interface(language[opt])
    elif(program_functionality == 4):
        run_boolean_knapsack_interface(language[opt])
    elif(program_functionality == 5):
        run_lcs_interface(language[opt])