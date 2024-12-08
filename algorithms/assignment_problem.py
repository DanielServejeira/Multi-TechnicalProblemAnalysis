from time import time
import tkinter as tk
from tkinter import ttk
import random
from translations.assignment_problem_translation import translate
import numpy as np




class AssignmentProblemApp(tk.Tk):
    language: str

    def __init__(self, language):
        super().__init__()
        self.language = language
        self.title(translate(language, "window_title"))
        self.geometry("600x700")

        title = ttk.Label(
            self,
            text=translate(language, "title"),
            font=("Arial", 16),
            justify="center",
        )
        title.pack(pady=20)

        self.assignments_label = ttk.Label(self, text=translate(language, "assignments"))
        self.assignments_label.pack()
        self.assignments_entry = ttk.Entry(self)
        self.assignments_entry.pack()

        self.people_label = ttk.Label(self, text=translate(language, "people"))
        self.people_label.pack()
        self.people_entry = ttk.Entry(self)
        self.people_entry.pack()
        
        self.assignment_weights_label = ttk.Label(
            self,
            text=translate(language, "assignment_weights"),
            justify="center",
        )
        self.assignment_weights_label.pack()
        self.assignment_weights_entry = ttk.Entry(self)
        self.assignment_weights_entry.pack()

        self.calculate_button = ttk.Button(
            self,
            text=translate(language, "calculate_button"),
            command=self.calculate_assignment_problem,
        )
        self.calculate_button.pack(pady=10)

        self.generate_weights_label = ttk.Label(
            self, 
            text=translate(language, "generate_weights"), 
            justify="center"
        )
        self.generate_weights_label.pack()

        self.from_label = ttk.Label(self, text=translate(language, "from"))
        self.from_label.pack()
        self.from_entry = ttk.Entry(self)
        self.from_entry.pack()

        self.to_label = ttk.Label(self, text=translate(language, "to"))
        self.to_label.pack()
        self.to_entry = ttk.Entry(self)
        self.to_entry.pack()

        self.generate_weights_button = ttk.Button(
            self,
            text=translate(language, "generate_weights_button"),
            command=self.generate_weights,
        )
        self.generate_weights_button.pack(pady=10)

        self.result_label = ttk.Label(self, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.elapsed_time_label = ttk.Label(self, text="", font=("Arial", 12))
        self.elapsed_time_label.pack(pady=10)

        self.error_label = ttk.Label(self, text="", font=("Arial", 12), foreground="red")
        self.error_label.pack(pady=10)

        self.exit_button = ttk.Button(
            self, text=translate(language, "exit_button"), command=self.destroy
        )
        self.exit_button.pack(pady=10)


    def generate_weights(self):
        people = self.people_entry.get()
        assignments = self.assignments_entry.get()
        start = self.from_entry.get()
        end = self.to_entry.get()

        self.assignment_weights_entry.delete(0, tk.END)

        weights = [random.randint(int(start), int(end)) for _ in range(int(people) * int(assignments))]
        weights_str = " ".join(map(str, weights))
        self.assignment_weights_entry.insert(0, weights_str)
        self.weights = weights  # Store the generated weights in an instance variable

    def calculate_assignment_problem(self):
        m = int(self.people_entry.get())
        n = int(self.assignments_entry.get())
        weights_str = self.assignment_weights_entry.get()

        # Convert the weights string back to a 2D list
        weights = list(map(int, weights_str.split()))

        if len(weights) != m * n:
            self.error_label.config(text=f"{translate(self.language, 'wrong_weight_amount')}")
            return

        weights_matrix = [weights[i * n:(i + 1) * n] for i in range(m)]

        start = time()
        result = assignment_problem(weights_matrix)
        end = time()
        elapsed_time = end - start

        self.result_label.config(
            text=f"{translate(self.language, 'best_cost')} {result[0]}\n{translate(self.language, 'best_solution')} {result[1]}"
        )
        self.elapsed_time_label.config(
            text=f"{translate(self.language, 'elapsed_time_label')} {elapsed_time:.8f} {translate(self.language, 'seconds')}"
        )
        self.error_label.config(text="")


def run_assignment_problem_interface(language: str):
    app = AssignmentProblemApp(language)
    app.mainloop()

print(
    """
    [0] - PT-BR
    [1] - EN-US
      """
)
opt = str(input("Selecione seu idioma de preferência: "))
lang = {"0": "pt-br", "1": "en-us"}
run_assignment_problem_interface(lang[opt])
