"""
Particle Swarm Optimisation is a population based metaheuristic
- The state of the system at any given time is defined by the positions and velocities of all particles

How it works:
- starts with a population of particles with rand positions and velocities
- positions are the float random values assigned to each value, velocities is how much they change
- each particle is evaluated at their current position (fitness)
- we store a global best "gbest" and for a particle best "pbest"
- if a certain pbest is greater than gbest, we update gbest
- the velocity of each particle is calculated based on pbest, gbest, current velocity and rand values

step 1: initialise particles with random x (position) and v (velocity)
step 2: evaluate fitness
step 3:
"""

from particle import *

def particle_swarm_optimisation(clauses, num_clauses, num_vars, num_particles):
    global_best = -999

    swarm = [Particle(num_vars) for _ in range(num_particles)] ## arr of particles, size = number of particles (arg)

    for particle in swarm:
        particle.fitness = evaluate_particle_fitness(clauses, particle.position)
        if particle.fitness > global_best: global_best = particle.fitness


    print(global_best)