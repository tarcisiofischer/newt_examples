from example_interactive_water_particles.water_particle import WaterParticle
from gui.input_listeners.game_like_input_listener import GameLikeInputListener
from gui.main_window import MainWindow
from gui.paintables.paintable_polyhedron import PaintablePolyhedron
from physics.force_generator.gravity_force_generator import GravityForceGenerator
from physics.physics_simulator import PhysicsSimulator


# Controls the number of simulated particles.
N_PARTICLES = 500


if __name__ == '__main__':
    main_window = MainWindow("Water Particles Example", 400, 400)
    main_window.setInputListener(GameLikeInputListener(main_window))

    simulator = PhysicsSimulator()
    for i in xrange(N_PARTICLES):
        # Add particle to simulator
        particle = WaterParticle()
        simulator.addForceGenerator(GravityForceGenerator(particle))
        simulator.addBody(particle)
        # Add particle to scene
        particle_painter = PaintablePolyhedron(particle.geometry)
        main_window.addObject(particle_painter)

    main_window.addBeforeDrawSceneCallback(simulator.update)
    main_window.mainLoop()
