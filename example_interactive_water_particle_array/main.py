from gui.input_listeners.game_like_input_listener import GameLikeInputListener
from gui.main_window import MainWindow
from gui.paintables.paintable_particle import PaintableParticle
from physics.force_generator.gravity_force_generator import GravityForceGenerator
from physics.physics_simulator import PhysicsSimulator
from example_interactive_water_particle_array.water_particle_array import WaterParticleArray

# Controls the number of simulated particles.
N_PARTICLES = 2000



if __name__ == '__main__':
    main_window = MainWindow("Water Particles Example", 400, 400)
    main_window.setInputListener(GameLikeInputListener(main_window))

    simulator = PhysicsSimulator()

    # Add particles to simulator
    particle_array = WaterParticleArray(N_PARTICLES)
    simulator.addForceGenerator(GravityForceGenerator(particle_array))
    simulator.addBody(particle_array)

    for i in xrange(N_PARTICLES):
        particle = particle_array.getReadOnlyParticle(i)

        # Add particle to scene
        particle_painter = PaintableParticle()
        particle_painter.setParticle(particle)
        main_window.addObject(particle_painter)

    main_window.addBeforeDrawSceneCallback(simulator.update)
    main_window.mainLoop()
