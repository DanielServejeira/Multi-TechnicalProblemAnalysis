from time import time
import tkinter as tk
from tkinter import ttk
import random


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
    def __init__(self):
        super().__init__()
        self.title("Problema da Mochila Booleana")
        self.geometry("600x550")

        title = ttk.Label(
            self,
            text="Problema da Mochila Booleana\n(comparativo com programação dinâmica x recursivo)",
            font=("Arial", 16),
            justify="center",
        )
        title.pack(pady=20)

        self.max_weight_label = ttk.Label(self, text="Peso máximo da mochila:")
        self.max_weight_label.pack()
        self.max_weight_entry = ttk.Entry(self)
        self.max_weight_entry.pack()

        self.profit_label = ttk.Label(
            self, text="Valores dos itens (separados por espaço):"
        )
        self.profit_label.pack()
        self.profit_entry = ttk.Entry(self)
        self.profit_entry.pack()

        self.weights_label = ttk.Label(
            self, text="Pesos dos itens (separados por espaço):"
        )
        self.weights_label.pack()
        self.weights_entry = ttk.Entry(self)
        self.weights_entry.pack()

        self.calculate_button = ttk.Button(
            self, text="Calcular", command=self.calculate_knapsack
        )
        self.calculate_button.pack(pady=10)

        self.mock_calculate_button = ttk.Button(
            self,
            text="Calcular (valores aleatórios)",
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

        self.exit_button = ttk.Button(self, text="Sair", command=self.quit)
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
            text=f"Valor máximo na mochila (dinâmico): {dynamic_result}"
        )
        self.dynamic_elapsed_time_label.config(
            text=f"Tempo decorrido (dinâmico): {dynamic_elapsed_time:.8f} segundos"
        )
        self.recursive_result_label.config(
            text=f"Valor máximo na mochila (recursivo): {recursive_result}"
        )
        self.recursive_elapsed_time_label.config(
            text=f"Tempo decorrido (recursivo): {recursive_elapsed_time:.8f} segundos"
        )


def run_boolean_knapsack_interface():
    app = BooleanKnapsackApp()
    app.mainloop()


run_boolean_knapsack_interface()
