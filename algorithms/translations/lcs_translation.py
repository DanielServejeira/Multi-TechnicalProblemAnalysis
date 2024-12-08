ptBr = {
    "window_title": "Problema da Subsequência Comum Mais Longa",
    "title": "Problema da Subsequência Comum Mais Longa\n(comparativo com programação dinâmica x recursivo)",
    "string1_label": "String 1:",
    "string2_label": "String 2:",
    "calculate_button": "Calcular",
    "mock_calculate_button": "Calcular (strings aleatórias)",
    "dynamic_result_label": "Subsequência comum mais longa (dinâmico):",
    "dynamic_elapsed_time_label": "Tempo decorrido (dinâmico):",
    "recursive_result_label": "Subsequência comum mais longa (recursivo):",
    "recursive_elapsed_time_label": "Tempo decorrido (recursivo):",
    "seconds": "segundos",
    "exit_button": "Sair"
}

enUs = {
    "window_title": "Longest Common Subsequence Problem",
    "title": "Longest Common Subsequence Problem\n(comparative with dynamic programming x recursive)",
    "string1_label": "String 1:",
    "string2_label": "String 2:",
    "calculate_button": "Calculate",
    "mock_calculate_button": "Calculate (random strings)",
    "dynamic_result_label": "Longest common subsequence (dynamic):",
    "dynamic_elapsed_time_label": "Elapsed time (dynamic):",
    "recursive_result_label": "Longest common subsequence (recursive):",
    "recursive_elapsed_time_label": "Elapsed time (recursive):",
    "seconds": "seconds",
    "exit_button": "Exit"
}

lcs_translation = {
    "pt-br": ptBr,
    "en-us": enUs
}

def translate(language: str, term: str):
    return lcs_translation[language][term]
