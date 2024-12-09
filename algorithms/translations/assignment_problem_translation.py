enUs = {
    "window_title": "Assignment Problem",
    "title": "Assignment Problem\nWith Branch and Bound",
    "assignments": "Number of assignments:",
    "people": "Number of people:",
    "assignment_weights": "Assignment weights separated by space\n(people x assignments, aij):",
    "calculate_button": "Calculate",
    "generate_weights": "Generate random weights\n(People and assignments fields need to be filled)",
    "from": "From",
    "to": "To",
    "generate_weights_button": "Generate Weights",
    "wrong_weight_amount": "The number of weights is incorrect.",
    "best_solution": "Best solution:",
    "best_cost": "Best cost:",
    "elapsed_time_label": "Execution time:",
    "seconds": "seconds",
    "empty_field_error": "Empty field. Please, insert a number.",
    "infinite": "Infinite",
    "exit_button": "Exit"
}

ptBr = {
    "window_title": "Problema de Associação de Tarefas",
    "title": "Problema de Associação de Tarefas\nCom Branch and Bound",
    "assignments": "Número de tarefas:",
    "people": "Número de pessoas:",
    "assignment_weights": "Pesos das tarefas separados por espaço\n(pessoas x tarefas, aij):",
    "calculate_button": "Calcular",
    "generate_weights": "Gerar pesos aleatórios\n(Os campos de pessoas e tarefas precisam estar preenchidos)",
    "from": "De",
    "to": "Até",
    "generate_weights_button": "Gerar Pesos",
    "wrong_weight_amount": "A quantidade de pesos está incorreta.",
    "best_solution": "Melhor solução:",
    "best_cost": "Melhor custo:",
    "elapsed_time_label": "Tempo de execução:",
    "seconds": "segundos",
    "empty_field_error": "Campo vazio. Por favor, insira um número.",
    "infinite": "Infinito",
    "exit_button": "Sair"
}

assignment_problem_translation = {
    "en-us": enUs,
    "pt-br": ptBr
}

def translate(language: str, term: str):
    return assignment_problem_translation[language][term]