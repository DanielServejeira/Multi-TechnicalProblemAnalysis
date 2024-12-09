from time import time
import tkinter as tk
from tkinter import ttk
import random
from algorithms.translations.assignment_problem_translation import translate


def calculate_cost(matrix, assignment):
    #Calculate the total cost of a given assignment.
    return sum(matrix[i][assignment[i]] for i in range(len(assignment)))

def branch_and_bound(matrix, assignment, level, best_solution, best_cost):
    n = len(matrix)
    if level == n:
        current_cost = calculate_cost(matrix, assignment)
        if current_cost < best_cost:
            best_cost = current_cost
            best_solution = assignment[:]
        return best_solution, best_cost

    for j in range(n):
        if j not in assignment:
            assignment[level] = j
            best_solution, best_cost = branch_and_bound(matrix, assignment, level + 1, best_solution, best_cost)
            assignment[level] = -1
    return best_solution, best_cost

def assignment_problem(matrix):
    n = len(matrix)
    assignment = [-1] * n
    best_solution = None
    best_cost = float('inf')
    return branch_and_bound(matrix, assignment, 0, best_solution, best_cost)


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
        # Generate random weights for the matrix.
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

        weights = list(map(int, weights_str.split()))
        if len(weights) != m * n:
            self.error_label.config(text=f"{translate(self.language, 'wrong_weight_amount')}")
            return

        weights_matrix = [weights[i * n:(i + 1) * n] for i in range(m)]

        start = time()
        best_cost, best_solution = assignment_problem(weights_matrix)
        end = time()
        elapsed_time = end - start

        self.result_label.config(
            text=f"{translate(self.language, 'best_cost')} {best_cost}\n"
                 f"{translate(self.language, 'best_solution')} {best_solution}"
        )
        self.elapsed_time_label.config(
            text=f"{translate(self.language, 'elapsed_time_label')}: {elapsed_time:.8f} {translate(self.language, 'seconds')}"
        )
        self.error_label.config(text="")


def run_assignment_problem_interface(language: str):
    app = AssignmentProblemApp(language)
    app.mainloop()