# Multi-Technical Problems Analysis

This project aims to develop programs to solve some usual problems, using the specified algorithm design technique. The programs strive to feature an intuitive and user-friendly interface open to multiple languages.

---

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Files and Structure](#files-and-structure)  
4. [Usage](#usage)  
5. [License](#license)  

---

## Project Overview

This project focuses on implementing solutions for a set of algorithmic problems, applied to real-world challenges. Below are the problems addressed:

1. **Assignment Problem**  
   - Solved using trial and error with **Branch and Bound**.

2. **Huffman Coding**  
   - Compressed a text provided by the user using a **Greedy Algorithm**.

3. **Fractional Knapsack Problem**  
   - Solved using a **Greedy Algorithm**.

4. **Boolean Knapsack Problem (0-1 Knapsack Problem)**  
   - Solved using **Dynamic Programming**.

5. **Longest Common Subsequence Problem**  
   - Solved using **Dynamic Programming**.

   ---

## Features

- **Multi-Technical Approach**: Implements multiple algorithm design techniques such as **Greedy Algorithms, Dynamic Programming, and Branch and Bound**.
- **User-Friendly Interface**: Designed for intuitive interaction, supporting **multiple languages**.
- **Real-World Applications**: Addresses optimization, data compression, and resource allocation problems.
- **Modular Codebase**: Well-structured and documented for easy modifications and enhancements.

---

## Files and Structure

```
Multi-TechnicalProblemAnalysis/
algorithms/
│── translations/
│   ├── __init__.py
│   ├── assignment_problem_translation.py
│   ├── boolean_knapsack_problem_translation.py
│   ├── fractional_knapsack_problem_translation.py
│   ├── huffman_coding_translation.py
│   ├── lcs_translation.py
│── translates/
│   ├── __init__.py
│   ├── main_translation.py
│── .gitignore
│── LICENSE
│── README.md
│── main.py
│── assignment_problem.py
│── boolean_knapsack_problem.py
│── fractional_knapsack_problem.py
│── huffman_coding.py
│── lcs.py
```

---

### Utilities

- **File Handling**: Functions to read and write structured input/output files.
- **Performance Analysis**: Benchmarking tools to measure algorithm efficiency.
- **Visualization Tools**: Graphical/text-based output for better understanding.

---

## Usage

### Prerequisites

Ensure you have the following installed:

- **Python 3.x**
- **Pandas Library**
   ```bash
   pip install pandas
   ```
- **MatPlotLib**
  ```bash
   pip install matplotlib
   ```

### Running the Programs

1. **Clone the repository**  
   ```bash
   git clone https://github.com/DanielServejeira/Multi-TechnicalProblemAnalysis.git
   cd Multi-TechnicalProblemAnalysis
   ```

2. **Navigate to the main archive and run the corresponding script**  
   ```bash
   python main.py
   ```

3. **Check the output in the console or generated files**

---

## License

This project is licensed under the **MIT License**. See the [`LICENSE`](LICENSE) file for details.
