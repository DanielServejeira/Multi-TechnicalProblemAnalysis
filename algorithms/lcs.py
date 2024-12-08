from time import time
import tkinter as tk
from tkinter import ttk
import random
from algorithms.translations.lcs_translation import translate


def dynamic_lcs(S1, S2, m, n):
    # Initialize the matrix with dimensions (m+1) x (n+1)
    L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Building the matrix in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Length of the LCS
    index = L[m][n]

    # Array to store the LCS characters
    lcs_algo = [""] * index

    # Start from the bottom-right corner and trace back
    i, j = m, n
    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            lcs_algo[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_algo)


def recursive_lcs(s1, s2, m, n):
    # Base case: If either string is empty, the LCS is an empty string
    if m == 0 or n == 0:
        return ""

    # If the last characters of both substrings match
    if s1[m - 1] == s2[n - 1]:
        # Include this character in LCS and recur for the remaining substrings
        return recursive_lcs(s1, s2, m - 1, n - 1) + s1[m - 1]
    else:
        # Recur for two cases and take the longer result:
        # 1. Exclude the last character of s1
        # 2. Exclude the last character of s2
        lcs1 = recursive_lcs(s1, s2, m - 1, n)
        lcs2 = recursive_lcs(s1, s2, m, n - 1)
        return lcs1 if len(lcs1) > len(lcs2) else lcs2


class LongestCommonSubsequenceApp(tk.Tk):
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

        self.string1_label = ttk.Label(self, text=translate(language, "string1_label"))
        self.string1_label.pack()
        self.string1_entry = ttk.Entry(self)
        self.string1_entry.pack()

        self.string2_label = ttk.Label(self, text=translate(language, "string2_label"))
        self.string2_label.pack()
        self.string2_entry = ttk.Entry(self)
        self.string2_entry.pack()

        self.calculate_button = ttk.Button(
            self,
            text=translate(language, "calculate_button"),
            command=self.calculate_lcs,
        )
        self.calculate_button.pack(pady=10)

        self.mock_calculate_button = ttk.Button(
            self,
            text=translate(language, "mock_calculate_button"),
            command=self.mock_calculate_lcs,
        )
        self.mock_calculate_button.pack(pady=10)

        self.dynamic_result_label = ttk.Label(self, text="", font=("Arial", 12))
        self.dynamic_result_label.pack(pady=10)

        self.dynamic_elapsed_time_label = ttk.Label(self, text="", font=("Arial", 12))
        self.dynamic_elapsed_time_label.pack(pady=10)

        self.recursive_result_label = ttk.Label(self, text="", font=("Arial", 12))
        self.recursive_result_label.pack(pady=10)

        self.recursive_elapsed_time_label = ttk.Label(self, text="", font=("Arial", 12))
        self.recursive_elapsed_time_label.pack(pady=10)

        self.exit_button = ttk.Button(
            self, text=translate(language, "exit_button"), command=self.destroy
        )
        self.exit_button.pack(pady=10)

    def mock_calculate_lcs(self):
        self.string1_entry.delete(0, tk.END)
        self.string2_entry.delete(0, tk.END)

        s1 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=15))
        s2 = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=15))
        self.string1_entry.insert(0, s1)
        self.string2_entry.insert(0, s2)

        self.calculate_lcs()

    def calculate_lcs(self):
        s1 = self.string1_entry.get()
        s2 = self.string2_entry.get()
        n = len(s1)
        m = len(s2)

        start = time()
        dynamic_result = dynamic_lcs(s1, s2, n, m)
        end = time()
        dynamic_elapsed_time = end - start

        start = time()
        recursive_result = recursive_lcs(s1, s2, n, m)
        end = time()
        recursive_elapsed_time = end - start

        self.dynamic_result_label.config(
            text=f"{translate(self.language, 'dynamic_result_label')}: {dynamic_result} ({len(dynamic_result)} caracteres)"
        )
        self.dynamic_elapsed_time_label.config(
            text=f"{translate(self.language, 'dynamic_elapsed_time_label')}: {dynamic_elapsed_time:.8f} {translate(self.language, 'seconds')}"
        )
        self.recursive_result_label.config(
            text=f"{translate(self.language, 'recursive_result_label')}: {recursive_result} ({len(recursive_result)} caracteres)"
        )
        self.recursive_elapsed_time_label.config(
            text=f"{translate(self.language, 'recursive_elapsed_time_label')}: {recursive_elapsed_time:.8f} {translate(self.language, 'seconds')}"
        )


def run_lcs_interface(language: str):
    app = LongestCommonSubsequenceApp(language)
    app.mainloop()
