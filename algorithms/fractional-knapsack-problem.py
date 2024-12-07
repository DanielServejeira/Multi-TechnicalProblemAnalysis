from time import time
import tkinter as tk
from tkinter import ttk
import random

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
            values[n - 1] + recursive_fractional_knapsack(values, weights, W - weights[n - 1], n - 1),
            recursive_fractional_knapsack(values, weights, W, n - 1)
        )

class KnapsackApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Problema da Mochila Fracionária")
        self.geometry("600x550")

        title = ttk.Label(self, text="Problema da Mochila Fracionária\n(comparativo com algoritmo guloso x recursivo)", font=("Arial", 16), justify="center")
        title.pack(pady=20)

        self.max_weight_label = ttk.Label(self, text="Peso máximo da mochila:")
        self.max_weight_label.pack()
        self.max_weight_entry = ttk.Entry(self)
        self.max_weight_entry.pack()

        self.values_label = ttk.Label(self, text="Valores dos itens (separados por espaço):")
        self.values_label.pack()
        self.values_entry = ttk.Entry(self)
        self.values_entry.pack()

        self.weights_label = ttk.Label(self, text="Pesos dos itens (separados por espaço):")
        self.weights_label.pack()
        self.weights_entry = ttk.Entry(self)
        self.weights_entry.pack()

        self.calculate_button = ttk.Button(self, text="Calcular", command=self.calculate_knapsack)
        self.calculate_button.pack(pady=10)
        
        self.mock_calculate_button = ttk.Button(self, text="Calcular (valores aleatórios)", command=self.mock_calculate_knapsack)
        self.mock_calculate_button.pack(pady=10)

        self.greedy_result_label = ttk.Label(self, text="", font=("Arial", 12))
        self.greedy_result_label.pack(pady=10)
        
        self.greedy_elapsed_time_label = ttk.Label(self, text="", font=("Arial", 12))
        self.greedy_elapsed_time_label.pack(pady=10)
        
        self.recursive_result_label = ttk.Label(self, text="", font=("Arial", 12))
        self.recursive_result_label.pack(pady=10)
        
        self.recursive_elapsed_time_label = ttk.Label(self, text="", font=("Arial", 12))
        self.recursive_elapsed_time_label.pack(pady=10)
        
        self.exit_button = ttk.Button(self, text="Sair", command=self.quit)
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
        print(f"greedy_start: {start}")
        print(f"greedy_end: {end}")
        print(f"greedy_elapsed_time: {greedy_elapsed_time}")
        
        start = time()
        recursive_result = recursive_fractional_knapsack(values, weights, max_weight, len(values))
        end = time()
        recursive_elapsed_time = end - start
        print(f"recursive_start: {start}")
        print(f"recursive_end: {end}")
        print(f"recursive_elapsed_time: {recursive_elapsed_time}")
        
        self.greedy_result_label.config(text=f"Valor máximo na mochila: {greedy_result}")
        self.greedy_elapsed_time_label.config(text=f"Tempo decorrido (guloso): {greedy_elapsed_time:.8f} segundos")
        self.recursive_result_label.config(text=f"Valor máximo na mochila: {recursive_result}")
        self.recursive_elapsed_time_label.config(text=f"Tempo decorrido (recursivo): {recursive_elapsed_time:.8f} segundos")

def run_knapsack_interface():
    app = KnapsackApp()
    app.mainloop()
    
run_knapsack_interface()