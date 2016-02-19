import numpy as np
from physics.particle_array import ParticleArray


#===============================================================================
# WaterParticleArray
#===============================================================================
class WaterParticleArray(ParticleArray):

    def __init__(self, number_of_particles):
        ParticleArray.__init__(self, mass=0.001, number_of_particles=number_of_particles)
        self.reset()


    def reset(self):
        self._lifetime = np.random.rand(self.number_of_particles) * 2.0
        self.velocity = np.random.rand(self.number_of_particles * 3).reshape(self.number_of_particles, 3)
        self.velocity[:,0] = 2.0 * self.velocity[:,0] - 1.0
        self.velocity[:,1] = 1.0 * self.velocity[:,1] + 7.0
        self.velocity[:,2] = 2.0 * self.velocity[:,2] - 1.0
        self.position = np.tile([-0.5, -2.0, 0.0], self.number_of_particles).reshape(self.number_of_particles, 3)


    def update(self, delta_t):
        self._lifetime -= delta_t

        positions = self._lifetime < 0.0
        number_of_deaths = np.sum(positions)

        self._lifetime[positions] = np.random.rand(number_of_deaths) * 2.0
        self.velocity[positions] = np.random.rand(number_of_deaths * 3).reshape(number_of_deaths, 3)
        self.velocity[positions,0] = 2.0 * self.velocity[positions,0] - 1.0
        self.velocity[positions,1] = 1.0 * self.velocity[positions,1] + 7.0
        self.velocity[positions,2] = 2.0 * self.velocity[positions,2] - 1.0
        self.position[positions] = np.tile([-0.5, -2.0, 0.0], number_of_deaths).reshape(number_of_deaths, 3)
        
        ParticleArray.update(self, delta_t)
