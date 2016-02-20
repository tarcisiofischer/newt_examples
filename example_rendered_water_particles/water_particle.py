import random

from physics.particle import Particle
import numpy as np


#===============================================================================
# WaterParticle
#===============================================================================
class WaterParticle(Particle):

    def __init__(self):
        Particle.__init__(self, mass=0.001)
        self.geometry.setColor(np.array([0.1, 0.1, 0.6]))
        self.reset()


    def reset(self):
        self._lifetime = random.random() * 2.0
        self.velocity = np.array([
            2.0 * random.random() - 1.0,
            1.0 * random.random() + 7.0,
            2.0 * random.random() - 1.0
        ])
        self.setPosition(np.array([-0.5, -2.0, 0.0]))


    def update(self, delta_t):
        self._lifetime -= delta_t
        if self._lifetime < 0.0:
            self.reset()
        Particle.update(self, delta_t)
