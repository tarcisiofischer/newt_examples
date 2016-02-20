import shutil

from example_rendered_water_particles.clip_generator import SimulationClipGenerator
from example_rendered_water_particles.simulation_parameters import SIMULATION_TIMESTEP, \
    SIMULATION_N_PARTICLES, OUTPUT_FILE_PATH, TMP_FOLDER
from example_rendered_water_particles.water_particle import WaterParticle
from gui.main_window import MainWindow
from gui.paintables.paintable_polyhedron import PaintablePolyhedron
from physics.delta_t_calculators import FixedDeltaTCalculator
from physics.force_generator.gravity_force_generator import GravityForceGenerator
from physics.physics_simulator import PhysicsSimulator


if __name__ == '__main__':
    main_window = MainWindow('Water Particles Example', 400, 400)
    main_window.calculateDeltaT = FixedDeltaTCalculator(delta_t=SIMULATION_TIMESTEP)
    simulator = PhysicsSimulator()
    for i in xrange(SIMULATION_N_PARTICLES):
        # Add particle to simulator
        particle = WaterParticle()
        simulator.addForceGenerator(GravityForceGenerator(particle))
        simulator.addBody(particle)
        # Add particle to scene
        particle_painter = PaintablePolyhedron(particle.geometry)
        main_window.addObject(particle_painter)

    main_window.addBeforeDrawSceneCallback(simulator.update)
    simulation_clip_generator = SimulationClipGenerator(main_window)
    simulation_clip_generator.generateClip(OUTPUT_FILE_PATH)

    # Comment this line if you want to see the generated frames in the TMP_FOLDER
    shutil.rmtree(TMP_FOLDER)
