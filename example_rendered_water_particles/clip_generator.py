import shutil
import time

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from scipy.misc import imsave

from example_rendered_water_particles.simulation_parameters import SIMULATION_TIME, \
    SIMULATION_TIMESTEP, TMP_FOLDER
import numpy as np


#===================================================================================================
# SimulationClipGenerator
#===================================================================================================
class SimulationClipGenerator(object):

    FPS = 60

    def __init__(self, main_window):
        self.current_simulation_time = 0.0
        self.next_save_frame_time = 0.0
        self.save_frame_timestep = 1.0 / self.FPS
        self.frames = []
        self._main_window = main_window
        main_window.addAfterDrawSceneCallback(self.saveDataAfterScene)


    def runSimulation(self):
        print '=' * 50
        print 'Simulation started!'
        print '=' * 50
        while self.current_simulation_time <= SIMULATION_TIME:
            start_time = time.time()
            self._main_window._drawScene()
            end_time = time.time()
            remain_simulation_time = SIMULATION_TIME - self.current_simulation_time
            remain_simulation_steps = remain_simulation_time / SIMULATION_TIMESTEP
            estimated_time = remain_simulation_steps * (end_time - start_time)
            print unicode(self.current_simulation_time) + '/' + unicode(SIMULATION_TIME),
            print '[Estimated time: ' + unicode(estimated_time) + ']'
            self.current_simulation_time += SIMULATION_TIMESTEP
        print '=' * 50
        print 'Simulation finished!'
        print '=' * 50


    def generateClip(self, filename):
        glutHideWindow()
        self.runSimulation()
        clip = ImageSequenceClip(self.frames, fps=self.FPS)
        clip.write_videofile(filename, fps=self.FPS)


    def saveDataAfterScene(self, delta_t):
        if self.current_simulation_time >= self.next_save_frame_time:
            pixels = glReadPixels(0, 0, 400, 400, GL_RGB, GL_UNSIGNED_BYTE, outputType=None)
            filename = str(TMP_FOLDER + '/t' + str(self.current_simulation_time) + '.png')
            imsave(filename, np.flipud(pixels))
            self.frames.append(filename)
            self.next_save_frame_time += self.save_frame_timestep
        self.current_simulation_time += delta_t
