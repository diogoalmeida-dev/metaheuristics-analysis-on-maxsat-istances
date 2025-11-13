"""
Particle Swarm Optimisation is a population based metaheuristic
- The state of the system at any given time is defined by the positions and velocities of all particles

How it works:
- starts with a population of particles with rand positions and velocities
- positions are the float random values assigned to each value, velocities is how much they change
- each particle is evaluated at their current position (fitness)
- we store a global best position "global_best_fitness" and for a particle best "particle.best_fitness"
- if a certain pbest is greater than gbest, we update gbest
- the velocity of each particle is calculated based on pbest, gbest, current velocity and rand values

step 1: initialise particles with random x (position) and v (velocity)
step 2: evaluate fitness
step 3: for each particle, update velocity
step 4: for each particle, update position
step 5: for each particle, update the best personal fitness and the best global fitness
step 6: for each particle, if the current fitness is a global optimum (satisfies all clauses) early exit
step 7: return to step 3
"""

from particle import *
from src.utils import evaluate_particle_fitness

def particle_swarm_optimisation(clauses, num_clauses, num_vars, num_particles, iterations):
    swarm = [initialise_particle(clauses,num_vars) for _ in range(num_particles)] ## arr of particles, size = number of particles (arg), step 1 and 2

    global_best_fitness = max(p.fitness for p in swarm)
    best_index = np.argmax([p.fitness for p in swarm])
    global_best_position = swarm[best_index].position.copy()

    for _ in range(iterations):
        for particle in swarm:
            particle.update_velocity(global_best_position) ## step 3
            particle.update_position()                     ## step 4

            particle.fitness = evaluate_particle_fitness(clauses, particle.position)

            if particle.fitness > global_best_fitness:
                global_best_fitness = particle.fitness   ## update global best fitness
            if particle.fitness > particle.best_fitness:
                particle.best_fitness = particle.fitness ## update particle best fitness

            if global_best_fitness == num_clauses or particle.best_fitness == num_clauses: ## early exit if global optimum found
                return global_best_fitness

    print(global_best_fitness)

def initialise_particle(clauses, num_vars):
    p = Particle(num_vars)
    p.fitness = evaluate_particle_fitness(clauses, p.position)
    p.update_best_state()
    return p