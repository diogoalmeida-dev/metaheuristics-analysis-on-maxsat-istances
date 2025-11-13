import numpy as np
from utils import evaluate_particle_fitness

# parameters
max_velocity = 2

class Particle:
    def __init__(self, num_vars):
        self.num_vars = num_vars ## number of max sat variables
        self.position = np.random.rand(num_vars) ## numpy array of values between 0 and 1
        self.velocity = np.random.uniform(-max_velocity, max_velocity, num_vars)
        self.fitness = 0
