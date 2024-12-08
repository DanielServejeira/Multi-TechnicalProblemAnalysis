from time import time
import tkinter as tk
from tkinter import ttk
import random
from algorithms.translations.fractional_knapsack_problem_translation import translate


def greedy_fractional_knapsack(values, weights, W):
    n = len(values)

    # Calculate value/weight ratio for each item
    ratios = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]

    # Sort items based on ratio in non-increasing order
    ratios.sort(reverse=True)

    total_value = 0  # Initialize total value
    current_weight = 0  # Initialize current weight

    # Loop through all items
    for ratio, value, weight in ratios:
        if current_weight + weight <= W:
            # Add entire item
            total_value += value
            current_weight += weight
        else:
            # Add fraction of item
            fraction = (W - current_weight) / weight
            total_value += value * fraction
            break

    return total_value


def recursive_fractional_knapsack(values, weights, W, n):
    if n == 0 or W == 0:
        return 0

    if weights[n - 1] > W:
        return recursive_fractional_knapsack(values, weights, W, n - 1)
    else:
        return max(
            values[n - 1]
            + recursive_fractional_knapsack(values, weights, W - weights[n - 1], n - 1),
            recursive_fractional_knapsack(values, weights, W, n - 1),
        )


class FractionalKnapsackApp(tk.Tk):
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

        self.max_weight_label = ttk.Label(
            self, text=translate(language, "max_weight_label")
        )
        self.max_weight_label.pack()
        self.max_weight_entry = ttk.Entry(self)
        self.max_weight_entry.pack()

        self.values_label = ttk.Label(
            self, text=translate(language, "item_values_label")
        )
        self.values_label.pack()
        self.values_entry = ttk.Entry(self)
        self.values_entry.pack()

        self.weights_label = ttk.Label(
            self, text=translate(language, "item_weights_label")
        )
        self.weights_label.pack()
        self.weights_entry = ttk.Entry(self)
        self.weights_entry.pack()

        self.calculate_button = ttk.Button(
            self,
            text=translate(language, "calculate_button"),
            command=self.calculate_knapsack,
        )
        self.calculate_button.pack(pady=10)

        self.mock_calculate_button = ttk.Button(
            self,
            text=translate(language, "mock_calculate_button"),
            command=self.mock_calculate_knapsack,
        )
        self.mock_calculate_button.pack(pady=10)

        self.greedy_result_label = ttk.Label(self, text="", font=("Arial", 12))
        self.greedy_result_label.pack(pady=10)

        self.greedy_elapsed_time_label = ttk.Label(self, text="", font=("Arial", 12))
        self.greedy_elapsed_time_label.pack(pady=10)

        self.recursive_result_label = ttk.Label(self, text="", font=("Arial", 12))
        self.recursive_result_label.pack(pady=10)

        self.recursive_elapsed_time_label = ttk.Label(self, text="", font=("Arial", 12))
        self.recursive_elapsed_time_label.pack(pady=10)

        self.exit_button = ttk.Button(
            self, text=translate(language, "exit_button"), command=self.destroy
        )
        self.exit_button.pack(pady=10)

    def mock_calculate_knapsack(self):
        self.max_weight_entry.delete(0, tk.END)
        self.values_entry.delete(0, tk.END)
        self.weights_entry.delete(0, tk.END)

        values = [random.randint(1, 100) for _ in range(25)]
        weights = [random.randint(1, 20) for _ in range(25)]

        self.max_weight_entry.insert(0, "500")
        self.values_entry.insert(0, " ".join(map(str, values)))
        self.weights_entry.insert(0, " ".join(map(str, weights)))
        self.calculate_knapsack()

    def calculate_knapsack(self):
        max_weight = int(self.max_weight_entry.get())
        values = list(map(int, self.values_entry.get().split()))
        weights = list(map(int, self.weights_entry.get().split()))

        start = time()
        greedy_result = greedy_fractional_knapsack(values, weights, max_weight)
        end = time()
        greedy_elapsed_time = end - start

        start = time()
        recursive_result = recursive_fractional_knapsack(
            values, weights, max_weight, len(values)
        )
        end = time()
        recursive_elapsed_time = end - start

        self.greedy_result_label.config(
            text=f"{translate(self.language, 'greedy_result_label')}: {greedy_result}"
        )
        self.greedy_elapsed_time_label.config(
            text=f"{translate(self.language, 'greedy_elapsed_time_label')}: {greedy_elapsed_time:.8f} {translate(self.language, 'seconds')}"
        )
        self.recursive_result_label.config(
            text=f"{translate(self.language, 'recursive_result_label')}: {recursive_result}"
        )
        self.recursive_elapsed_time_label.config(
            text=f"{translate(self.language, 'recursive_elapsed_time_label')}: {recursive_elapsed_time:.8f} {translate(self.language, 'seconds')}"
        )


def run_fractional_knapsack_interface(language: str):
    app = FractionalKnapsackApp(language)
    app.mainloop()