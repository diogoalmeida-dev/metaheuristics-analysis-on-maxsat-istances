#utils.py

import random

# Default CNF file path (can be overridden)
CNF_FILE_PATH = "../cnf_files/uf20-01.cnf"

# functions that reads the cnf file and stores variables and lists of its content
def read_cnf(filepath=None):
    if filepath is None:
        filepath = CNF_FILE_PATH
    clauses = []
    num_clauses = 0
    num_vars = 0

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("c"):
                continue

            if line.startswith("p"): # process header line (starts with p)
                parts = line.split()
                num_vars = int(parts[2])
                num_clauses = int(parts[3])
                continue

            clause = []             # clause lines, finish with 0
            for x in line.split():
                if x == '0': ## if 0, go next line
                    continue
                try:
                    clause.append(int(x)) ## if not append the integer
                except ValueError: ## if any char besides integers, skip line (bcs of % 0 in end of file .cnf)
                    continue

            if clause:
                clauses.append(clause)

            if len(clauses) >= num_clauses: ## stop after all clauses are read
                break

    return clauses, num_clauses, num_vars


# Function to find the fitness being the fitness the number of clauses satisfied by the combination
def evaluate_particle_fitness(clauses, combination):
    fitness = 0

    for clause in clauses:

        clause_fitness = 0
        for value in clause:
            var_index = abs(value) - 1 ## normalise for clause list
            ## replace with: "combination[var_index]" if you want to use the continuous vector, this line just turns 0.3 in 0 and 0.7 in 1
            bool_value = 1 if combination[var_index] > 0.5 else 0
            if value < 0: ## if literal value is below 0, the variable is negated
                bool_value = not bool_value
            if bool_value: ## if bool is true
                clause_fitness = 1
                break
        fitness += clause_fitness
    return fitness