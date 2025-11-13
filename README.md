# Particle Swarm Optimisation for MAX-SAT

Binary Particle Swarm Optimisation (PSO) applied to MAX-SAT instances in DIMACS CNF format. Each particle is an array of floats [0..1] with size equals to the number of variables presented in the MAX-SAT problem, and the fitness is the number of satisfied clauses.

---

## How the Code Works (Flow)

The typical run in `src/main.py` looks like this:

1. **Load CNF instance**  
   - Reads a DIMACS file from `cnf_files/` (e.g. `../cnf_files/uf20-01.cnf`).  
   - Extracts:
     - `clauses` – list of clauses
     - `num_vars` – number of variables
     - `num_clauses` – number of clauses  
   - Prints a short summary: `Loaded: <file> — vars=X, clauses=Y`.

2. **Run PSO or PSO with informants**  
   - Calls (example):  
     `particle_swarm_optimisation_with_informants(clauses, num_clauses, num_vars, num_particles, num_particles, num_informants, iterations)`  
   - Inside PSO:
     - Creates an initial swarm of random binary assignments.
     - Evaluates fitness of each particle.
     - For each iteration:
       - (Informant version: Finds each particle’s **informants** (subset of the swarm)).
       - (Informant version: Finds the best informant for each particle).
       - Updates velocities and bit flip probabilities.
       - Updates positions (0/1 bits) accordingly.
       - Updates personal bests and global / informants’ best.
   - At the end, reports the best fitness found.

---

## Project Structure

- `src/main.py`  
  Entry point; loads CNF, defines parameters, calls the PSO function.

- `src/particle_swarm_optimisation.py`

Implementation of:
  - `particle_swarm_optimisation`
  - `particle_swarm_optimisation_with_informants`

- `src/particle.py`
  Class that defines a particle, functions to update velocity, update velocity with informants, update position.

- `src/utils.py` (or similar)  
  Function to read and parse DIMACS CNF files into `clauses`, `num_vars`, `num_clauses` and a function to evaluate fitness.

- `cnf_files/`  
  Contains the `.cnf` instances used in the experiments.

- `results/` (in development)  


---

## Requirements

- **Python** ≥ 3.10
- Recommended packages:
  - `numpy` (for arrays and vectorised operations, if used)

Install dependencies:
- `pip install -r requirements.txt`

or manually:
- `pip install numpy pandas matplotlib`

---

## Running the Code

From the repo root:

- `python src/main.py`

By default, `main.py`:

- Chooses a CNF file (e.g. `../cnf_files/uf20-01.cnf`).
- Sets PSO parameters (swarm size, number of informants, iterations).
- Runs PSO and prints the best fitness.

To run a different instance or change settings, edit the values in `main.py`:

- Path to the CNF file.
- The arguments passed to `particle_swarm_optimisation_with_informants(...)`.

---

## Tunable Parameters

The main PSO call generally looks like:

```python
particle_swarm_optimisation_with_informants(
    clauses,
    num_clauses,
    num_vars,
    swarm_size,        # e.g. 100
    num_informants,    # e.g. 4
    max_iterations     # e.g. 200
)
