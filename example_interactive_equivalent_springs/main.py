from gui.input_listeners.game_like_input_listener import GameLikeInputListener
from gui.main_window import MainWindow
from gui.paintables.paintable_connector import PaintableConnector
from gui.paintables.paintable_particle import PaintableParticle
from physics.force_generator.spring_force_generator import SpringForceGenerator
from physics.particle import Particle
from physics.physics_simulator import PhysicsSimulator
import numpy as np

# As in reality, infinite equals one million :)
INFINITE = 1000000.0

if __name__ == '__main__':
    main_window = MainWindow("Equivalent Springs Example", 400, 400)
    main_window.setInputListener(GameLikeInputListener(main_window))

    simulator = PhysicsSimulator()

    #===========================================================================
    
    k0 = 3.5
    k1 = 0.5
    
    particle1 = Particle(mass=1.0)
    particle2 = Particle(mass=INFINITE)
    simulator.addBody(particle1)
    simulator.addBody(particle2)
    particle1_painter = PaintableParticle()
    particle2_painter = PaintableParticle()
    particle1_painter.setParticle(particle1)
    particle2_painter.setParticle(particle2)
    connector1_2_painter = PaintableConnector(particle1, particle2)
    main_window.addObject(particle1_painter)
    main_window.addObject(particle2_painter)
    main_window.addObject(connector1_2_painter)
    particle1.position = np.array([-1.0, 0.0, 5.0])
    particle2.position = np.array([-1.0, -1.0, 5.0])
    simulator.addForceGenerator(SpringForceGenerator(particle1, particle2, 0.6, k0))
    simulator.addForceGenerator(SpringForceGenerator(particle1, particle2, 0.6, k1))
    
    equivalent_k = k0 + k1

    particle1 = Particle(mass=1.0)
    particle2 = Particle(mass=INFINITE)
    simulator.addBody(particle1)
    simulator.addBody(particle2)
    particle1_painter = PaintableParticle()
    particle2_painter = PaintableParticle()
    particle1_painter.setParticle(particle1)
    particle2_painter.setParticle(particle2)
    connector1_2_painter = PaintableConnector(particle1, particle2)
    main_window.addObject(particle1_painter)
    main_window.addObject(particle2_painter)
    main_window.addObject(connector1_2_painter)
    particle1.position = np.array([-0.5, 0.0, 5.0])
    particle2.position = np.array([-0.5, -1.0, 5.0])
    simulator.addForceGenerator(SpringForceGenerator(particle1, particle2, 0.6, equivalent_k))

    #===========================================================================
    
    k0 = 1.0
    k1 = 5.0

    particle1 = Particle(mass=1.0)
    particle2 = Particle(mass=0.01)
    particle3 = Particle(mass=INFINITE)
    simulator.addBody(particle1)
    simulator.addBody(particle2)
    simulator.addBody(particle3)
    particle1_painter = PaintableParticle()
    particle2_painter = PaintableParticle()
    particle3_painter = PaintableParticle()
    particle1_painter.setParticle(particle1)
    particle2_painter.setParticle(particle2)
    particle3_painter.setParticle(particle3)
    connector1_2_painter = PaintableConnector(particle1, particle2)
    connector2_3_painter = PaintableConnector(particle2, particle3)
    main_window.addObject(particle1_painter)
    main_window.addObject(particle2_painter)
    main_window.addObject(particle3_painter)
    main_window.addObject(connector1_2_painter)
    main_window.addObject(connector2_3_painter)
    particle1.position = np.array([0.5, 0.0, 5.0])
    particle2.position = np.array([0.5, -0.5, 5.0])
    particle3.position = np.array([0.5, -1.0, 5.0])
    simulator.addForceGenerator(SpringForceGenerator(particle1, particle2, 0.4, k0))
    simulator.addForceGenerator(SpringForceGenerator(particle2, particle3, 0.4, k1))

    equivalent_k = 1.0 / (1.0 / k0 + 1.0 / k1)
    
    # Add particles to simulator
    particle1 = Particle(mass=1.0)
    particle2 = Particle(mass=INFINITE)
    simulator.addBody(particle1)
    simulator.addBody(particle2)

    # Add particle to scene
    particle1_painter = PaintableParticle()
    particle2_painter = PaintableParticle()
    particle1_painter.setParticle(particle1)
    particle2_painter.setParticle(particle2)
    connector1_2_painter = PaintableConnector(particle1, particle2)
    main_window.addObject(particle1_painter)
    main_window.addObject(particle2_painter)
    main_window.addObject(connector1_2_painter)

    particle1.position = np.array([1.0, 0.0, 5.0])
    particle2.position = np.array([1.0, -1.0, 5.0])

    # Finally, add forces
    simulator.addForceGenerator(SpringForceGenerator(particle1, particle2, 0.8, equivalent_k))
 
    #===========================================================================

    main_window.addBeforeDrawSceneCallback(simulator.update)
    main_window.mainLoop()
