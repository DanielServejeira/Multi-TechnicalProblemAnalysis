import random
import heapq
import os
from collections import Counter
import tkinter as tk
from tkinter import ttk
from algorithms.translations.huffman_coding_translation import translate


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    frequency = Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    return heap[0]


def generate_huffman_codes(node, prefix="", codes={}):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = prefix

    generate_huffman_codes(node.left, prefix + "0", codes)
    generate_huffman_codes(node.right, prefix + "1", codes)

    return codes


def encode_text(text, huffman_codes):
    return "".join(huffman_codes[char] for char in text)


def decode_text(encoded_text, root):
    decoded_text = []
    current_node = root

    for bit in encoded_text:
        current_node = current_node.left if bit == "0" else current_node.right

        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = root

    return "".join(decoded_text)


def save_compressed_and_decompressed_files(encoded_text, decoded_text):
    folder = "huffman_archives"
    if not os.path.exists(folder):
        os.makedirs(folder)

    compressed_file = os.path.join(folder, "compressed.txt")
    decompressed_file = os.path.join(folder, "decompressed.txt")

    with open(compressed_file, "w") as f:
        f.write(encoded_text)

    with open(decompressed_file, "w") as f:
        f.write(decoded_text)


def huffman_compression(text):
    root = build_huffman_tree(text)
    huffman_codes = generate_huffman_codes(root)
    encoded_text = encode_text(text, huffman_codes)

    decoded_text = decode_text(encoded_text, root)

    save_compressed_and_decompressed_files(encoded_text, decoded_text)

    return encoded_text, decoded_text, huffman_codes


class HuffmanCodingApp(tk.Tk):
    language: str

    def __init__(self, language):
        super().__init__()
        self.language = language
        self.title(translate(language, "window_title"))
        self.geometry("600x550")

        title = ttk.Label(
            self,
            text=translate(language, "title"),
            font=("Arial", 16),
            justify="center",
        )
        title.pack(pady=20)

        self.string_label = ttk.Label(self, text=translate(language, 'string_label'))
        self.string_label.pack()
        self.string_entry = ttk.Entry(self)
        self.string_entry.pack()

        self.compress_button = ttk.Button(
            self,
            text=translate(language, "compress_button"),
            command=self.compress_button,
        )
        self.compress_button.pack(pady=10)

        self.number_of_characters_label = ttk.Label(self, text=translate(language, 'number_of_characters_label'))
        self.number_of_characters_label.pack()
        self.number_of_characters_entry = ttk.Entry(self)
        self.number_of_characters_entry.pack()

        self.generate_string_button = ttk.Button(
            self,
            text=translate(language, "generate_string_button"),
            command=self.generate_string,
        )
        self.generate_string_button.pack(pady=10)

        self.error_label = ttk.Label(self, text=translate(language, 'empty_number_error'), foreground="red")
        self.error_label.pack_forget()

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)

        self.exit_button = ttk.Button(
            self, text=translate(language, "exit_button"), command=self.destroy
        )
        self.exit_button.pack(pady=10)

    def generate_string(self):
        self.string_entry.delete(0, tk.END)
        self.error_label.pack_forget()
        try:
            num_chars = int(self.number_of_characters_entry.get())
            string = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", k=num_chars))
            self.string_entry.insert(0, string)
            self.string = string
        except ValueError:
            self.error_label.config(text=f"{translate(self.language, 'empty_number_error')}")
            self.error_label.pack()

    def compress_button(self):
        input_text = self.string_entry.get()

        if not input_text:
            self.error_label.config(text=f"{translate(self.language, 'empty_string_error')}")
            self.error_label.pack()
            return

        encoded_text, _, huffman_codes = huffman_compression(input_text)

        self.path_label = ttk.Label(self, text="path_label")

        self.binary_compressed_text = ttk.Label(self, text=translate(self.language, 'compressed_text'))
        self.encoded_text = ttk.Label(self, text=encoded_text)

        self.result_label.config(text=f"{translate(self.language, 'compressed_text')} {encoded_text[:50]}...")

        self.huffman_coding_table = ttk.Label(self, text=translate(self.language, 'huffman_coding_table'))
        for char, code in huffman_codes.items():
            self.table = ttk.Label(self, text=(f"'{char}': {code}"))


def run_huffman_coding_interface(language: str):
    app = HuffmanCodingApp(language)
    app.mainloop()
