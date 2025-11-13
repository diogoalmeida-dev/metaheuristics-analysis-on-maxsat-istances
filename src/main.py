from src import utils
from particle_swarm_optimisation import *

CNF_FILES = {
    "1": "../cnf_files/uf20-01.cnf",
    "2": "../cnf_files/uf100-01.cnf",
    "3": "../cnf_files/uf250-01.cnf"
}

num_particles = 500
num_informants = 3
iterations = 5000

def main():
    print("Select CNF file:")
    print("1 - uf20-01.cnf")
    print("2 - uf100-01.cnf")
    print("3 - uf250-01.cnf")
    cnf_choice = input("Enter choice (1-3): ").strip()

    if cnf_choice not in CNF_FILES:
        print("Invalid CNF file choice.")
        return

    cnf_path = CNF_FILES[cnf_choice]
    clauses, num_clauses, num_vars = utils.read_cnf(cnf_path)
    print(f"\nLoaded: {cnf_path} — vars={num_vars}, clauses={num_clauses}")

    print("\nSelect algorithm:")
    print("1 - PSO")
    print("2 - PSO with informants")
    x = int(input("Enter choice: (1-2): "))
    if x == 1:
        particle_swarm_optimisation(clauses, num_clauses, num_vars,num_particles, iterations)
    else:
        particle_swarm_optimisation_with_informants(clauses, num_clauses, num_vars, num_particles, num_informants, iterations)

if __name__ == "__main__":
    main()
