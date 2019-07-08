#!/usr/bin/env python3
"""
Displays robot Gen3 
"""
from mujoco_py import load_model_from_path, MjSim, MjViewer
from mujoco_py.modder import TextureModder
import os

# model = load_model_from_path("models/GEN3.xml")
model = load_model_from_path("models/gen3_robotiq.xml")
sim = MjSim(model)

viewer = MjViewer(sim)

t = 0

while True:
    sim.step()
    viewer.render()
    t += 1
    if t > 100 and os.getenv('TESTING') is not None:
        break
