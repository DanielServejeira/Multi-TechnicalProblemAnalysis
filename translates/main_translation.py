enUs = {
    "author": "By Daniel Servejeira & Pedro Alonso Oliveira",
    "problem_choosing": "Choose a problem",
    "assignment_problem": "Assignment Problem",
    "huffman_coding": "Huffman Coding",
    "fractional_knapsack_problem": "Fractional Knapsack Problem",
    "boolean_knapsack_problem": "Boolean Knapsack Problem",
    "longest_common_subsequence": "Longest Common Subsequence",
    "program_functionality": "Enter your choice:",
    "value_error": "Please enter a valid number.",
}

ptBr = {
    "author": "Por Daniel Servejeira & Pedro Alonso Oliveira",
    "problem_choosing": "Escolha um problema:",
    "assignment_problem": "Problema de Associação de Tarefas",
    "huffman_coding": "Codificação de Huffman",
    "fractional_knapsack_problem": "Problema da Mochila Fracionária",
    "boolean_knapsack_problem": "Problema da Mochila Booleana",
    "longest_common_subsequence": "Problema da Subsequência Comum Máxima",
    "program_functionality": "Digite sua escolha:",
    "value_error": "Por favor digite um número válido.",
}

main_translation = {
    "en-us": enUs,
    "pt-br": ptBr
}

def translate(language: str, term: str):
    return main_translation[language][term]