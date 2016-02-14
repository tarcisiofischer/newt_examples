from gui.input_listeners.game_like_input_listener import GameLikeInputListener
from gui.main_window import MainWindow
from gui.paintables.paintable_connector import PaintableConnector
from gui.paintables.paintable_particle import PaintableParticle
from physics.force_generator.spring_force_generator import SpringForceGenerator
from physics.particle import Particle
from physics.physics_simulator import PhysicsSimulator
import numpy as np


if __name__ == '__main__':
    main_window = MainWindow("Spring Example", 400, 400)
    main_window.setInputListener(GameLikeInputListener(main_window))

    simulator = PhysicsSimulator()
    # Add particles to simulator
    particle1 = Particle(mass=0.1)
    particle2 = Particle(mass=1.0)
    particle3 = Particle(mass=0.2)
    simulator.addBody(particle1)
    simulator.addBody(particle2)
    simulator.addBody(particle3)

    # Add particle to scene
    particle1_painter = PaintableParticle()
    particle2_painter = PaintableParticle()
    particle3_painter = PaintableParticle()
    particle1_painter.setParticle(particle1)
    particle2_painter.setParticle(particle2)
    particle3_painter.setParticle(particle3)
    connector12_painter = PaintableConnector(particle1, particle2)
    connector23_painter = PaintableConnector(particle2, particle3)
    connector13_painter = PaintableConnector(particle1, particle3)
    main_window.addObject(particle1_painter)
    main_window.addObject(particle2_painter)
    main_window.addObject(particle3_painter)
    main_window.addObject(connector12_painter)
    main_window.addObject(connector23_painter)
    main_window.addObject(connector13_painter)

    # Re-position particles for simulation
    # Particle1 is the fix particle (Will not have gravity)
    particle1.position = np.array([1.0, 0.0, 7.0])
    # Particle2 is the moving particle (Will have the gravity force changing it)
    particle2.position = np.array([0.0, 0.0, 7.0])
    particle3.position = np.array([0.0, -1.0, 7.0])

    # Finally, add forces
    simulator.addForceGenerator(SpringForceGenerator(particle1, particle2, 1.2, 4.0))
    simulator.addForceGenerator(SpringForceGenerator(particle2, particle3, 1.2, 4.0))
    simulator.addForceGenerator(SpringForceGenerator(particle1, particle3, 1.2, 4.0))

    main_window.addBeforeDrawSceneCallback(simulator.update)
    main_window.mainLoop()
