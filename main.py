import os
import importlib

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def program_functionality(language: int) -> int:
    program_functionality = 0

    if language == 1:
        while program_functionality not in [1, 2, 3, 4, 5]:
            print("""
                    By Daniel Servejeira & Pedro Alonso Oliveira\n
                    Choose a problem:
                    [1] <- Assignment Problem
                    [2] <- Huffman Coding
                    [3] <- Fractional Knapsack Problem
                    [4] <- Boolean Knapsack Problem
                    [5] <- Longest Common Subsequence\n
                """)
            try:
                program_functionality = int(input("Enter your choice: "))
            except ValueError:  
                print("Please enter a valid number.\n")
                clear_screen()

    elif language == 2:
        while program_functionality not in [1, 2, 3, 4, 5]:
            print("""
                    Por Daniel Servejeira & Pedro Alonso Oliveira\n
                    Escolha um problema:
                    [1] <- Problema de Associação de Tarefas
                    [2] <- Codificação de Huffman
                    [3] <- Problema da Mochila Fracionária
                    [4] <- Problema da Mochila Booleana
                    [5] <- Problema da Subsequência Comum Máxima\n
                """)
            try:
                program_functionality = int(input("Digite sua escolha: "))
            except ValueError:  
                print("Por favor digite um número válido.\n")

    return program_functionality

program_functionality = 0
language = 0
supported_languages = 2

functionality_map = {
    1: "assignment_problem",
    2: "huffman_coding",
    3: "fractional_knapsack_problem",
    4: "boolean_knapsack_problem",
    5: "lcs"
}

while language < 1 or language > supported_languages:
    print("""
            Select your language: 
            [1] <- English (Coming soon)
            [2] <- Portuguese\n
          """)
    try:
        language = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.\n")
        clear_screen()

if language == 1:
    interface_path = english_interfaces_path
elif language == 2:
    interface_path = portuguese_interfaces_path

program_functionality = program_functionality(language)

module_name = functionality_map.get(program_functionality)

if module_name:
    try:
        # Dynamically import the module and run the function
        module = importlib.import_module(f"{interface_path}.{module_name}")
        run_function = getattr(module, f"run_{module_name}_interface")
        run_function()  # Call the function
    except (ImportError, AttributeError) as e:
        print(f"Error: {e}")