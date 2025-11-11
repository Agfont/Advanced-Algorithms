# Advanced-Algorithms
Couse of Advanced-Algorithms - UB

## Repository overview

This repository contains course materials for an Advanced Algorithms. Practical implementations are organized into two main folders: Exercises and Laboratory. 

- [Exercises](Exercises/)
	- [0-Complejidad](Exercises/0-Complejidad/)
	- [1-Grafos_A](Exercises/1-Grafos_A/)

	- [1-Grafos_B](Exercises/1-Grafos_B/)
	- [1-Grafos_C](Exercises/1-Grafos_C/)
	- [2-Greedy](Exercises/2-Greedy/)

	- [3-PD_A](Exercises/3-PD_A/)
	- [3-PD_B](Exercises/3-PD_B/)
	- [4-Enum](Exercises/4-Enum/)


- [Laboratory](Laboratory/)
	- [Lab0](Laboratory/Lab0/)
	- [Lab1](Laboratory/Lab1/)

	- [Lab2](Laboratory/Lab2/)
	- [Lab3](Laboratory/Lab3/)
	- [Lab4](Laboratory/Lab4/)

	- [Parcial](Laboratory/Parcial/)

## Notes about the notebooks

- Most notebooks are self-contained Jupyter notebooks (.ipynb) and are intended for sequential execution (run cells top-to-bottom).
- Several notebooks reference helper Python files (for example `utils.py`) in the same folder — keep those files alongside the corresponding notebook when running.

## How to run the notebooks (quick)

1. Install typical data-science and graph libraries used by the notebooks (add more if specific imports are required):

```bash
pip install --upgrade pip
pip install jupyterlab numpy pandas matplotlib networkx
```

2. Start JupyterLab or Jupyter Notebook and open the notebook you want:

```bash
jupyter-notebook
```

### Exercises

- `0-Complejidad/` — Notes and examples about algorithmic complexity (Big-O, empirical timings). Contains explanatory markdown and small Python demos used as micro-benchmarks.

- `1-Grafos_A/` — Introductory graph algorithms: graph representations, traversal (BFS/DFS), connectivity, simple examples and visualizations. This folder includes helper code (`utils.py`) and image assets used in the notebooks.

- `1-Grafos_B/` — Continued graph exercises and more practice problems (variants and extended examples). Contains notebooks that reuse graph helpers and include additional problem statements and sample runs.

- `1-Grafos_C/` — Further graph problem sets and solutions; often focused on specific graph tasks or proof-of-concept implementations.

- `2-Greedy/` — Greedy algorithm exercises. Typical content: greedy-choice explanations, examples (coin change, scheduling, MST heuristics) and Python implementations of greedy heuristics.

- `3-PD_A/` — Dynamic programming (Programación Dinámica) fundamentals and classic problems (knapsack, edit distance, sequence problems). Long code cells implement DP recurrences and examples.

- `3-PD_B/` — Additional DP exercises and variations, providing more practice problems and alternative implementations.

- `4-Enum/` — Enumeration and backtracking problems (exhaustive search, branch-and-bound, constraint solving). Notebooks include backtracking templates and problem-specific pruning strategies.

### Laboratory

- `Lab0/` — Introductory lab covering Python classes, data structures and basic utilities used across later labs. Contains thorough examples and class-based implementations.

- `Lab1/` — Practical lab on graphs. Includes dataset CSVs in `Lab1/csv/` (for network examples), longer code cells with BFS/DFS/Dijkstra and sometimes flow algorithms. Good for applied graph tasks and visualizations.

- `Lab2/` — Greedy lab: applied greedy problems, plotting and example datasets. Notebooks show step-by-step greedy decisions and result comparisons.

- `Lab3/` — Dynamic programming lab. Contains instructor-provided notebooks and student variants; exercises implement DP solutions and may include richer outputs (plots, interactive widgets).

- `Lab4/` — Enumeration/backtracking lab. Includes problem statements and solution notebooks; there is a `Sol4Enum/` folder with worked solutions and example runs.

- `Parcial/` — Partial/exam notebooks and project-style exercises. These are sized like assessments: problem descriptions, input parsing and consolidated solver implementations (often with plots/images embedded).