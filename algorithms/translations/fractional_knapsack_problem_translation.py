ptBr = {
    "window_title":"Problema da Mochila Fracionária",
    "title":"Problema da Mochila Fracionária\n(comparativo com algoritmo guloso x recursivo)",
    "max_weight_label": "Peso máximo da mochila:",
    "item_values_label": "Valores dos itens (separados por espaço):",
    "item_weights_label": "Pesos dos itens (separados por espaço):",
    "calculate_button": "Calcular",
    "mock_calculate_button": "Calcular (valores aleatórios)",
    "greedy_result_label": "Valor máximo na mochila (guloso):",
    "greedy_elapsed_time_label": "Tempo de execução (guloso):",
    "recursive_result_label": "Valor máximo na mochila (recursivo):",
    "recursive_elapsed_time_label": "Tempo de execução (recursivo):",
    "seconds": "segundos",
    "exit_button": "Sair"
}

enUs = {
    "window_title":"Fractional Knapsack Problem",
    "title":"Fractional Knapsack Problem\n(comparative with greedy algorithm x recursive)",
    "max_weight_label": "Maximum weight of the knapsack:",
    "item_values_label": "Item values (separated by space):",
    "item_weights_label": "Item weights (separated by space):",
    "calculate_button": "Calculate",
    "mock_calculate_button": "Calculate (random values)",
    "greedy_result_label": "Maximum value in the knapsack (greedy):",
    "greedy_elapsed_time_label": "Execution time (greedy):",
    "recursive_result_label": "Maximum value in the knapsack (recursive):",
    "recursive_elapsed_time_label": "Execution time (recursive):",
    "seconds": "seconds",
    "exit_button": "Exit"
}

fractional_knapsack_problem_translation = {
    "pt-br": ptBr,
    "en-us": enUs
}

def translate(language: str, term: str):
    return fractional_knapsack_problem_translation[language][term]