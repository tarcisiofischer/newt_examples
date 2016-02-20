from example_interactive_water_particle_array.water_particle_array import WaterParticleArray
from gui.input_listeners.game_like_input_listener import GameLikeInputListener
from gui.main_window import MainWindow
from gui.paintables.paintable_polyhedron import PaintablePolyhedron
from physics.force_generator.gravity_force_generator import GravityForceGenerator
from physics.physics_simulator import PhysicsSimulator


# Controls the number of simulated particles.
N_PARTICLES = 1000



if __name__ == '__main__':
    main_window = MainWindow("Water Particles Example", 400, 400)
    main_window.setInputListener(GameLikeInputListener(main_window))

    simulator = PhysicsSimulator()

    particle_array = WaterParticleArray(N_PARTICLES)
    simulator.addBody(particle_array)
    simulator.addForceGenerator(GravityForceGenerator(particle_array))

    for i in xrange(N_PARTICLES):
        particle = particle_array.getReadOnlyParticle(i)
        particle_painter = PaintablePolyhedron(particle.geometry)
        main_window.addObject(particle_painter)

    main_window.addBeforeDrawSceneCallback(simulator.update)
    main_window.mainLoop()
