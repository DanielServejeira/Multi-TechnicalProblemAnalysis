enUs = {
    "window_title": "Huffman Coding",
    "title": "Huffman Coding\nFor Compression Of A User Provided Text\n(with greedy algorithm)",
    "string_label": "String:",
    "compress_button": "Compress",
    "generate_string_label": "Generate random string",
    "number_of_characters_label": "Number of characters:",
    "generate_string_button": "Generate String",
    "empty_string_error": "Empty string. Please, insert a string",
    "empty_number_error": "Empty number field. Please, insert a number.",
    "compressed_text": "Compressed text:",
    "huffman_coding_table": "Huffman Coding Table",
    "path_label": "Compressed and decompressed files saved in: ",
    "exit_button": "Exit"
}

ptBr = {
    "window_title": "Codificação de Huffman",
    "title": "Codificação de Huffman\nPara Compressão De Um Texto Fornecido Pelo Usuário\n(com algoritmo guloso)",
    "string_label": "String:",
    "compress_button": "Comprimir",
    "generate_string_label": "Gerar string aleatória",
    "number_of_characters_label": "Número de caracteres:",
    "generate_string_button": "Gerar String",
    "empty_string_error": "Texto vazio. Por favor, insira uma string.",
    "empty_number_error": "Campo de número vazio. Por favor, insira um número.",
    "compressed_text": "Texto comprimido:",
    "huffman_coding_table": "Tabela de Codificação de Huffman",
    "path_label": "Arquivos comprimido e descomprimido salvos em: ",
    "exit_button": "Sair"
}

huffman_coding_translation = {
    "en-us": enUs,
    "pt-br": ptBr
}

def translate(language: str, term: str):
    return huffman_coding_translation[language][term]
