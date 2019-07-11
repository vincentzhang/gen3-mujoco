#!/usr/bin/env python3
"""
Displays Kinova Gen3 robotic arm with Robotiq gripper
"""
from mujoco_py import load_model_from_path, MjSim, MjViewer
# from mujoco_py.modder import TextureModder
import os

xml_path = "models/Gen3Robotiq.xml"

class gen3_env(object):
    def __init__(self):
        #super(lab_env, self).__init__(env)
        # The real-world simulator
        self.model = load_model_from_path(xml_path)
        self.sim = MjSim(self.model)
        self.viewer = MjViewer(self.sim)

    def step(self):
    	self.sim.step()
    	self.viewer.render()
    	print(self.sim.data.qpos)
    	# self.sim.data.ctrl[:] = 0.0
    	for i in range(len(self.sim.data.qvel)):
    		self.sim.data.qvel[i] = 0.1
    	# self.sim.forward()

if __name__ == '__main__':
	env = gen3_env()
	t = 0
	while True:
	    env.step()
	    t += 1
	    if t > 100 and os.getenv('TESTING') is not None:
	    # if t > 1000:
	        break
    # env = create_env('Goal_LfD', None)
    # angles, state, images = env.reset(0)
    # print(state)
    # state, images = env.step([0.2, -0.2, 0.4, -1])
    #imshow(images[0])
    #imshow(images[1])
    # fig1 = env.sim.render(width = 960, height = 720, camera_name = 'workbench_camera')
    # fig1 = env.sim.render(width = 960, height = 720, camera_name = 'workbench_camera')
    # #imshow(fig1)
    # fig2 = env.sim.render(width = 960, height = 720, camera_name = 'upper_camera')
    # fig2 = env.sim.render(width = 960, height = 720, camera_name = 'upper_camera')
    # imshow(fig2)
    # state, images = env.step([0.2, -0.2, 0.4, 1])
    # print(state)
    # fig2 = env.sim.render(width = 960, height = 720, camera_name = 'upper_camera')
    # fig2 = env.sim.render(width = 960, height = 720, camera_name = 'upper_camera')
    # imshow(fig2)
    # state, images = env.step([0.2, 0, -0.2, 1])
    # print(state)
    # fig2 = env.sim.render(width = 960, height = 720, camera_name = 'upper_camera')
    # fig2 = env.sim.render(width = 960, height = 720, camera_name = 'upper_camera')
    # imshow(fig2)
    # state, images = env.step([0.2, 0, -0.2, 0.9])
    # print(state)
    # fig2 = env.sim.render(width = 960, height = 720, camera_name = 'upper_camera')
    # fig2 = env.sim.render(width = 960, height = 720, camera_name = 'upper_camera')
    # imshow(fig2)
