from time import time
import tkinter as tk
from tkinter import ttk
import random
from translations.boolean_knapsack_problem_translation import translate


def dynamic_boolean_knapsack(weights, profit, max_weight, n, t):
    # base conditions
    if n == 0 or max_weight == 0:
        return 0
    if t[n][max_weight] != -1:
        return t[n][max_weight]

    # choice diagram code
    if weights[n - 1] <= max_weight:
        t[n][max_weight] = max(
            profit[n - 1]
            + dynamic_boolean_knapsack(
                weights, profit, max_weight - weights[n - 1], n - 1, t
            ),
            dynamic_boolean_knapsack(weights, profit, max_weight, n - 1, t),
        )
        return t[n][max_weight]
    elif weights[n - 1] > max_weight:
        t[n][max_weight] = dynamic_boolean_knapsack(
            weights, profit, max_weight, n - 1, t
        )
        return t[n][max_weight]


def recursive_boolean_knapsack(max_weight, weights, profit, n):
    # Base Case
    if n == 0 or max_weight == 0:
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity max_weight,
    # then this item cannot be included
    # in the optimal solution
    if weights[n - 1] > max_weight:
        return recursive_boolean_knapsack(max_weight, weights, profit, n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            profit[n - 1]
            + recursive_boolean_knapsack(
                max_weight - weights[n - 1], weights, profit, n - 1
            ),
            recursive_boolean_knapsack(max_weight, weights, profit, n - 1),
        )


class BooleanKnapsackApp(tk.Tk):
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

        self.max_weight_label = ttk.Label(self, text=translate(language, "max_weight_label"))
        self.max_weight_label.pack()
        self.max_weight_entry = ttk.Entry(self)
        self.max_weight_entry.pack()

        self.profit_label = ttk.Label(
            self, text=translate(language, "item_values_label")
        )
        self.profit_label.pack()
        self.profit_entry = ttk.Entry(self)
        self.profit_entry.pack()

        self.weights_label = ttk.Label(
            self, text=translate(language, "item_weights_label")
        )
        self.weights_label.pack()
        self.weights_entry = ttk.Entry(self)
        self.weights_entry.pack()

        self.calculate_button = ttk.Button(
            self, text=translate(language, "calculate_button"), command=self.calculate_knapsack
        )
        self.calculate_button.pack(pady=10)

        self.mock_calculate_button = ttk.Button(
            self,
            text=translate(language, "mock_calculate_button"),
            command=self.mock_calculate_knapsack,
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

        self.exit_button = ttk.Button(self, text=translate(language, "exit_button"), command=self.quit)
        self.exit_button.pack(pady=10)

    def mock_calculate_knapsack(self):
        self.max_weight_entry.delete(0, tk.END)
        self.profit_entry.delete(0, tk.END)
        self.weights_entry.delete(0, tk.END)

        profit = [random.randint(1, 100) for _ in range(25)]
        weights = [random.randint(1, 20) for _ in range(25)]

        self.max_weight_entry.insert(0, "500")
        self.profit_entry.insert(0, " ".join(map(str, profit)))
        self.weights_entry.insert(0, " ".join(map(str, weights)))
        self.calculate_knapsack()

    def calculate_knapsack(self):
        max_weight = int(self.max_weight_entry.get())
        profit = list(map(int, self.profit_entry.get().split()))
        weights = list(map(int, self.weights_entry.get().split()))

        start = time()
        t = [[-1 for i in range(max_weight + 1)] for j in range(len(profit) + 1)]
        dynamic_result = dynamic_boolean_knapsack(
            weights, profit, max_weight, len(profit), t
        )
        end = time()
        dynamic_elapsed_time = end - start

        start = time()
        recursive_result = recursive_boolean_knapsack(
            max_weight, weights, profit, len(profit)
        )
        end = time()
        recursive_elapsed_time = end - start

        self.dynamic_result_label.config(
            text=f"{translate(self.language, 'dynamic_result_label')}: {dynamic_result}"
        )
        self.dynamic_elapsed_time_label.config(
            text=f"{translate(self.language, 'dynamic_elapsed_time_label')}: {dynamic_elapsed_time:.8f} {translate(self.language, 'seconds')}"
        )
        self.recursive_result_label.config(
            text=f"{translate(self.language, 'recursive_result_label')}: {recursive_result}"
        )
        self.recursive_elapsed_time_label.config(
            text=f"{translate(self.language, 'recursive_elapsed_time_label')}: {recursive_elapsed_time:.8f} {translate(self.language, 'seconds')}"
        )


def run_boolean_knapsack_interface(language):
    app = BooleanKnapsackApp(language)
    app.mainloop()

print("""
    [0] - PT-BR
    [1] - EN-US
      """)
opt = str(input("Selecione seu idioma de preferência: "))
lang = {
    "0":'pt-br',
    "1":'en-us'
}
run_boolean_knapsack_interface(lang[opt])
